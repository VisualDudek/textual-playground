from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, RichLog
from textual.binding import Binding
from rich.text import Text
from rich.syntax import Syntax
from rich.table import Table
from datetime import datetime

import asyncio

class RichLogBoilerplateApp(App):
    """
    A boilerplate Textual application to demonstrate RichLog.
    """

    TITLE = "RichLog Boilerplate"
    SUB_TITLE = "Demonstrating RichLog Capabilities"

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

    BINDINGS = [
        Binding("ctrl+l", "add_log_entry", "Add Log Entry"),
        Binding("ctrl+s", "add_styled_entry", "Add Styled Entry"),
        Binding("ctrl+c", "add_code_entry", "Add Code Entry"),
        Binding("ctrl+t", "add_table_entry", "Add Table Entry"),
        Binding("ctrl+x", "clear_log", "Clear Log"),
        Binding("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield RichLog(id="my_rich_log", wrap=True, highlight=True, markup=True)
        yield Footer()

    async def on_mount(self) -> None:
        """Called when the app is first mounted."""
        log_widget = self.query_one(RichLog)
        log_widget.write("Welcome to the RichLog Boilerplate App!")
        log_widget.write(f"Current time: {datetime.now().isoformat()}")
        log_widget.write("--- Press key bindings to add more entries ---")
        log_widget.write(Text.assemble(
            ("Tip: ", "bold cornflower_blue"),
            ("Use ", "default"),
            ("Ctrl+L", "bold green"),
            (" to add a basic log entry.")
        ))

    async def on_ready(self) -> None:
        """Called when the app is ready."""
        log_widget = self.query_one(RichLog)
        log_widget.write("App is ready!")
        await asyncio.sleep(1)  # Simulate some delay for demonstration
        log_widget.write("App is ready!")

    async def action_add_log_entry(self) -> None:
        """Add a simple text log entry."""
        log_widget = self.query_one(RichLog)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_widget.write(f"[{timestamp}] A standard log entry has been added.")

    async def action_add_styled_entry(self) -> None:
        """Add a log entry with Rich Text styling."""
        log_widget = self.query_one(RichLog)
        styled_text = Text.assemble(
            ("This is a ", "default"),
            ("styled", "bold italic underline magenta on_cyan"),
            (" entry with multiple styles and ", "default"),
            ("colors!", "green"),
        )
        log_widget.write(styled_text)
        log_widget.write(Text("You can use [b]markup[/b] too if markup=True!", style="dim"))


    async def action_add_code_entry(self) -> None:
        """Add a syntax-highlighted code snippet."""
        log_widget = self.query_one(RichLog)
        python_code = """
from textual.app import App

class MyApp(App):
    def on_mount(self) -> None:
        self.bell()
"""
        syntax = Syntax(python_code, "python", theme="monokai", line_numbers=True)
        log_widget.write("--- Python Code Snippet ---")
        log_widget.write(syntax)
        log_widget.write("--- End Code Snippet ---")

    async def action_add_table_entry(self) -> None:
        """Add a Rich Table to the log."""
        log_widget = self.query_one(RichLog)
        table = Table(title="Sample Data Table")
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Name", style="magenta")
        table.add_column("Role", style="green")

        table.add_row("1", "Alice", "Developer")
        table.add_row("2", "Bob", "Designer")
        table.add_row("3", "Charlie", "Manager")

        log_widget.write("--- Data Table ---")
        log_widget.write(table)
        log_widget.write("--- End Data Table ---")


    async def action_clear_log(self) -> None:
        """Clear all entries from the RichLog."""
        log_widget = self.query_one(RichLog)
        log_widget.clear()
        log_widget.write("Log cleared.")

if __name__ == "__main__":
    app = RichLogBoilerplateApp()
    app.run()