# PROMPT
Model: Gemini 2.5 Pro

Prompt: write me boilerplate code app for python textual framework, provide hevy comment to explain what is going on in context of textual faramework

---
# **A Developer's Guide to Textual Boilerplate: Building Robust TUIs with Python**

## **1\. Introduction: Understanding Boilerplate in the Context of Textual**

In software development, "boilerplate" refers to sections of code that are repeated in multiple parts of a program or across different projects with little to no variation.1 This standardized, reusable code serves as a template, providing a foundational structure that can be adapted for specific needs.1 The concept is analogous to boilerplate text in press releases or legal documents, which offers a standard "about us" or terms section that can be slightly modified as needed.2 For software engineers, boilerplate code accelerates development by providing a ready-made starting point, ensuring consistency, and reducing the likelihood of errors that can arise from rewriting common structures from scratch.1

Textual, a Python framework developed by Textualize.io, enables the creation of sophisticated Text User Interfaces (TUIs) directly in the terminal.3 It leverages Rich, another Textualize library, for rich text and beautifully formatted terminal output.5 Textual applications are event-driven and can be styled using a simplified dialect of CSS, offering a development experience inspired by modern web development.3 Given Textual's structure, which involves defining an application class, composing widgets, handling events, and optionally applying styles, a well-crafted boilerplate can significantly streamline the process of initiating new TUI projects.

This document provides a comprehensive Textual boilerplate application, heavily commented to elucidate the framework's core concepts. It aims to serve as both a practical starting point for new Textual projects and an educational tool for understanding how Textual orchestrates TUI development.

## **2\. The Rationale for Using Boilerplate with Textual**

Employing a boilerplate for Textual application development offers several distinct advantages:

* **Accelerated Project Initiation:** A boilerplate provides a pre-built skeleton, allowing developers to bypass the initial setup of the main application class, common imports, CSS linkage, and basic UI structure. This means one can immediately focus on the unique logic and features of the intended application.1  
* **Ensuring Consistency:** For teams or individuals working on multiple Textual projects, a boilerplate enforces a consistent structure and coding style. This uniformity improves code readability, maintainability, and collaboration.1  
* **Facilitating Learning and Onboarding:** A well-commented boilerplate acts as an interactive tutorial. By examining and modifying a functional, minimal Textual application, developers new to the framework can grasp fundamental concepts such as widget composition, layout management, event handling, and styling more effectively.3  
* **Reducing Repetitive Code:** Common patterns, such as setting up a Header, Footer, or a main content area, can be included in the boilerplate, saving developers from rewriting this code for every new TUI.  
* **Best Practice Demonstration:** A good boilerplate can subtly guide developers towards best practices, such as separating CSS into its own file, using appropriate widget IDs for styling and querying, and structuring event handlers clearly.

In essence, a Textual boilerplate embodies a "standard template" 1 that streamlines development, promotes consistency, and aids in understanding the framework's architecture.

## **3\. Prerequisites and Setting Up Your Environment**

Before diving into the boilerplate code, ensure your development environment meets the following requirements:

* **Python Version:** Textual requires Python 3.8 or later.3 It is highly recommended to use a recent version of Python 3\.  
* **Virtual Environment:** As a best practice for any Python project, create and activate a virtual environment. This isolates project dependencies and keeps your global Python installation clean.3  
  Bash  
  python3 \-m venv.venv  
  source.venv/bin/activate  \# On Linux/macOS  
  \#.venv\\Scripts\\activate   \# On Windows

* **Textual Installation:** Install Textual and the development tools (textual-dev) using pip within your activated virtual environment 3:  
  Bash  
  pip install textual textual-dev  
  The textual package provides the core framework, while textual-dev includes tools like the live development console, which is invaluable for debugging and iterating on UI designs.3

Once these prerequisites are met, you are ready to create and run your first Textual application using the boilerplate provided.

## **4\. The Textual Boilerplate Application**

This section presents the boilerplate code, divided into a Python application file (my\_app.py) and a corresponding CSS file (boilerplate.tcss). Both files are heavily commented to explain each part in the context of the Textual framework.

