from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Label, Static, Header, Footer, RichLog
from rich.text import Text
from datetime import datetime
import asyncio

class PopupScreen(ModalScreen):
    """A simple modal screen for the popup."""

    # Define a keybinding to close this screen (e.g., Escape key)
    BINDINGS = [
        ("q", "close_popup", "Close Popup")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield RichLog(id="my_rich_log", wrap=True, highlight=True, markup=True)
        yield Footer()

    def action_close_popup(self) -> None:
        self.app.pop_screen()

    async def on_mount(self) -> None:
        """Called when the app is first mounted."""
        log_widget = self.query_one(RichLog)
        log_widget.write("Welcome to the RichLog Boilerplate App!")
        log_widget.write(f"Current time: {datetime.now().isoformat()}")
        log_widget.write("--- Press key bindings to add more entries ---")
        log_widget.write("This is a new log entry.")

    async def on_ready(self) -> None:
        """Called when the app is ready."""
        log_widget = self.query_one(RichLog)
        log_widget.write("App is ready!")
        await asyncio.sleep(1)
        log_widget.write("App is ready!")
        await asyncio.sleep(1)
        log_widget.write("App is ready!")

class MainApp(App):
    """Main application class."""

    CSS = """
    Screen {
        align: center middle;
    }

    RichLog {
        width: 80%;
        height: 80%;
        border: round $primary;
        margin: 1 2;
        background: $surface; /* Ensure background for better readability */
    }
    """

    # Define a keybinding to open the popup screen (e.g., 'p' key)
    BINDINGS = [
        ("p", "request_popup", "Open Popup")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Press 'p' to open the popup.")
        yield Footer()

    async def action_request_popup(self) -> None:
        """Open the popup screen."""
        self.push_screen(PopupScreen())

if __name__ == "__main__":
    app = MainApp()
    app.run()