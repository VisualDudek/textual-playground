# Keybind and Action Demonstration

This Textual application demonstrates the use of key bindings to trigger actions within the app.

## Functionality

The application (`main.py`) sets up a simple user interface with a header, a footer, and a central static display area for messages.

It defines the following key bindings:

-   **`q`**: Pressing 'q' will quit the application.
-   **`h`**: Pressing 'h' will trigger the `action_say_hello` method, which updates the static display to show "Hello from the keybind action!".
-   **`c`**: Pressing 'c' will trigger the `action_clear_message` method, which updates the static display to show "Message cleared. Press 'h' to say hello again.".

Initially, the application displays the message: "Press 'h' to see a message, 'Ctrl+C' to clear, or 'q' to quit."

