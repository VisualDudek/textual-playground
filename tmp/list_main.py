from textual.app import App
from textual.widgets import ListView, ListItem, Footer, Label, DataTable, Link
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual import on
from rich.text import Text
from itertools import cycle

DATA = {
    "a": (4, "Joseph Schooling", "Singapore", 50.39),
    "b": (6, "László Cseh", "Hungary", 51.14),
    "c": (7, "Tom Shields", "United States", 51.73),
}

COLUMN_HEADERS = ("lane", "swimmer", "country", "time")

ROWS = [
    (4, "Joseph Schooling", "Singapore", 50.39),
    (2, "Michael Phelps", "United States", 51.14),
    (5, "Chad le Clos", "South Africa", 51.14),
    (6, "László Cseh", "Hungary", 51.14),
    (3, "Li Zhuhao", "China", 51.26),
    (8, "Mehdy Metella", "France", 51.58),
    (7, "Tom Shields", "United States", 51.73),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84),
    (10, "Darren Burns", "Scotland", 51.84),
]

# nice trick with self.data and super() init Label
class MyListItem(ListItem):
    def __init__(self, data):
        super().__init__(Label(data))
        self.data = data

class CustomListView(ListView):

    BINDINGS = [
        Binding("enter", "select_cursor", "Select", show=False),
        Binding("k", "cursor_up", "Cursor up", show=False),
        Binding("j", "cursor_down", "Cursor down", show=False),
    ]

    def on_mount(self):
        for item in DATA.keys():
            self.append(MyListItem(item))
    

class CustomDataTable(DataTable):

    BINDINGS = [
    # Binding("enter", "select_cursor", "Select", show=False),
    Binding("k", "cursor_up", "Cursor up", show=True),
    Binding("j", "cursor_down", "Cursor down", show=True),
    Binding("t", "style_row", "Toggle row", show=True),
    ]

    def on_mount(self) -> None:
        self.cursor_type = "row"
        self.add_columns(*COLUMN_HEADERS)
        self.add_rows(ROWS)
        self.cursor_foreground_priority = 'renderable'

    def update_table(self, key):
        self.add_row(*DATA[key])

    def action_style_row(self):
        row, col = self.cursor_row, self.cursor_column
        self.log(self.get_cell_at((row, col)))
        value = self.get_cell_at((row, col))
        self.update_cell_at((row, col), Text(str(value), style="bold red"))

class MyApp(App):

    CSS = """
    CustomListView {
        width: 1fr;
    }
    CustomDataTable {
        width: 9fr;
    }
    """

    BINDINGS = [
        Binding("q", "exit", "Exit"),
        Binding("l", "focus_datatable", show=False)
        ]
    
    def compose(self):
        yield Footer()
        with Horizontal():
            yield CustomListView()
            yield CustomDataTable()

    def action_exit(self):
        self.exit()

    def action_focus_datatable(self):
        if self.query_one(CustomListView).has_focus:
            self.query_one(CustomDataTable).focus()
        else:
            self.query_one(CustomListView).focus()

    @on(ListView.Highlighted)
    def update_data_table(self, event: ListView.Highlighted):
        self.log(event.item.data)
        self.query_one(CustomDataTable).update_table(event.item.data)
    


if __name__ == "__main__":
    app = MyApp()
    app.run()