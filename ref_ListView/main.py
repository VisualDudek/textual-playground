from textual.app import App, ComposeResult
from textual.widgets import Footer, Label, ListItem, ListView, Link, Switch
from textual.containers import HorizontalGroup
from textual import on


class ListViewExample(App):
    CSS_PATH = "list_view.tcss"

    def compose(self) -> ComposeResult:
        yield ListView(
            ListItem(HorizontalGroup(Label("One"), Switch(value=True))),
            ListItem(Label("Two")),
            ListItem(Label("Three")),
            ListItem(Link(
            "Go to textualize.io",
            url="https://textualize.io",
            tooltip="Click me",
            )),
        )
        yield Footer()

    @on(ListView.Selected)
    def abc(self, event: ListView.Selected) -> None:
        """Log the selected item."""
        it: ListItem = event.item
        # child_wiget = it.children[0]
        
        # self.log(f"Selected {it} with child {child_wiget}, text: {child_wiget.text}")

        # self.log(it.query_one(Link).url)
        # child_wiget.focus()

        it.toggle_class("selected")



if __name__ == "__main__":
    app = ListViewExample()
    app.run()