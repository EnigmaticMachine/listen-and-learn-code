class LogMixin:
    """
    The LogMixin class is a mixin that provides logging functionality.

    A mixin is a type of class that is designed to be used in combination with other classes
    to add specific functionality. Unlike a regular parent class, a mixin is not intended to
    stand on its own. Instead, it provides a set of methods or attributes that can be mixed
    into other classes.

    Mixins are typically small and focused on doing one thing well. They allow us to add
    reusable functionality across different classes without creating deep inheritance hierarchies.

    In this example, LogMixin provides a simple logging method that can be added to any class
    that needs logging capability.
    """

    def log(self, message):
        # A simple logging method that prints a message with a "Log:" prefix
        print(f"Log: {message}")


class FileHandler(LogMixin):
    """
    The FileHandler class represents a class that handles file operations.

    By inheriting from LogMixin, FileHandler gains logging functionality without
    needing to implement it directly. This demonstrates how mixins can be used
    to add modular and reusable functionality to different classes.

    The primary responsibility of FileHandler is to handle files, but by mixing in
    LogMixin, it also gains the ability to log actions related to file handling.
    """

    def open_file(self, filename):
        # Use the log method from LogMixin to log the action of opening a file
        self.log(f"Opening file: {filename}")
        # Placeholder for actual file opening logic
        # Here, we just simulate opening a file with a print statement
        print(f"File {filename} opened successfully")


# Creating an instance of FileHandler
file_handler = FileHandler()

# Demonstrating the use of the open_file method, which uses the log method from LogMixin
file_handler.open_file("example.txt")
# Output:
# Log: Opening file: example.txt
# File example.txt opened successfully
