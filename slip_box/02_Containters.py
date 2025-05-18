"""
This script demonstrates:
- Basic Textual App structure.
- UI layout using the `compose` method.
- Usage of `Header` and `Label` widgets.
- Arranging widgets horizontally using `Horizontal` container.
- Two methods for adding children to a container.
"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Label, Footer
from textual.containers import Horizontal



class ContainerApp(App):

    def compose(self):
        yield Header()
        yield Footer()
        with Horizontal(id="main_container"):
            yield Label("Hello, World!")
            yield Label("Hello, World!")

        # Also works but above is more readable
        yield Horizontal(
            Label("Hello, World!"),
            Label("Hello, World!"),
            id="horizontal_container"
        )

if __name__ == "__main__":
    ContainerApp().run()