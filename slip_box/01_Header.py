"""
Demonstrates:
- Basic Textual app structure (App, compose).
- Header widget usage (show_clock, time_format, name).
- Key bindings (BINDINGS).
- Custom actions (action_toggle_header).
- Widget querying (query_one).
- Dynamic widget property modification (header.tall).
"""

from textual.app import App, ComposeResult
from textual.widgets import Header


class HeaderApp(App):

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("h", "toggle_header", "Toggle Header"),
    ]

    def compose(self) -> ComposeResult:
        
        yield Header(show_clock=True, time_format="%H:%M:%S", name="Header Example")

    def action_toggle_header(self) -> None:
        """Toggle the visibility of the header."""
        header = self.query_one(Header)
        header.tall = not header.tall


if __name__ == "__main__":
    HeaderApp().run()