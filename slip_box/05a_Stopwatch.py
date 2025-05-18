"""
Use decorator on a class method to handle events.
"""
from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Digits, Footer, Header
from textual import on


class TimeDisplay(Digits):
    """A widget to display elapsed time."""


class Stopwatch(HorizontalGroup):
    """A stopwatch widget."""

    # def on_button_pressed(self, event: Button.Pressed) -> None:
    #     """Event handler called when a button is pressed."""
    #     if event.button.id == "start":
    #         self.add_class("started")
    #     elif event.button.id == "stop":
    #         self.remove_class("started")
    @on(Button.Pressed, "#start")
    def start_stopwatch(self):
        self.add_class("started")

    @on(Button.Pressed, "#stop")
    def stop_stopwatch(self):
        self.remove_class("started")

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