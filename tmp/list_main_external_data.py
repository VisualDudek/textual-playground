import pickle

from textual.app import App
from textual.widgets import ListView, ListItem, Footer, Label, DataTable, Link
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual import on
from rich.text import Text
from itertools import cycle
from dataclasses import dataclass, field, fields
from datetime import datetime


DATA = {
    "a": (4, "Joseph Schooling", "Singapore", 50.39),
    "b": (6, "László Cseh", "Hungary", 51.14),
    "c": (7, "Tom Shields", "United States", 51.73),
}

COLUMN_HEADERS = ("Time", "Title", "Duration")

ROWS = [
    (4, "Joseph Schooling", "Singapore", 50.39),
    (2, "Michael Phelps", "United States", 51.14),
    (5, "Chad le Clos", "South Africa", 51.14),
    (6, "László Cseh", "Hungary", 51.14),
    (3, "Li Zhuhao", "China", 51.26),
    (8, "Mehdy Metella", "France", 51.58),
    (7, "Tom Shields", "United States", 51.73),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84),
    (10, "Darren Burns", "Scotland", 51.84),
]

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
            row = (video.published_at, video.title, video.duration)
            self.add_row(*row, key=video.url)

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
        url = event.row_key
        self.log(url)
        self.app.open_url(url.value)
        

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
    with open("data.pkl", "rb") as f:
        loaded_data = pickle.load(f)

    # data = { d["_id"]: d for d in loaded_data }

    data = dict()
    field_names = {f.name for f in fields(Video)}

    for item in loaded_data:
        channel_name = item["_id"]
        videos = []

        for video in item["latest_videos"]:
            filtered_data = {k:v for k,v in video.items() if k in field_names}
            videos.append(Video(**filtered_data))

        data[channel_name] = videos


    return data

@dataclass
class Video:
    title: str
    video_id: str
    published_at: datetime
    url: str = field(default="N/A")
    duration: str = field(default="N/A")


if __name__ == "__main__":
    DATA = load_data()
    app = MyApp()
    app.run()