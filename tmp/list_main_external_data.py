import os
import pickle

from textual.app import App
from textual.widgets import ListView, ListItem, Footer, Label, DataTable, Link
from textual.binding import Binding
from textual.containers import Horizontal
from textual import on
from rich.text import Text
from dataclasses import dataclass, field, fields
from datetime import datetime, date, timedelta
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId


DATA = None
COLUMN_HEADERS = ("Time", "Title", "Duration")


# nice trick with self.data and super() init Label
class MyListItem(ListItem):
    def __init__(self, data):
        super().__init__(Label(data))
        self.data = data

class CustomListView(ListView):

    BINDINGS = [
        Binding("enter", "select_cursor", "Select", show=False),
        Binding("k", "cursor_up", "Cursor up", show=False),
        Binding("j", "cursor_down", "Cursor down", show=False),
    ]

    def on_mount(self):
        for channel_name in DATA.keys():
            self.append(MyListItem(channel_name))
    

class CustomDataTable(DataTable):

    BINDINGS = [
    # Binding("enter", "select_cursor", "Select", show=True),
    Binding("k", "cursor_up", "Cursor up", show=True),
    Binding("j", "cursor_down", "Cursor down", show=True),
    Binding("t", "style_row", "Toggle row", show=True),
    ]

    def on_mount(self) -> None:
        self.cursor_type = "row"
        self.add_columns(*COLUMN_HEADERS)
        # self.add_rows(ROWS)
        self.log(self.columns)
        self.cursor_foreground_priority = 'renderable'

    def update_table(self, key):
        self.clear()
        for video in DATA[key]:
            # if date is today, change color
            if video.published_at.date() == date.today():
                title = Text(video.title, style="bold red")
            elif video.published_at.date() == date.today() - timedelta(days=1):
                title = Text(video.title, style="bold green")
            else:
                title = video.title
            
            row = (video.published_at, title, video.duration)
            self.add_row(*row, key=video.video_id)

    def action_style_row(self):
        row, col = self.cursor_row, self.cursor_column
        self.log(self.get_cell_at((row, col)))
        value = self.get_cell_at((row, col))
        self.update_cell_at((row, col), Text(str(value), style="bold red"))

    # def action_select_cursor(self):
    #     row, col = self.cursor_row, self.cursor_column
    #     value = self.get_cell_at((row, 1))
    #     self.log(value)

    @on(DataTable.RowSelected)
    def open_url_in_browser(self, event: DataTable.RowSelected):
        video_id = event.row_key.value
        self.app.open_url(f"https://www.youtube.com/watch?v={video_id}")
        

class MyApp(App):

    CSS = """
    CustomListView {
        width: 2fr;
    }
    CustomDataTable {
        width: 9fr;
    }
    """

    BINDINGS = [
        Binding("q", "exit", "Exit"),
        Binding("l", "focus_datatable", show=False)
        ]
    
    def compose(self):
        yield Footer()
        with Horizontal():
            yield CustomListView()
            yield CustomDataTable()

    def action_exit(self):
        self.exit()

    def action_focus_datatable(self):
        if self.query_one(CustomListView).has_focus:
            self.query_one(CustomDataTable).focus()
        else:
            self.query_one(CustomListView).focus()

    @on(ListView.Highlighted)
    def update_data_table(self, event: ListView.Highlighted):
        self.log(event.item.data)
        self.query_one(CustomDataTable).update_table(event.item.data)
    

def load_data():
    # with open("data.pkl", "rb") as f:
    #     loaded_data = pickle.load(f)

    print(f"Connecting to MongoDB at {MONGO_URI}...")
    mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000, server_api= ServerApi('1')) # Timeout for connection
    # Ping to confirm connection
    mongo_client.admin.command('ping') 
    print("Successfully connected to MongoDB.")

    db = mongo_client[MONGO_DATABASE_NAME]
    video_collection = db[MONGO_COLLECTION_NAME]

    loaded_data = list(db.latest_ten.find())

    data = dict()
    field_names = {f.name for f in fields(Video)}

    for item in loaded_data:
        channel_name = item["_id"]
        videos = []

        for video in item["latest_videos"]:
            filtered_data = {k:v for k,v in video.items() if k in field_names}
            videos.append(Video(**filtered_data))

        data[channel_name] = videos

    if mongo_client:
        mongo_client.close()
        print("\nMongoDB connection closed.")

    return data


@dataclass
class Video:
    _id: ObjectId
    title: str
    video_id: str
    published_at: datetime
    url: str = field(default="N/A")
    duration: str = field(default="N/A")


if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()  

    # --- MongoDB Configuration ---
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DATABASE_NAME = "youtube_data"
    MONGO_COLLECTION_NAME = "videos"     

    DATA = load_data()
    app = MyApp()
    app.run()