### **4.1. File Structure**

It is recommended to organize your Textual application with at least two primary files:

* my\_app.py: Contains the Python logic for your application, including the App class definition, widget composition, and event handlers.  
* boilerplate.tcss (or a similar name): Contains the Textual CSS for styling your application's widgets and layout. Keeping CSS separate from Python code is a good practice for maintainability and allows for features like live CSS editing.6

### **4.2. Python Application Code (my\_app.py)**

Python

\# my\_app.py

\# Import necessary classes from the textual.app module.  
\# App is the base class for all Textual applications.  
\# ComposeResult is a type hint for the return value of the compose method,  
\# indicating it yields Widget instances.  
from textual.app import App, ComposeResult

\# Import widget classes from textual.widgets.  
\# Header: A standard widget for displaying a title at the top of the screen.  
\# Footer: A standard widget for displaying key bindings or status at the bottom.  
\# Static: A simple widget for displaying static or dynamic text content.  
\# Button: A widget that users can click to trigger actions.  
\# Input: A widget for single-line text input from the user.  
from textual.widgets import Header, Footer, Static, Button, Input

\# Import container widgets from textual.containers.  
\# VerticalScroll is a container that arranges its children vertically  
\# and provides scrolling if the content exceeds the available space.  
from textual.containers import VerticalScroll

\# Import event classes.  
\# Button.Pressed is the message sent when a Button is clicked.  
from textual.widgets.Button import Pressed as ButtonPressed

