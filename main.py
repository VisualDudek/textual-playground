import datetime
import os  # For data parsing

from textual import work
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, ListView, ListItem, Label, Markdown
from textual.reactive import reactive

from dotenv import load_dotenv

from pymongo import MongoClient
from pymongo.server_api import ServerApi


# ObjectId class needs to be defined if it's used in the 'data' variable
# If ObjectId is not part of a standard library and was only for data.txt parsing context,
# ensure it's defined here or imported if 'data' variable relies on it.
# Assuming ObjectId is defined as it was in the previous full file context for the 'data' variable.
class ObjectId:
    def __init__(self, id_val):
        self.id_val = str(id_val)
    def __repr__(self):
        return f"ObjectId(\'{self.id_val}\')"
    def __str__(self):
        return self.id_val
    
# Load environment variables from .env file
load_dotenv()

# --- MongoDB Configuration ---
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DATABASE_NAME = "youtube_data" 
MONGO_COLLECTION_NAME = "videos"     

# --- MongoDB Setup ---
mongo_client = None
video_collection = None
try:
    print(f"Connecting to MongoDB at {MONGO_URI}...")
    mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000, server_api= ServerApi('1')) # Timeout for connection
    # Ping to confirm connection
    mongo_client.admin.command('ping') 
    print("Successfully connected to MongoDB.")
    
    db = mongo_client[MONGO_DATABASE_NAME]
    video_collection = db[MONGO_COLLECTION_NAME]

except Exception as e:
    print(f"Error: Could not connect to MongoDB or set up collection: {e}")
    print("Please ensure MongoDB is running and accessible, and MONGO_URI is correct.")
    exit(1) # Exit if DB connection fails, as storing data is a key goal.


# print("\n--- Fetching data from MongoDB View ---")
# for doc in db.latest_three.find():

# --- Fetch data from MongoDB View ---
data = (doc for doc in db.latest_ten.find())

# --- Data Loading Logic ---
# Removed load_data_from_file function

# --- Textual App Components ---
class ChannelListItem(ListItem):
    """A ListItem that holds channel data."""
    def __init__(self, channel_data) -> None:
        super().__init__(Label(str(channel_data.get('_id', 'Unknown Channel'))))
        self.channel_data = channel_data

class VideoViewerApp(App):
    """A Textual app to view video channel data."""

    CSS_PATH = "style.tcss"  # Path to the CSS file

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("r", "refresh_db", "Refresh DB"),  # Refresh data
    ]

    video_details_content = reactive("") # For right pane

    def __init__(self): # Removed data_filepath parameter
        super().__init__()
        self.all_data = list(data) # Use the global 'data' variable
        self.video_details_pane: Markdown | None = None


    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        with Horizontal(id="main_container"):
            with Vertical(id="left_pane"):
                yield ListView(id="channel_list_view")
            with Vertical(id="right_pane"):
                self.video_details_pane = Markdown(id="video_details_pane")
                yield self.video_details_pane
        yield Footer()

    def on_mount(self) -> None:
        """Called when the app is mounted."""
        list_view = self.query_one("#channel_list_view", ListView)
        
        if not self.all_data:
            if self.video_details_pane:
                self.video_details_pane.update("# Error\\nFailed to load data or no data available from `data.txt`.")
            return

        for channel_doc in self.all_data:
            item = ChannelListItem(channel_doc)
            list_view.append(item)
        
        list_view.focus()
        
        # Automatically select the first item and display its details
        if list_view.children and len(list_view.children) > 0:
            list_view.index = 0  # Visually select the first item
            first_item = list_view.children[0]
            if isinstance(first_item, ChannelListItem):
                self.call_later(self._update_video_details_for_item, first_item)

    def action_refresh_db(self) -> None:
        """Refresh the database connection and data."""
        global mongo_client, video_collection, data
        try:
            print(f"Reconnecting to MongoDB at {MONGO_URI}...")
            mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000, server_api= ServerApi('1'))
            mongo_client.admin.command('ping')
            print("Successfully reconnected to MongoDB.")
            
            db = mongo_client[MONGO_DATABASE_NAME]
            video_collection = db[MONGO_COLLECTION_NAME]
            data = (doc for doc in db.latest_ten.find())
            self.all_data = list(data)  # Update the all_data variable
            print("Data refreshed from MongoDB.")
        except Exception as e:
            print(f"Error: Could not reconnect to MongoDB or set up collection: {e}")
            print("Please ensure MongoDB is running and accessible, and MONGO_URI is correct.")
            exit(1)

        # Close teh MongoDB connection
        if mongo_client:
            mongo_client.close()
            print("MongoDB connection closed.")
        # Re-mount the app to refresh the data
        # self.on_mount() # Re-mounting is not necessary; we can just refresh the data
        # Re-render the app to show the updated data
        self.refresh()  # Refresh the app to show the updated data

        
    @work(exclusive=True)
    async def _update_video_details_for_item(self, item: ChannelListItem | None) -> None: # Allow item to be None
        """Updates the right pane with video details for the given channel item."""
        if not item: # Handle case where no item is highlighted (e.g., empty list)
            if self.video_details_pane:
                await self.video_details_pane.update("No item selected.")
            return

        selected_channel_data = item.channel_data
        videos = selected_channel_data.get('latest_videos', [])
        
        channel_id_str = str(selected_channel_data.get('_id', 'Unknown Channel'))
        details_md = f"# {channel_id_str}\n\n"
        
        if videos:
            for video in videos:
                title = video.get('title', 'No Title')
                published_at = video.get('published_at', 'N/A')
                video_duration = video.get('duration', 'N/A')

                # Convert published_at to a string if it's a datetime object

                if isinstance(published_at, datetime.datetime):
                    published_at_str = published_at.strftime("%Y-%m-%d %H:%M:%S")
                    published_at_short = published_at.strftime("%Y-%m-%d")
                else:
                    published_at_str = str(published_at)
                    published_at_short = str(published_at)

                details_md += f"- {published_at_short} [{title}](https://www.youtube.com/watch?v={video.get('video_id', 'N/A')})"
                details_md += f" **Duration:** {video_duration}\n"

        else:
            details_md += "No videos found for this channel."
        
        if self.video_details_pane:
            await self.video_details_pane.update(details_md)

    async def on_list_view_highlighted(self, event: ListView.Highlighted) -> None: # Changed from on_list_view_selected
        """Called when an item in the ListView is highlighted.""" # Docstring updated
        if isinstance(event.item, ChannelListItem):
            # await self._update_video_details_for_item(event.item)
            self._update_video_details_for_item(event.item)
        elif event.item is None: # Handle case where highlighting is removed (e.g. list becomes empty or loses focus)
             await self._update_video_details_for_item(None)


if __name__ == "__main__":


    app = VideoViewerApp() # Instantiate without data_filepath
    app.run()
