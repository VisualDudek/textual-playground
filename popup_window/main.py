from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Label, Static, Header, Footer

class PopupScreen(ModalScreen):
    """A simple modal screen for the popup."""

    # Define a keybinding to close this screen (e.g., Escape key)
    BINDINGS = [
        ("escape", "pop_screen", "Close Popup")
    ]

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("This is a popup window!", id="popup_message"),
            Button("Close (or press Esc)", variant="primary", id="close_popup"),
            id="popup_dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press to close the popup."""
        if event.button.id == "close_popup":
            self.app.pop_screen()

class MainApp(App):
    """Main application class."""

    CSS_PATH = "style.tcss"  # Path to the CSS file

    # Define a keybinding to open the popup screen (e.g., 'p' key)
    BINDINGS = [
        ("p", "request_popup", "Open Popup")
    ]

    # Register the popup screen with a name
    # SCREENS = {"popup": PopupScreen}

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Press 'p' to open the popup.")
        yield Footer()

    def action_request_popup(self) -> None:
        """Open the popup screen."""
        self.push_screen(PopupScreen())

if __name__ == "__main__":
    app = MainApp()
    app.run()