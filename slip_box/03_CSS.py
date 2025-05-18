"""
This code demonstrates how to use: 
- an external CSS file (CSS_PATH) with a Textual application, 
- how to use the Vertical container,
- and how to apply an ID to a widget for specific styling.
"""
from textual.app import App, ComposeResult
from textual.widgets import Header, Label
from textual.containers import Vertical


class ContainerApp(App):

    # CSS = #"""
    # Label {
    #     color: white;
    #     background: blue;
    # }
    # #label_2 {
    #     color: red;
    #     background: green;
    # }
    # """

    CSS_PATH = '02_container_CSS.tcss'


    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical(id="main_container"):
            yield Label("Hello, World!")
            yield Label("Hello, World!", id="label_2")


if __name__ == "__main__":
    ContainerApp().run()