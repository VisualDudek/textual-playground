"""
- create reactive attribute for TimeDisplay class
- create method that reacts to change in reactive attribute
- use query_one to get the TimeDisplay instance
- change the time_elapsed attribute of TimeDisplay instance
"""
from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Digits, Footer, Header
from textual import on
from textual.reactive import reactive


class TimeDisplay(Digits):
    """A widget to display elapsed time."""

    time_elapsed = reactive(0.0)

    def watch_time_elapsed(self) -> None:
        """Update the displayed time when it changes."""
        self.update(str(self.time_elapsed))


class Stopwatch(HorizontalGroup):
    """A stopwatch widget."""

    @on(Button.Pressed, "#start")
    def start_stopwatch(self):
        self.add_class("started")

    @on(Button.Pressed, "#stop")
    def stop_stopwatch(self):
        self.remove_class("started")

        time_display = self.query_one(TimeDisplay)
        time_display.time_elapsed = 7.4

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.00")


class StopwatchApp(App):
    """A Textual app to manage stopwatches."""

    CSS_PATH = "05_stopwatch.tcss"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield VerticalScroll(Stopwatch(), Stopwatch(), Stopwatch())


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()