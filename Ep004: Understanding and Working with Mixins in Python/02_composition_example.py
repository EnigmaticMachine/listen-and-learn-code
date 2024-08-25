class Engine:
    """
    The Engine class represents a component of a larger object (a car).
    It has a method `start` that simulates starting the engine.

    In object-oriented programming (OOP), composition is a design principle
    where a class is composed of one or more objects of other classes, rather
    than inheriting from them. This allows us to build complex objects by combining
    simpler, independent components.

    Composition provides flexibility because it allows us to change the behavior
    of the composed object by changing its components, rather than modifying
    the entire class through inheritance.
    """

    def start(self):
        return "Engine starts"


class Car:
    """
    The Car class represents a complex object that is composed of simpler objects,
    such as the Engine class.

    Instead of inheriting from another class, the Car class uses composition
    to include an instance of the Engine class. This means the Car class has
    an Engine as one of its attributes, allowing it to use the Engine's functionality.

    Composition is often more flexible than inheritance because it lets us
    build complex objects by assembling them from smaller, independent parts.
    This modular approach allows us to easily swap out components (like replacing
    the engine) without changing the overall structure of the Car class.
    """

    def __init__(self, engine):
        # The Car class contains an instance of the Engine class as an attribute
        self.engine = engine

    def start(self):
        # The start method of Car delegates the action to the Engine's start method
        return self.engine.start()


# Creating an instance of Engine
engine = Engine()

# Creating an instance of Car with the Engine instance
car = Car(engine)

# Demonstrating the use of the start method in Car, which delegates to Engine
print(car.start())  # Output: Engine starts
