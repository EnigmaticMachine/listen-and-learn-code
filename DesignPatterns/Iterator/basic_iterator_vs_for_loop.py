# Simple Function with a `for` Loop
# ---------------------------------
# This function takes a collection (like a list) and processes each item using a `for` loop.
# It prints each item in the collection as it iterates through it.


def process_collection(collection):
    # The `for` loop automatically handles the iteration over the collection.
    for item in collection:
        print(f"Processing item: {item}")


# Example usage of the simple function:
my_list = [1, 2, 3, 4]  # A sample list to process
process_collection(my_list)  # Call the function to process the list


# Custom Iterator Class
# ---------------------
# This is a more advanced approach using the Iterator pattern.
# We define a custom class that can be used as an iterator. This class will handle the iteration
# logic internally, giving us more control and flexibility.


class MyIterator:
    def __init__(self, collection):
        # Initialize the iterator with the collection and set the starting index to 0.
        self.collection = collection
        self.index = 0

    def __iter__(self):
        # The `__iter__` method is called when the iteration is started.
        # It returns the iterator object itself, making the object iterable.
        return self

    def __next__(self):
        # The `__next__` method is called each time the loop asks for the next item.
        # It returns the next item in the collection and increments the index.
        # If the index exceeds the length of the collection, it raises the StopIteration exception.
        if self.index < len(self.collection):
            item = self.collection[self.index]
            self.index += 1  # Move to the next index
            return item
        else:
            # When there are no more items to return, raise StopIteration to signal the end of the iteration.
            raise StopIteration


# Example usage of the custom iterator class:
my_list = [1, 2, 3, 4]  # A sample list to process
my_iterator = MyIterator(my_list)  # Create an instance of the iterator class

# Using the custom iterator in a `for` loop:
# The `for` loop will internally call the `__iter__` method first, and then repeatedly call `__next__`.
for item in my_iterator:
    print(f"Processing item: {item}")


# Explanation of Key Differences:
# --------------------------------
# 1. Simple Function with `for` loop:
#    - The iteration is directly controlled by the `for` loop within the function.
#    - This approach is straightforward and effective for simple tasks.
#    - However, it lacks flexibility if the iteration logic needs to be more complex or reused.

# 2. Custom Iterator Class:
#    - The iteration logic is encapsulated within the `MyIterator` class.
#    - The class handles the process of moving through the collection, making the object itself an iterator.
#    - This approach provides more control and allows the iteration process to be reused and customized.
#    - The `__iter__` method ensures the object can be used in a `for` loop, while `__next__` handles the retrieval of each item.
#    - The `StopIteration` exception is used to signal when the iteration is complete, which the `for` loop automatically handles.

# Conclusion:
# ------------
# - Using a simple `for` loop inside a function is easy and works well for basic iteration tasks.
# - Implementing the iterator pattern with a custom class offers more control and modularity, especially useful in complex scenarios.
# - The custom iterator approach allows your class to manage iteration internally, making your code more reusable and maintainable.
