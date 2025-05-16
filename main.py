import datetime  # For data parsing

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, ListView, ListItem, Label, Markdown
from textual.reactive import reactive

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

data = (
    {
    '_id': 'Visual Studio Code',
    'latest_videos': [
        {
            '_id': ObjectId('6826ceeae93db3c2a51c4abf'),
            'title': 'Our #1 tip for editing code',
            'video_id': 'ftlvuxm9BVY',
            'published_at': datetime.datetime(2025, 5, 15, 20, 15, 24),
            'channel_id': 'UCs5Y5_7XK8HLDX0SLNwkd3w',
            'channel_title': 'Visual Studio Code'
        },
        {
            '_id': ObjectId('6826ceeae93db3c2a51c4ac0'),
            'title': 'BYOK in VS Code',
            'video_id': 'tqoGDAAfSWc',
            'published_at': datetime.datetime(2025, 5, 15, 14, 1, 24),
            'channel_id': 'UCs5Y5_7XK8HLDX0SLNwkd3w',
            'channel_title': 'Visual Studio Code'
        },
        {
            '_id': ObjectId('6826ceeae93db3c2a51c4ac2'),
            'title': 'Vibe Coding at Microsoft Build - Day 3',
            'video_id': 'y4r6I2_Yk7c',
            'published_at': datetime.datetime(2025, 5, 15, 3, 48, 20),
            'channel_id': 'UCs5Y5_7XK8HLDX0SLNwkd3w',
            'channel_title': 'Visual Studio Code'
        }
    ]
},
{
    '_id': 'James Montemagno',
    'latest_videos': [
        {
            '_id': ObjectId('6825e5493381dd7b37bc15cc'),
            'title': 'Visual Studio 2022 + Copilot Agent Mode + Model Context Protocol (MCP) Servers Are Here!',
            'video_id': 'oPFecZHBCkg',
            'published_at': datetime.datetime(2025, 5, 14, 13, 1, 33),
            'channel_id': 'UCENTmbKaTphpWV2R2evVz2A',
            'channel_title': 'James Montemagno'
        },
        {
            '_id': ObjectId('6825e5493381dd7b37bc15cd'),
            'title': 'A Powerhouse PC for under $600?! MINISFORUM UM880 Plus Mini PC - Ryzen 7, 1TB SSD, 32GB RAM!',
            'video_id': 'WRF_rOh4vLE',
            'published_at': datetime.datetime(2025, 5, 9, 13, 30, 19),
            'channel_id': 'UCENTmbKaTphpWV2R2evVz2A',
            'channel_title': 'James Montemagno'
        },
        {
            '_id': ObjectId('6825e5493381dd7b37bc15ce'),
            'title': 'The Best Mac Mini M4 Accessory? Pulwtop Hub &amp; Dock Hands-On Review - M.2 SSD, HDMI, &amp; USB!',
            'video_id': 'dnn0Bid9C88',
            'published_at': datetime.datetime(2025, 4, 29, 14, 0, 55),
            'channel_id': 'UCENTmbKaTphpWV2R2evVz2A',
            'channel_title': 'James Montemagno'
        }
    ]
},
{
    '_id': 'GitHub',
    'latest_videos': [
        {
            '_id': ObjectId('6826d4ebc2abab02b8603406'),
            'title': 'Event in Spanish: Jueves de Quack: Especial VS Code y GitHub Copilot',
            'video_id': '2sckM3X4bCI',
            'published_at': datetime.datetime(2025, 5, 16, 4, 14, 12),
            'channel_id': 'UC7c3Kb6jYCRj4JOHHZTxKsQ',
            'channel_title': 'GitHub',
            'url': 'https://www.youtube.com/watch?v=2sckM3X4bCI',
            'duration': 'PT1H5M34S',
            'view_count': '229'
        },
        {
            '_id': ObjectId('6826d4ebc2abab02b8603407'),
            'title': 'Rubber Duck Thursdays - Building from requirements with Agent Mode',
            'video_id': 'pOr5nJ_XVDE',
            'published_at': datetime.datetime(2025, 5, 15, 23, 37, 15),
            'channel_id': 'UC7c3Kb6jYCRj4JOHHZTxKsQ',
            'channel_title': 'GitHub',
            'url': 'https://www.youtube.com/watch?v=pOr5nJ_XVDE',
            'duration': 'PT1H59M18S',
            'view_count': '712'
        },
        {
            '_id': ObjectId('6826d4ebc2abab02b8603408'),
            'title': "How GitHub Copilot empowers anyone to make apps | Kelly Ford's journey",
            'video_id': 'heubNV-QtuI',
            'published_at': datetime.datetime(2025, 5, 15, 16, 47, 4),
            'channel_id': 'UC7c3Kb6jYCRj4JOHHZTxKsQ',
            'channel_title': 'GitHub',
            'url': 'https://www.youtube.com/watch?v=heubNV-QtuI',
            'duration': 'PT2M3S',
            'view_count': '382'
        }
    ]
}
)

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
        ("q", "quit", "Quit")
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

    async def _update_video_details_for_item(self, item: ChannelListItem) -> None:
        """Updates the right pane with video details for the given channel item."""
        selected_channel_data = item.channel_data
        videos = selected_channel_data.get('latest_videos', [])
        
        channel_id_str = str(selected_channel_data.get('_id', 'Unknown Channel'))
        details_md = f"# {channel_id_str}\\n\\n"
        
        if videos:
            for video in videos:
                title = video.get('title', 'No Title')
                video_id = video.get('video_id', 'N/A')
                published_at = video.get('published_at', 'N/A')
                
                if isinstance(published_at, datetime.datetime):
                    published_at_str = published_at.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    published_at_str = str(published_at)

                details_md += f"## {title}\\n"
                details_md += f"- **Video ID:** {video_id}\\n"
                details_md += f"- **Published:** {published_at_str}\\n"
                if 'url' in video:
                    details_md += f"- **URL:** [{video.get('url')}]({video.get('url')})\\n"
                if 'duration' in video:
                    details_md += f"- **Duration:** {video.get('duration')}\\n"
                if 'view_count' in video:
                    details_md += f"- **Views:** {video.get('view_count')}\\n"
                details_md += "\\n---\\n"
        else:
            details_md += "No videos found for this channel."
        
        if self.video_details_pane:
            await self.video_details_pane.update(details_md)

    async def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Called when an item in the ListView is selected."""
        if isinstance(event.item, ChannelListItem):
            await self._update_video_details_for_item(event.item)

if __name__ == "__main__":
    app = VideoViewerApp() # Instantiate without data_filepath
    app.run()
