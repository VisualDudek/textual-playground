from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Container

class KeybindApp(App):
    """A simple Textual app to demonstrate key bindings."""

    # Define the key bindings
    BINDINGS = [
        ("q", "quit_app", "Quit the application"),
        ("h", "say_hello", "Say Hello"),
        # Ctrl+C is not a valid key binding in Textual, but you can use other modifiers
        # you can try to explicite it in the BINDINGS list using a 5-tuple biding format
        # (key, action, description, modifier, name)
        # ("ctrl+c", "clear_message", "Clear Message"), # Example of a modifier key
        ("c", "clear_message", "Clear Message"), 
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Container(Static("Press 'h' to see a message, 'Ctrl+C' to clear, or 'q' to quit.", id="message_display"))
        yield Footer()

    # Action methods correspond to the second element in the BINDINGS tuples
    def action_quit_app(self) -> None:
        """Called when 'q' is pressed."""
        self.exit("User pressed 'q' to quit.")

    def action_say_hello(self) -> None:
        """Called when 'h' is pressed."""
        message_widget = self.query_one("#message_display", Static)
        message_widget.update("Hello from the keybind action!")

    def action_clear_message(self) -> None:
        """Called when 'Ctrl+C' is pressed."""
        message_widget = self.query_one("#message_display", Static)
        message_widget.update("Message cleared. Press 'h' to say hello again.")

if __name__ == "__main__":
    app = KeybindApp()
    app.run()