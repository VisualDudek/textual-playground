from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, DataTable, Button, Static

# Sample data for the application (e.g., tasks and metrics).
# A list of task entries (id, title, status, due_date) to populate the DataTable.
TASKS = [
    (1, "Implement login feature", "In Progress", "2025-05-20"),
    (2, "Write unit tests", "Completed", "2025-04-30"),
    (3, "Update documentation", "Pending", "2025-05-18"),
    (4, "Refactor codebase", "In Progress", "2025-06-01"),
    (5, "Release version 1.0", "Pending", "2025-06-15"),
]

# Calculate some metrics from the TASKS data for the dashboard overview.
total_tasks = len(TASKS)
completed_tasks = sum(1 for t in TASKS if t[2] == "Completed")
pending_tasks = sum(1 for t in TASKS if t[2] == "Pending")
in_progress_tasks = sum(1 for t in TASKS if t[2] == "In Progress")

# Prepare metric data as list of tuples (metric_name, value) for the dashboard table.
METRICS = [
    ("Total Tasks", total_tasks),
    ("Completed Tasks", completed_tasks),
    ("In Progress Tasks", in_progress_tasks),
    ("Pending Tasks", pending_tasks),
]

class DashboardScreen(Screen):
    """The main dashboard screen of the TUI application.
    
    This screen shows an overview of key metrics and provides navigation options.
    It contains a Header, a Static welcome message, a DataTable of metrics,
    and a Button to navigate to the detailed data view.
    """
    # Set the screen title (overrides the App title when this screen is active).
    TITLE = "Dashboard"
    
    def compose(self) -> ComposeResult:
        """Create and add widgets to the dashboard screen."""
        # Compose is similar to App.compose, but for an individual Screen.
        # It should yield the UI elements (widgets) that make up this screen.
        yield Header()  # Header displays the application title and (optionally) subtitle.
        # Place a Static welcome message and a DataTable of metrics side by side using a Horizontal container.
        yield Horizontal(
            Static("Welcome to the Dashboard!\nUse 'd' to open the Data View or press the button below.", id="welcome"),
            DataTable(id="metrics_table"),
            id="metrics_row"
        )
        # A Button to navigate to the detail view (as an alternative to using the keyboard shortcut).
        yield Button(label="Open Data View", id="open_data_button", variant="success")
        # Footer displays key bindings defined in the App (like hints for navigation).
        yield Footer()
    
    def on_mount(self) -> None:
        """Event handler called when the screen is added to the app.
        
        Here we populate the DataTable with the metrics data once the screen is mounted.
        """
        # Query for the DataTable widget by its ID to populate it with data.
        table = self.query_one(DataTable)
        # Add two columns: "Metric" and "Value" for the metrics overview.
        table.add_columns("Metric", "Value")
        # Add each metric row from METRICS data.
        for metric_name, value in METRICS:
            table.add_row(metric_name, str(value))
        # Optionally, set some visual properties of the table.
        table.cursor_type = "row"  # Highlight entire rows when navigating (read-only summary data here).
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events on this screen."""
        # This will catch all Button pressed events in this screen.
        # Identify which button was pressed by its id.
        if event.button.id == "open_data_button":
            # When the "Open Data View" button is pressed, push the DataViewScreen onto the screen stack.
            # This navigates to the detailed data view.
            self.app.push_screen("detail")  # "detail" is the name for DataViewScreen defined in the App.

class DataViewScreen(Screen):
    """The detailed data view screen of the TUI application.
    
    This screen shows a table of detailed task data. 
    It contains a Header, a DataTable listing all tasks, a Back button to return to the dashboard, and a Footer.
    """
    # Set the screen title (overrides the App title when this screen is active).
    TITLE = "Data View"
    # Define a screen-specific key binding: 'escape' to go back to the previous screen.
    BINDINGS = [("escape", "app.pop_screen", "Go Back")]
    
    def compose(self) -> ComposeResult:
        """Create and add widgets to the data view screen."""
        yield Header()  # Header displays the screen (app) title, here "Data View".
        # A DataTable widget to display the detailed task list.
        yield DataTable(id="tasks_table")
        # A Back button to navigate back to the dashboard screen.
        yield Button(label="Back to Dashboard", id="back_button", variant="primary")
        yield Footer()
    
    def on_mount(self) -> None:
        """Populate the task DataTable with data when this screen is mounted."""
        # Get the DataTable by its ID and add columns and rows for tasks.
        table = self.query_one(DataTable)
        # Define column headers for the task table (matching fields in TASKS tuples).
        table.add_columns("ID", "Task", "Status", "Due Date")
        # Add all tasks as rows in the table.
        for task_id, title, status, due_date in TASKS:
            table.add_row(str(task_id), title, status, due_date)
        # Set cursor movement to highlight the whole row for better readability.
        table.cursor_type = "row"
        # (Optional) We could add event handlers here, for example on_data_table_row_selected,
        # to handle user selection of a row.
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events on the data view screen."""
        if event.button.id == "back_button":
            # When the back button is pressed, pop this screen off the stack to return to the dashboard.
            self.app.pop_screen()

class DashboardApp(App):
    """Main application class for the Textual TUI.
    
    This class manages switching between the Dashboard and Data View screens.
    It defines global key bindings and starts with the dashboard screen.
    """
    # Register the screens with the application, associating names for navigation.
    SCREENS = {
        "dashboard": DashboardScreen,
        "detail": DataViewScreen,
    }
    # Global key bindings for the app:
    # 'd' to open the Data View screen, and 'q' to quit the application.
    BINDINGS = [
        ("d", "push_screen('detail')", "Open Data View"),
        ("q", "quit", "Quit"),
    ]
    
    def on_mount(self) -> None:
        """Event handler called when the application starts (after the terminal is ready).
        
        Use this to set up the initial view of the app.
        """
        # Make the dashboard screen the first view by pushing it onto the screen stack.
        self.push_screen("dashboard")
        # (If we did not push a screen here, the app would start with no content until a screen is pushed.)

# Run the application if the script is executed directly.
if __name__ == "__main__":
    app = DashboardApp()
    app.run()
