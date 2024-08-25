# --- Key Differences Explained ---

"""
1. Purpose:
   - Regular Inheritance:
     Regular inheritance is used when creating a more specialized version of a class.
     It represents an "is-a" relationship, such as Dog "is-a" Animal. This means the
     subclass should conceptually be a type of the parent class, inheriting and possibly
     overriding or extending its behavior.

   - Mixin:
     A mixin is used to add specific, reusable functionality to a class without
     implying that the class "is" a type of the mixin. For example, the FileHandler
     and NetworkHandler classes are not types of LogMixin, but they "have" the ability
     to log because of the LogMixin. This represents a "has-a" or "can-do" relationship.

2. Design and Structure:
   - Regular Inheritance:
     The subclass typically extends or modifies the parent class's behavior,
     inheriting all of its attributes and methods. This can lead to deep inheritance
     hierarchies if not carefully managed.

   - Mixin:
     Mixins are small, focused classes that provide specific functionality.
     A class can inherit from multiple mixins to gain various capabilities, promoting
     modularity and code reuse without deepening the inheritance hierarchy.

3. Use Case:
   - Regular Inheritance:
     Use regular inheritance when you need to define a specialized version of a class,
     where the subclass should conceptually be a type of the parent class (e.g.,
     Dog is a type of Animal).

   - Mixin:
     Use mixins when you want to add specific, modular functionality across different
     classes that do not share a common ancestor. Mixins allow you to avoid code
     duplication and keep your classes focused on their primary responsibilities
     while still gaining additional features.
"""


class Animal:
    """
    The Animal class is a base class representing a generic animal.
    It provides common functionality that all animals might share.

    In object-oriented programming, regular inheritance is used to create a
    specialized version of an existing class. The specialized class (child class)
    inherits attributes and methods from the existing class (parent class).
    """

    def move(self):
        return "Moving around"


class Dog(Animal):
    """
    In this case, Dog "is-a" specific type of Animal. The Dog class can override
    methods from the Animal class to specialize behavior (e.g., how a dog moves).

    This is an example of regular inheritance where the subclass is a more
    specialized version of the parent class.
    """

    def move(self):
        return "Running on four legs"


# Demonstrating regular inheritance
generic_animal = Animal()
dog = Dog()

# Calling the move method on both the generic animal and the dog
print(f"Animal moves: {generic_animal.move()}")  # Output: Moving around
print(f"Dog moves: {dog.move()}")  # Output: Running on four legs


# --- Mixin Example ---


class LogMixin:
    """
    The LogMixin class provides logging functionality that can be added to any class.

    The LogMixin class is small and focused on a single responsibility: logging messages.
    By using this mixin, other classes can gain logging capabilities without needing
    to implement logging themselves.
    """

    def log(self, message):
        # A simple logging method that prints a message with a "Log:" prefix
        print(f"Log: {message}")


class FileHandler(LogMixin):
    """
    The FileHandler class represents a class that handles file operations.

    By inheriting from LogMixin, FileHandler gains the ability to log actions.
    This is an example of how mixins can be used to add specific functionality
    (like logging) to different classes without creating complex inheritance hierarchies.
    """

    def open_file(self, filename):
        # Use the log method from LogMixin to log the action of opening a file
        self.log(f"Opening file: {filename}")
        print(f"File {filename} opened successfully")


class NetworkHandler(LogMixin):
    """
    The NetworkHandler class represents a class that handles network operations.

    Like FileHandler, NetworkHandler also inherits from LogMixin to gain logging capabilities.
    This demonstrates the reusability of mixins, allowing multiple unrelated classes
    to share the same functionality (logging in this case) without duplicating code.
    """

    def connect(self, address):
        # Use the log method from LogMixin to log the action of connecting to an address
        self.log(f"Connecting to {address}")
        print(f"Connected to {address}")


# Demonstrating mixin usage with both FileHandler and NetworkHandler

# Creating an instance of FileHandler
file_handler = FileHandler()
file_handler.open_file("example.txt")
# Output:
# Log: Opening file: example.txt
# File example.txt opened successfully

# Creating an instance of NetworkHandler
network_handler = NetworkHandler()
network_handler.connect("192.168.1.1")
# Output:
# Log: Connecting to 192.168.1.1
# Connected to 192.168.1.1