\# Define the main application class, inheriting from textual.app.App.  
\# The type hint \`App\[str\]\` indicates that this app, when it exits,  
\# might return a string value (e.g., via self.exit("some\_value")).  
\# If no specific return value is intended, App\[None\] can be used.  
class MyBoilerplateApp(App\[str\]):  
    """  
    A heavily commented boilerplate Textual application.  
    This class defines the structure and behavior of the TUI.  
    """

    \# TITLE sets the application title displayed in the Header widget (if used)  
    \# and potentially by the terminal window manager.  
    TITLE \= "Boilerplate Textual App"

    \# SUB\_TITLE provides an optional subtitle, also displayed in the Header.  
    SUB\_TITLE \= "A Starting Point for Your TUI"

    \# CSS\_PATH specifies the path to the external CSS file for styling the app.  
    \# Textual will load and apply styles from this file.  
    \# If None, or if the file doesn't exist, default styles apply.  
    CSS\_PATH \= "boilerplate.tcss"

    \# BINDINGS define global key bindings for the application.  
    \# Each tuple is (key\_description, action\_name, display\_text).  
    \# 'ctrl+q' will call the action\_quit method.  
    \# 'ctrl+c' is often a default exit binding as well.  
    BINDINGS \= \[  
        ("ctrl+q", "quit", "Quit App"),  
    \]

    \# The compose method is where the initial UI layout is defined.  
    \# It must be a generator function that yields Widget instances.  
    \# These widgets are added to the application's screen in the order they are yielded.  
    def compose(self) \-\> ComposeResult:  
        """  
        Create and arrange the initial child widgets for the application.  
        This method is called by Textual when the app starts.  
        """  
        \# Yield a Header widget. Textual automatically uses TITLE and SUB\_TITLE.  
        \# The Header is typically docked to the top of the screen (see CSS).  
        yield Header()

        \# Yield a VerticalScroll container. This widget will contain other widgets  
        \# and allow them to scroll vertically if their combined height exceeds  
        \# the container's height. It helps manage content that might not fit.  
        \# The \`id\` attribute is crucial for CSS styling and for querying the DOM.  
        \# Using an \`id\` allows specific targeting in CSS (e.g., \#main\_content)  
        \# and in Python code (e.g., self.query\_one("\#main\_content")).  
        with VerticalScroll(id\="main\_content"):  
            \# Yield a Static widget to display a welcome message.  
            \# This widget is placed inside the VerticalScroll container.  
            \# \`id\` allows styling and access.  
            yield Static("Welcome to your Textual Boilerplate\!", id\="welcome\_message")

            \# Yield an Input widget for user text entry.  
            \# \`placeholder\` provides hint text.  
            \# \`id\` is essential for retrieving its value later.  
            yield Input(placeholder="Enter some text here...", id\="my\_input")

            \# Yield a Button widget.  
            \# The first argument is the button's label.  
            \# \`variant="primary"\` is a common way to style a primary action button (see CSS).  
            \# \`id\` helps in identifying the button if multiple buttons exist or for specific styling.  
            yield Button("Submit", variant="primary", id\="submit\_button")

            \# Yield another Static widget, initially empty.  
            \# This will be used to display output based on user interaction.  
            \# \`id\` allows us to find and update this widget.  
            yield Static(id\="output\_area")

        \# Yield a Footer widget. Textual automatically populates this with BINDINGS.  
        \# The Footer is typically docked to the bottom of the screen (see CSS).  
        yield Footer()

    \# Event handler for when the "Submit" button is pressed.  
    \# Textual's event system automatically calls methods named \`on\_\<widget\_type\>\_\<event\_name\>\`  
    \# or, more specifically for buttons with IDs, \`on\_button\_pressed\` can be decorated  
    \# with \`@on(Button.Pressed, "\#submit\_button")\`.  
    \# This simpler form \`on\_button\_pressed\` handles any Button.Pressed event.  
    \# The \`async\` keyword indicates this is an asynchronous method. Textual's event  
    \# handlers can be async, allowing for non-blocking operations if needed.  
    \# Textual is built on Python's asyncio.  
    async def on\_button\_pressed(self, event: ButtonPressed) \-\> None:  
        """  
        Handles the Button.Pressed event, specifically for our submit button.  
        This method is called when any button in the app is pressed.  
        """  
        \# Check if the pressed button is the one we're interested in by its ID.  
        \# The \`event.button\` attribute gives access to the Button instance that was pressed.  
        \# This check is important if you have multiple buttons and need different actions.  
        if event.button.id \== "submit\_button":  
            \# Query the DOM to get the Input widget using its ID.  
            \# \`self.query\_one\` expects to find exactly one widget matching the selector.  
            \# The second argument, \`Input\`, specifies the expected type for type checking.  
            input\_widget \= self.query\_one("\#my\_input", Input)

            \# Query the DOM to get the Static widget for output.  
            output\_area \= self.query\_one("\#output\_area", Static)

            \# Get the current value from the Input widget.  
            user\_text \= input\_widget.value

            \# Update the content of the 'output\_area' Static widget.  
            \# The \`update\` method re-renders the widget with new content.  
            \# f-strings are used for easy string formatting.  
            output\_area.update(f"You entered: '{user\_text}' and clicked the button\!")

            \# Clear the input field after submission for better UX.  
            input\_widget.value \= ""

            \# Optionally, play a system bell sound as feedback.  
            \# \`self.bell()\` is a built-in App method.  
            self.bell()

    \# Action methods are prefixed with \`action\_\`.  
    \# They are called when a binding is invoked (e.g., 'ctrl+q' calls 'action\_quit').  
    def action\_quit(self) \-\> None:  
        """  
        Called when the 'quit' action is triggered (e.g., by a binding).  
        This method exits the application.  
        """  
        self.exit("Application closed by user.")

\# This is the standard Python entry point.  
\# The code inside this block runs only when the script is executed directly  
\# (not when imported as a module).  
if \_\_name\_\_ \== "\_\_main\_\_":  
    \# Create an instance of our Textual application.  
    app \= MyBoilerplateApp()  
    \# Call the run() method to start the application.  
    \# This takes over the terminal, sets up the UI, and starts the event loop.  
    \# The optional \`log\_path\` argument can be used to redirect Textual's internal  
    \# logging to a file for debugging.  
    app.run()

### **4.3. Textual CSS File (boilerplate.tcss)**

CSS

/\* boilerplate.tcss \*/

