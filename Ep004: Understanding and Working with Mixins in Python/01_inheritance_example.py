class Animal:
    """
    The Animal class is a base class (or parent class) that represents a generic animal.
    It has a method `speak` that returns a generic sound.

    In object-oriented programming (OOP), the concept of inheritance allows us to define
    a new class that is based on an existing class. This new class, called the child class,
    inherits attributes and methods from the existing class, known as the parent class.

    In this example, Animal is the parent class. It provides a basic method, `speak`,
    that any animal might use. However, it's quite generic, returning a sound that
    could represent any animal.

    One of the key benefits of inheritance is code reuse. By defining common behavior
    (like making a sound) in a parent class, we can avoid repeating this behavior in
    every child class. Each specific animal class (like Dog or Cat) can inherit this
    common behavior and then modify it if needed.
    """

    def speak(self):
        return "Some generic animal sound"


class Dog(Animal):
    """
    The Dog class is a subclass (or child class) that inherits from the Animal class.
    It overrides the `speak` method to return a sound specific to dogs.

    Here, the Dog class inherits the speak method from the Animal class but overrides
    it to provide a dog-specific implementation. This is an example of how inheritance
    allows us to define specialized behavior for subclasses while still reusing the
    common functionality provided by the parent class.

    This demonstrates one of the limitations of inheritance: if we need to change
    the behavior of a subclass (like making the Dog class sound different from the
    generic Animal class), we must override the inherited method. In complex hierarchies,
    managing these overrides can become challenging.
    """

    def speak(self):
        return "Woof!"


class Cat(Animal):
    """
    The Cat class is another subclass of Animal.
    It also overrides the `speak` method to return a sound specific to cats.

    Similar to the Dog class, the Cat class overrides the inherited `speak` method
    from the Animal class to provide cat-specific behavior. This example further
    illustrates the use of inheritance to share common functionality (the idea that
    animals make sounds) while allowing subclasses to provide their own specific
    implementations.

    However, if we needed more flexibility in how these sounds were managed, or if
    we wanted to combine different behaviors in a more modular way, we might consider
    other object-oriented techniques like mixins or composition.
    """

    def speak(self):
        return "Meow!"


# Creating instances of each class
generic_animal = Animal()
dog = Dog()
cat = Cat()

# Demonstrating the use of the speak method in each class
print("Animal says:", generic_animal.speak())  # Output: Some generic animal sound
print("Dog says:", dog.speak())  # Output: Woof!
print("Cat says:", cat.speak())  # Output: Meow!
