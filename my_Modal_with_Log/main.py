from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Log, Static, Header, Footer
import asyncio
from textual import work
from datetime import datetime

class PopupScreen(ModalScreen):
    """A simple modal screen for the popup."""

    # Define a keybinding to close this screen (e.g., Escape key)
    BINDINGS = [
        ("q", "close_popup", "Close Popup")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Log()
        yield Footer()

    def action_close_popup(self) -> None:
        self.app.pop_screen()

    def on_mount(self) -> None:
        """Called when the app is first mounted."""
        log = self.query_one(Log)
        log.write_line("Welcome to the RichLog Boilerplate App!")
        log.write_line("--- Press key bindings to add more entries ---")
        log.write_line("This is a new log entry.")
        self.run_io_task()


    @work(exclusive=True)
    async def run_io_task(self) -> None:
        """Add a simple text log entry."""
        log = self.query_one(Log)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write_line(f"[{timestamp}] A standard log entry has been added.")
        await asyncio.sleep(1)
        log.write_line(f"[{timestamp}] A standard log entry has been added.")

    # async def on_ready(self) -> None:
    #     """Called when the app is ready."""
    #     log = self.query_one(Log)
    #     log.write_line("Welcome to the RichLog Boilerplate App!")
    #     log.write_line("--- Press key bindings to add more entries ---")
    #     log.write_line("This is a new log entry.")
    #     await asyncio.sleep(1)
    #     log.write_line("This is a new log entry.")
    #     await asyncio.sleep(1)
    #     log.write_line("This is a new log entry.")

class MainApp(App):
    """Main application class."""

    CSS = """
    Screen {
        align: center middle;
    }

    Log {
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
        await self.push_screen(PopupScreen())

if __name__ == "__main__":
    app = MainApp()
    app.run()