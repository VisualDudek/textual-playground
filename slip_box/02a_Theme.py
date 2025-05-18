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

    def on_mount(self) -> None:
        self.theme = "gruvbox"

    

if __name__ == "__main__":
    ContainerApp().run()