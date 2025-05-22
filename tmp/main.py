from textual.app import App
from textual.widgets import Placeholder, Header, Footer, Button, Label, Static
from textual.containers import HorizontalGroup, Vertical, Horizontal
from textual import on


class TimerBar(HorizontalGroup):

    couter = 0

    def compose(self):
        yield Static("Static")
        yield Button(label="start", id="start")
        yield Button(label="Stop")

    def on_mount(self):
        self.timer = self.set_interval(1, self.update_label, pause=True)

    def update_label(self):
        label = self.query_one(Static)
        label.update(str(self.couter))
        self.couter += 1

    @on(Button.Pressed, "#start")
    def start_timer(self):
        self.timer.resume()


class StopwatchApp(App):

    CSS = """
    TimerBar {
        margin: 2;
        align: center middle;
    }
    Static {
        width: auto;
    }
    """

    def compose(self):
        yield Header()
        yield Footer()
        yield TimerBar()



if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
