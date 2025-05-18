"""
- add update time method to TimeDisplay class
- create Timer in on_mount method, make it pause, keep reference to it
- call update_time method at periodic intervals
- resume timer when start method is called
- pause timer when stop method is called
"""
from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Digits, Footer, Header
from textual import on
from textual.reactive import reactive
from time import monotonic


class TimeDisplay(Digits):
    """A widget to display elapsed time."""

    time_elapsed = reactive(0.0)
    start_time = monotonic()

    def on_mount(self):
        """Call fn. at periodic intervals."""
        self.update_timer = self.set_interval(
            1/60, 
            self.update_time,
            pause=True,
            )

    def watch_time_elapsed(self) -> None:
        """Update the displayed time when it changes."""
        self.update(str(self.time_elapsed))

    def start(self):
        self.start_time = monotonic()
        self.update_timer.resume()

    def stop(self):
        self.time_elapsed += monotonic() - self.start_time
        self.update_timer.pause()

    def reset(self):    
        self.time_elapsed = 0.0

    def update_time(self):
        self.time_elapsed = monotonic() - self.start_time


class Stopwatch(HorizontalGroup):
    """A stopwatch widget."""

    @on(Button.Pressed, "#start")
    def start_stopwatch(self):
        self.add_class("started")

        self.query_one(TimeDisplay).start()

    @on(Button.Pressed, "#stop")
    def stop_stopwatch(self):
        self.remove_class("started")

        self.query_one(TimeDisplay).stop()

    @on(Button.Pressed, "#reset")
    def reset_stopwatch(self):
        time_display = self.query_one(TimeDisplay).reset()


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