/\* Screen is the root container for the application. \*/  
/\* Styles applied here affect the overall app window. \*/  
Screen {  
    /\* \`layout: vertical\` arranges child widgets (Header, VerticalScroll, Footer)  
       from top to bottom. This is often the default for Screen. \*/  
    layout: vertical;  
    /\* \`overflow: hidden hidden;\` can prevent unexpected scrollbars at the screen level.  
       Typically, scrolling is managed by inner containers like VerticalScroll. \*/  
    overflow: hidden hidden;  
    /\* \`background: $surface;\` uses a Textual system color for the background.  
       System colors adapt to light/dark mode. \*/  
    background: $surface;  
}

/\* Style the Header widget. \*/  
Header {  
    /\* \`dock: top;\` fixes the Header to the top of its parent (the Screen).  
       Docked widgets are laid out first and take up space along the edge. \*/  
    dock: top;  
    /\* \`background: $primary-background;\` sets a distinct background for the header. \*/  
    background: $primary-background;  
    /\* \`color: $text;\` sets the text color. \*/  
    color: $text;  
}

/\* Style the Footer widget. \*/  
Footer {  
    /\* \`dock: bottom;\` fixes the Footer to the bottom of its parent (the Screen). \*/  
    dock: bottom;  
    /\* \`background: $primary-background-darken-2;\` uses a darker shade for the footer. \*/  
    background: $primary-background-darken-2;  
    color: $text-muted; /\* Muted text color for less emphasis. \*/  
}

/\* Style the VerticalScroll container with id 'main\_content'. \*/  
/\* The '\#' prefix targets a widget by its ID. \*/  
\#main\_content {  
    /\* \`padding: 1 2;\` adds padding around the content within this container.  
       (1 row top/bottom, 2 columns left/right). \*/  
    padding: 1 2;  
    /\* \`width: 100%;\` ensures it takes the full available width. \*/  
    width: 100%;  
    /\* \`height: 1fr;\` makes this container take up 1 fraction of the remaining  
       vertical space after Header and Footer are docked. This is key for  
       making the content area fill the available space. \*/  
    height: 1fr;  
    /\* \`background: $panel;\` sets a background for the content area. \*/  
    background: $panel;  
}

/\* Style the Static widget with id 'welcome\_message'. \*/  
\#welcome\_message {  
    /\* \`width: 100%;\` ensures full width. \*/  
    width: 100%;  
    /\* \`text-align: center;\` centers the text within the widget. \*/  
    text-align: center;  
    /\* \`margin-bottom: 1;\` adds some space below this widget. \*/  
    margin-bottom: 1;  
    /\* \`text-style: bold;\` makes the text bold. \*/  
    text-style: bold;  
}

/\* Style all Input widgets. \*/  
Input {  
    /\* \`width: 100%;\` makes input fields take the full available width. \*/  
    width: 100%;  
    /\* \`margin-bottom: 1;\` adds space below each input field. \*/  
    margin-bottom: 1;  
    /\* \`border: round $primary;\` adds a rounded border with the primary color. \*/  
    border: round $primary;  
}

/\* Style all Button widgets. \*/  
Button {  
    /\* \`width: 100%;\` makes buttons span the full width of their container. \*/  
    width: 100%;  
    /\* \`margin: 1 0;\` adds vertical margin (1 row top/bottom, 0 columns left/right). \*/  
    margin: 1 0;  
}

/\* Style Button widgets with the 'primary' variant. \*/  
/\* This targets buttons like \<Button variant="primary"\>. \*/  
Button.-primary {  
    /\* \`background: $success;\` uses a system color typically for success/confirmation. \*/  
    background: $success;  
    /\* \`color: $text-primary;\` ensures good contrast for text on this background. \*/  
    color: $text-primary;  
}

/\* Style the Static widget with id 'output\_area'. \*/  
\#output\_area {  
    /\* \`width: 100%;\` full width. \*/  
    width: 100%;  
    /\* \`height: auto;\` allows the widget to grow in height based on its content. \*/  
    height: auto;  
    /\* \`min-height: 3;\` ensures it has at least some visible height even when empty. \*/  
    min-height: 3;  
    /\* \`padding: 1;\` adds padding inside the output area. \*/  
    padding: 1;  
    /\* \`margin-top: 1;\` adds space above it. \*/  
    margin-top: 1;  
    /\* \`border: round $accent;\` adds a border to make it distinct. \*/  
    border: round $accent;  
    /\* \`background: $primary-background-lighten-2;\` a slightly lighter background. \*/  
    background: $primary-background-lighten-2;  
}

The careful use of IDs (e.g., \#my\_input, \#submit\_button) in the Python code is fundamental. These IDs serve as hooks for Textual's CSS engine to apply specific styles and for the Python logic to query and interact with specific widgets. For instance, self.query\_one("\#my\_input", Input) relies on the Input widget having id="my\_input". This creates a direct link between the application's structure defined in Python and its presentation defined in CSS, mirroring the way IDs and classes connect HTML structure with CSS rules in web development. This mechanism is central to how Textual enables developers to build complex and stylable TUIs.

Furthermore, the event handler async def on\_button\_pressed demonstrates Textual's integration with Python's asyncio library.7 By defining event handlers as asynchronous co-routines, Textual applications can perform operations that might otherwise block the user interface (like network requests or file I/O) without freezing the TUI. While this boilerplate's handler is simple, the async nature is a provision for more complex, real-world scenarios, ensuring UI responsiveness.

## **5\. Dissecting the Boilerplate: Key Textual Concepts Explained**

The boilerplate application, though simple, demonstrates several core concepts of the Textual framework. Understanding these concepts is key to building more complex TUIs.

### **5.1. Working with Widgets: The Building Blocks of Your TUI**

Widgets are the fundamental UI elements in a Textual application. Each widget is a Python class, typically inheriting from textual.widget.Widget or one of its specialized subclasses.6 Instances of these widget classes are created and yielded in the compose method of an App or a parent widget to build the UI hierarchy.6 Each widget is responsible for managing a rectangular area of the screen, rendering its content, and potentially responding to user events like mouse clicks or key presses.3

The boilerplate uses several built-in Textual widgets:

* **Header and Footer**: These are standard widgets for displaying application titles/subtitles and key bindings, respectively.8 They often utilize docking to position themselves at the top or bottom of the screen.  
* **Static**: Used for displaying blocks of text that can be either fixed or updated dynamically during runtime (e.g., the welcome\_message and output\_area in the boilerplate).3 The .update() method is commonly used to change its content.  
* **Input**: A control for capturing single-line text input from the user.3 Its value attribute holds the entered text.  
* **Button**: Allows users to trigger actions by clicking it.3 It emits a Button.Pressed message when clicked. Buttons can also have variant attributes (e.g., variant="primary") for easy styling via CSS.  
* **VerticalScroll**: This is a container widget that arranges its children vertically and automatically provides scrollbars if the content's height exceeds the available space.9

The following table summarizes the widgets used in the boilerplate and the Textual concepts they illustrate:

| Widget Class | Purpose in Boilerplate | Key Textual Concept Illustrated |
| :---- | :---- | :---- |
| Header | Displays app title and subtitle at the top. | Standard UI element, automatic styling, title integration. |
| Footer | Displays key bindings at the bottom. | Standard UI element, bindings integration, interactivity. |
| VerticalScroll | Contains the main interactive elements, allows scrolling. | Layout container, managing overflow, child widget composition. |
| Static | Displays welcome message and dynamic output from user input. | Basic content display, dynamic content updates via .update(). |
| Input | Allows user to enter text. | Capturing user input, value property, placeholder text. |
| Button | Triggers an action when clicked to process input. | Event handling (Button.Pressed), variants for styling, user action. |

This structured approach to UI construction, where widgets are composed and managed, forms the basis of all Textual applications. The framework's design, where each widget can have its own style settings and event responses, allows for modular and maintainable TUI code.3

### **5.2. Layout and Containers: Arranging Widgets on Screen**

Textual provides a flexible layout system to arrange widgets within an application or container. Layouts can be defined via CSS properties or by using specific container widgets.9 The boilerplate primarily demonstrates a vertical layout, which is the default for the Screen object and explicitly for the VerticalScroll container.

* **Vertical Layout**: Arranges child widgets from top to bottom. In the compose method, the order of yield statements determines this top-to-bottom arrangement.9  
* **Docking**: Widgets like Header and Footer are often "docked." In the boilerplate's CSS, dock: top; for the Header and dock: bottom; for the Footer fix them to the respective edges of the screen.4 Docked widgets are laid out first, and the remaining space is then available for other content.  
* **Fractional Units (fr)**: The CSS height: 1fr; for the \#main\_content VerticalScroll container is significant. It tells this container to take up one fraction of the available vertical space remaining after the Header and Footer have been docked. This allows the main content area to dynamically resize with the terminal window.  
* **Container Widgets**: VerticalScroll is an example of a container widget. Textual also offers others like HorizontalScroll, Vertical, Horizontal, and Grid for more complex layout scenarios.3 These containers can be nested to create intricate UI structures.

The interaction between Python's compose method and Textual's CSS for layout control is a powerful feature. While compose defines the hierarchy and initial order, CSS provides fine-grained control over sizing, positioning, and responsiveness.

### **5.3. Event-Driven Programming: Responding to User Interactions**

Textual applications are event-driven.3 This means the application waits for events (like key presses, mouse clicks, or internal state changes) and then reacts to them by executing specific event handler methods.7

* **Event Handler Methods**: In Textual, event handlers are typically methods within an App or Widget class. A common naming convention is on\_\<EventName\> (e.g., on\_mount, on\_key) or, for widget-specific messages, on\_\<WidgetType\>\_\<MessageName\> (e.g., on\_input\_changed).10 The boilerplate uses async def on\_button\_pressed(self, event: ButtonPressed).  
* **The event Object**: Event handler methods receive an event object as an argument (e.g., event: ButtonPressed). This object contains information about the event, such as the source widget (event.button in the case of ButtonPressed).10  
* **Message Queue**: Every App and Widget has a message queue. When an event occurs, Textual creates a message and posts it to the relevant widget's queue. An asyncio task then processes these messages one by one, calling the appropriate handler.10 This ensures that events are handled sequentially and don't get lost, even if the application is briefly busy.  
* **Actions and Bindings**: The BINDINGS class variable in the App defines global key bindings. Pressing ctrl+q triggers the quit action, which Textual maps to the action\_quit method. This provides a way to define application-level shortcuts.

The event model, coupled with asyncio, allows for responsive TUIs that can handle user input and background tasks efficiently. The ability to query the widget tree (e.g., self.query\_one("\#my\_input", Input)) within an event handler to access the state of other widgets is a common pattern for building interactive applications. This DOM-like querying capability, using CSS selectors, provides a flexible way to decouple event sources from the widgets they affect.

### **5.4. Styling with Textual CSS: Customizing the Look and Feel**

Textual uses a dialect of CSS for styling applications, offering a familiar way to control the appearance of TUIs.3 This CSS can be defined in an external file (as done in the boilerplate via CSS\_PATH \= "boilerplate.tcss") or embedded directly in Python code for custom widgets.6

* **External CSS File**: Linking an external CSS file is generally recommended for applications as it separates presentation from logic and enables features like live CSS editing with textual-dev tools.6  
* **Selectors**: Textual CSS uses selectors similar to web CSS.  
  * Type selectors: Button (targets all Button widgets).  
  * ID selectors: \#my\_input (targets the widget with id="my\_input").  
  * Class selectors: .-primary (targets widgets with class="primary", often used for variants like Button(variant="primary")).  
* **Properties**: The CSS file (boilerplate.tcss) demonstrates various properties:  
  * layout: Defines how child widgets are arranged (e.g., vertical, horizontal).4  
  * dock: Fixes a widget to an edge of its container (e.g., top, bottom).4  
  * padding, margin: Control spacing around and inside widgets.  
  * width, height: Define widget dimensions. fr units are particularly useful for flexible layouts.  
  * background, color: Set background and text colors. Textual supports system colors (e.g., $primary, $surface) that adapt to terminal themes.  
  * border: Defines widget borders.  
  * text-align, text-style: Control text alignment and style (e.g., bold).  
* **Simplified Dialect**: While powerful, Textual's CSS is a simplified version compared to web CSS, making it easier to learn and use effectively for TUI design.4

A notable aspect of Textual's CSS system is that CSS defined within a custom widget's DEFAULT\_CSS is scoped by default.6 This means that styles intended for a specific custom widget will not unintentionally affect other parts of the application. This encapsulation is crucial for building modular and reusable widgets, as it prevents style conflicts in larger applications—a lesson learned from the complexities of global CSS in web development. While app-level CSS (like boilerplate.tcss) can apply more broadly, the scoping for widget-specific default styles promotes better organization.

## **6\. Running, Testing, and Expanding Your Application**

With the boilerplate code and its underlying concepts explained, the next step is to run it and explore how to enhance it.

### **6.1. How to Run the Boilerplate Application**

To run the boilerplate application, follow these steps:

1. **Save the Files**:  
   * Save the Python code from section 4.2 into a file named my\_app.py.  
   * Save the CSS code from section 4.3 into a file named boilerplate.tcss in the **same directory** as my\_app.py.  
2. **Open Your Terminal**: Navigate to the directory where you saved these two files.  
3. **Activate Virtual Environment**: If you haven't already, activate the Python virtual environment where you installed Textual:  
   Bash  
   source.venv/bin/activate  \# On Linux/macOS  
   \#.venv\\Scripts\\activate   \# On Windows

4. **Run the Application**: Execute the Python script:  
   Bash  
   python my\_app.py  
   The Textual application should launch in your terminal, displaying the Header, Input field, Button, and Footer as defined. You can type text into the input field and click the "Submit" button (or press Enter if the button is focused) to see the output\_area update. Press Ctrl+Q to quit the application.

### **6.2. Leveraging textual-dev Tools for Enhanced Development**

Textual provides development tools via the textual-dev package, which includes a command-line tool also named textual.3 One of its most powerful features is the development console, which supports live editing of CSS and inspection of the widget DOM.

To run your application with the development tools, use:

Bash

textual run \--dev my\_app.py

This will launch your application. You can then press F12 (or as indicated by the tool) to open the Textual console. Here, you can:

* **Inspect Widgets**: View the widget tree, their properties, and current styles.  
* **Live Edit CSS**: Modify the boilerplate.tcss file, and the changes will be reflected in the running application almost instantly. This dramatically speeds up UI styling and iteration.  
* **Debug**: Access logs and other debugging information.

The availability of such tools underscores an important aspect of TUI development with Textual: it's designed to be an iterative process. Developers are encouraged to experiment and refine their UIs, and the textual-dev tools facilitate this rapid feedback loop, making the development experience more efficient and enjoyable.

### **6.3. Ideas for Extending the Boilerplate**

The provided boilerplate is a starting point. Here are some ideas for expanding upon it to explore more of Textual's capabilities:

* **Add More Widgets**: Explore other widgets from textual.widgets and textual.containers.8 For example:  
  * Checkbox or RadioButton for selection options.  
  * DataTable for displaying tabular data.  
  * Markdown for rendering Markdown content.  
  * LoadingIndicator for showing activity during long operations.  
* **Implement Complex Layouts**: Use Horizontal, Vertical, or Grid containers to create more sophisticated screen arrangements.3 Experiment with nesting these containers.  
* **Advanced Event Handling**:  
  * Handle other events like Input.Changed (to react as the user types) or Input.Submitted (when Enter is pressed in an Input field).  
  * Use the @on decorator for more targeted event handling, especially if you have multiple instances of the same widget type.10  
* **State Management**: For more complex applications, consider how to manage application state beyond simple widget attributes. This might involve creating dedicated state objects or using reactive variables if integrating with other patterns.  
* **Create Custom Widgets**: Subclass textual.widget.Widget to build your own reusable UI components.6 This is a powerful feature for encapsulating complex UI logic and appearance. Custom widgets can have their own compose method, DEFAULT\_CSS, and event handlers.  
* **Multiple Screens**: Explore Textual's screen management to create multi-screen applications (e.g., a settings screen, a main view screen).  
* **Asynchronous Operations**: Modify an event handler to perform a genuinely asynchronous task (e.g., await asyncio.sleep(2) before updating the output) to observe Textual's non-blocking behavior.

The ability to create custom widgets and the rich set of built-in components signify that Textual is an extensible framework.6 It provides robust foundations but is designed for developers to build upon and adapt to a wide array of TUI application needs. This boilerplate serves as the initial step in that journey.

## **7\. Conclusion: Your Next Steps with Textual**

This document has provided a heavily commented boilerplate Textual application, designed to serve as a practical launchpad for developing Text User Interfaces in Python. By dissecting its components—the App class structure, widget composition, layout management, event handling, and CSS styling—developers can gain a foundational understanding of Textual's core mechanics. The boilerplate is not just a template; it's an educational tool intended to accelerate learning and kickstart custom TUI projects.

To continue your journey with Textual, consider the following pathways:

* **Official Documentation**: The official Textual documentation is an invaluable resource. It contains detailed guides, API references, and numerous examples that cover the framework in depth.4  
* **Community Engagement**: The Textualize community (often found on platforms like Discord or GitHub discussions) can provide support, inspiration, and a place to share your projects and learn from others. Exploring lists of Textual projects, such as "awesome-textualize-projects," can also offer insights into what's possible with the framework.5  
* **Experimentation**: The best way to learn is by doing. Use the boilerplate as a base to experiment with different widgets, layouts, and event handling patterns. The textual-dev tools are your companion in this iterative process.

The investment in robust documentation and the fostering of a community are often indicative of a healthy and evolving framework. Textual, with its modern approach to TUI development, offers a powerful and enjoyable way to build sophisticated command-line applications. This boilerplate aims to make your initial steps into this ecosystem both productive and insightful.

#### **Works cited**

1. Boilerplate Language, Uses, History, Examples, Pros & Cons \- Investopedia, accessed May 16, 2025, [https://www.investopedia.com/terms/b/boilerplate.asp](https://www.investopedia.com/terms/b/boilerplate.asp)  
2. What is a Boilerplate? Examples and Tips for Writing \- Mailchimp, accessed May 16, 2025, [https://mailchimp.com/resources/boilerplate/](https://mailchimp.com/resources/boilerplate/)  
3. Python Textual: Build Beautiful UIs in the Terminal – Real Python, accessed May 16, 2025, [https://realpython.com/python-textual/](https://realpython.com/python-textual/)  
4. Crash Course On Using Textual \- Fedora Magazine, accessed May 16, 2025, [https://fedoramagazine.org/crash-course-on-using-textual/](https://fedoramagazine.org/crash-course-on-using-textual/)  
5. awesome-textualize-projects \- GitHub Pages, accessed May 16, 2025, [https://oleksis.github.io/awesome-textualize-projects/](https://oleksis.github.io/awesome-textualize-projects/)  
6. Widgets \- Textual, accessed May 16, 2025, [https://textual.textualize.io/guide/widgets/](https://textual.textualize.io/guide/widgets/)  
7. App Basics \- Textual, accessed May 16, 2025, [https://textual.textualize.io/guide/app/](https://textual.textualize.io/guide/app/)  
8. Widgets \- Textual, accessed May 16, 2025, [https://textual.textualize.io/widget\_gallery/](https://textual.textualize.io/widget_gallery/)  
9. Layout \- Textual, accessed May 16, 2025, [https://textual.textualize.io/guide/layout/](https://textual.textualize.io/guide/layout/)  
10. Events and Messages \- Textual, accessed May 16, 2025, [https://textual.textualize.io/guide/events/](https://textual.textualize.io/guide/events/)  
11. Textual tutorial – build a TODO app in Python | mathspp, accessed May 16, 2025, [https://mathspp.com/blog/textual-tutorial-build-a-todo-app-in-python](https://mathspp.com/blog/textual-tutorial-build-a-todo-app-in-python)