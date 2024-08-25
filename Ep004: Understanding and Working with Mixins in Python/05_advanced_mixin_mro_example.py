class LogMixin:
    """
    The LogMixin class provides logging functionality that can be added to any class.

    This mixin defines a method called `log`, which logs a message. This mixin can
    be included in other classes to add logging capabilities. The method resolution
    order (MRO) determines how Python resolves which method to call when multiple
    mixins or parent classes are involved.
    """

    def log(self, message):
        print(f"Log: {message}")


class SaveMixin:
    """
    The SaveMixin class provides saving functionality.

    This mixin defines a method called `save`, which simulates saving data.
    Like LogMixin, SaveMixin can be combined with other classes to provide additional
    functionality. In classes that inherit from multiple mixins, the MRO is crucial
    for determining which method is executed when a method name overlaps across mixins.
    """

    def save(self, data):
        print(f"Saving data: {data}")


class BackupMixin(SaveMixin):
    """
    The BackupMixin class inherits from SaveMixin and overrides the `save` method.

    This mixin adds backup functionality by overriding the `save` method from SaveMixin.
    It first calls the original `save` method (using super()) and then logs a backup action.
    This is an example of method overriding in mixins and how the MRO ensures that
    the correct `save` method is called.
    """

    def save(self, data):
        super().save(data)  # Call the save method from SaveMixin
        print(f"Backing up data: {data}")


class DataHandler(LogMixin, BackupMixin):
    """
    The DataHandler class combines LogMixin and BackupMixin.

    By inheriting from multiple mixins, DataHandler gains both logging and saving
    functionality. The MRO is critical in determining the order in which methods are
    resolved and executed. In this case, BackupMixin comes before SaveMixin in the
    inheritance chain, so its `save` method is executed first.

    The MRO ensures that the methods are resolved in a specific order, allowing us
    to predict the behavior of our class when multiple mixins are involved.
    """

    def process_and_save(self, data):
        self.log(f"Processing data: {data}")
        self.save(data)


# Creating an instance of DataHandler
data_handler = DataHandler()

# Demonstrating the use of process_and_save, which involves both logging and saving
data_handler.process_and_save("Important data")
# Output:
# Log: Processing data: Important data
# Saving data: Important data
# Backing up data: Important data


# --- Method Resolution Order (MRO) Explained ---

"""
In this example, the DataHandler class inherits from both LogMixin and BackupMixin.
When the `process_and_save` method is called, it first logs the data processing action
using the `log` method from LogMixin.

Then, it calls the `save` method, which is provided by BackupMixin. Since BackupMixin
inherits from SaveMixin and overrides its `save` method, the MRO ensures that the
overridden method in BackupMixin is executed first.

Here’s the method resolution order for DataHandler:
1. DataHandler
2. BackupMixin
3. SaveMixin
4. LogMixin
5. object (the root of all classes in Python)

This means that when DataHandler calls the `save` method, Python first looks in BackupMixin,
finds the overridden method, and executes it. If BackupMixin didn't have a `save` method,
Python would continue searching in SaveMixin, and so on.

This order ensures that the correct method is called, even when multiple mixins or parent
classes are involved, allowing for predictable and manageable behavior in complex class hierarchies.
"""
