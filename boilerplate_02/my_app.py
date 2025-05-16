# my_app.py

# Import necessary classes from the textual.app module.
# App is the base class for all Textual applications.
# ComposeResult is a type hint for the return value of the compose method,
# indicating it yields Widget instances.
from textual.app import App, ComposeResult

# Import widget classes from textual.widgets.
# Header: A standard widget for displaying a title at the top of the screen.
# Footer: A standard widget for displaying key bindings or status at the bottom.
# Static: A simple widget for displaying static or dynamic text content.
# Button: A widget that users can click to trigger actions.
# Input: A widget for single-line text input from the user.
from textual.widgets import Header, Footer, Static, Button, Input

# Import container widgets from textual.containers.
# VerticalScroll is a container that arranges its children vertically
# and provides scrolling if the content exceeds the available space.
from textual.containers import VerticalScroll

# Define the main application class, inheriting from textual.app.App.
# The type hint `App[str]` indicates that this app, when it exits,
# might return a string value (e.g., via self.exit("some_value")).
# If no specific return value is intended, App[None] can be used.
class MyBoilerplateApp(App[str]):
    """
    A heavily commented boilerplate Textual application.
    This class defines the structure and behavior of the TUI.
    """

    # TITLE sets the application title displayed in the Header widget (if used)
    # and potentially by the terminal window manager.
    TITLE = "Boilerplate Textual App"

    # SUB_TITLE provides an optional subtitle, also displayed in the Header.
    SUB_TITLE = "A Starting Point for Your TUI"

    # CSS_PATH specifies the path to the external CSS file for styling the app.
    # Textual will load and apply styles from this file.
    # If None, or if the file doesn't exist, default styles apply.
    CSS_PATH = "boilerplate.tcss"

    # BINDINGS define global key bindings for the application.
    # Each tuple is (key_description, action_name, display_text).
    # 'ctrl+q' will call the action_quit method.
    # 'ctrl+c' is often a default exit binding as well.
    BINDINGS = [
        ("ctrl+q", "quit", "Quit App"),
    ]

    # The compose method is where the initial UI layout is defined.
    # It must be a generator function that yields Widget instances.
    # These widgets are added to the application's screen in the order they are yielded.
    def compose(self) -> ComposeResult:
        """
        Create and arrange the initial child widgets for the application.
        This method is called by Textual when the app starts.
        """
        # Yield a Header widget. Textual automatically uses TITLE and SUB_TITLE.
        # The Header is typically docked to the top of the screen (see CSS).
        yield Header()

        # Yield a VerticalScroll container. This widget will contain other widgets
        # and allow them to scroll vertically if their combined height exceeds
        # the container's height. It helps manage content that might not fit.
        # The `id` attribute is crucial for CSS styling and for querying the DOM.
        # Using an `id` allows specific targeting in CSS (e.g., #main_content)
        # and in Python code (e.g., self.query_one("#main_content")).
        with VerticalScroll(id="main_content"):
            # Yield a Static widget to display a welcome message.
            # This widget is placed inside the VerticalScroll container.
            # `id` allows styling and access.
            yield Static("Welcome to your Textual Boilerplate!", id="welcome_message")

            # Yield an Input widget for user text entry.
            # `placeholder` provides hint text.
            # `id` is essential for retrieving its value later.
            yield Input(placeholder="Enter some text here...", id="my_input")

            # Yield a Button widget.
            # The first argument is the button's label.
            # `variant="primary"` is a common way to style a primary action button (see CSS).
            # `id` helps in identifying the button if multiple buttons exist or for specific styling.
            yield Button("Submit", variant="primary", id="submit_button")

            # Yield another Static widget, initially empty.
            # This will be used to display output based on user interaction.
            # `id` allows us to find and update this widget.
            yield Static(id="output_area")

        # Yield a Footer widget. Textual automatically populates this with BINDINGS.
        # The Footer is typically docked to the bottom of the screen (see CSS).
        yield Footer()

    # Event handler for when the "Submit" button is pressed.
    # Textual's event system automatically calls methods named `on_<widget_type>_<event_name>`
    # or, more specifically for buttons with IDs, `on_button_pressed` can be decorated
    # with `@on(Button.Pressed, "#submit_button")`.
    # This simpler form `on_button_pressed` handles any Button.Pressed event.
    # The `async` keyword indicates this is an asynchronous method. Textual's event
    # handlers can be async, allowing for non-blocking operations if needed.
    # Textual is built on Python's asyncio.
    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handles the Button.Pressed event, specifically for our submit button.
        This method is called when any button in the app is pressed.
        """
        # Check if the pressed button is the one we're interested in by its ID.
        # The `event.button` attribute gives access to the Button instance that was pressed.
        # This check is important if you have multiple buttons and need different actions.
        if event.button.id == "submit_button":
            # Query the DOM to get the Input widget using its ID.
            # `self.query_one` expects to find exactly one widget matching the selector.
            # The second argument, `Input`, specifies the expected type for type checking.
            input_widget = self.query_one("#my_input", Input)

            # Query the DOM to get the Static widget for output.
            output_area = self.query_one("#output_area", Static)

            # Get the current value from the Input widget.
            user_text = input_widget.value

            # Update the content of the 'output_area' Static widget.
            # The `update` method re-renders the widget with new content.
            # f-strings are used for easy string formatting.
            output_area.update(f"You entered: '{user_text}' and clicked the button!")

            # Clear the input field after submission for better UX.
            input_widget.value = ""

            # Optionally, play a system bell sound as feedback.
            # `self.bell()` is a built-in App method.
            self.bell()

    # Action methods are prefixed with `action_`.
    # They are called when a binding is invoked (e.g., 'ctrl+q' calls 'action_quit').
    def action_quit(self) -> None:
        """
        Called when the 'quit' action is triggered (e.g., by a binding).
        This method exits the application.
        """
        self.exit("Application closed by user.")


# This is the standard Python entry point.
# The code inside this block runs only when the script is executed directly
# (not when imported as a module).
if __name__ == "__main__":
    # Create an instance of our Textual application.
    app = MyBoilerplateApp()
    # Call the run() method to start the application.
    # This takes over the terminal, sets up the UI, and starts the event loop.
    # The optional `log_path` argument can be used to redirect Textual's internal
    # logging to a file for debugging.
    app.run()