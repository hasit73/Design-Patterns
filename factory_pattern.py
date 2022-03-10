"""
Factory Pattern:
Factory pattern is one of the most used design patterns. This type of design pattern comes
under creational pattern as this pattern provides one of the best ways to create an object.

Create single Factory class to generate the objects of various classes.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """ Shape is base class of all different shape
        It doesn't have any attributes
    """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


class Circle(Shape):
    """ Circle is child class of Shape
        It Contains different properties of circle shape
    """

    def __init__(self):
        self.shape_name = "circle"

    def get_name(self):
        return f"C-{self.shape_name}"


class Square(Shape):
    """ Square is child class of Shape
        It Contains different properties of square shape
    """

    def __init__(self):
        self.shape_name = "square"

    def get_name(self):
        return f"S-{self.shape_name}"


class Triangle(Shape):
    """ Triangle is child class of Shape
        It Contains different properties of triangle shape
    """

    def __init__(self):
        self.shape_name = "triangle"

    def get_name(self):
        return f"T-{self.shape_name}"


class ShapeFactory:
    """ Produce different type of Shapes """
    def get_shape(self, shape_type):
        """
        Get given type of shape
        """
        if shape_type == "circle":
            return Circle()

        elif shape_type == "triangle":
            return Triangle()

        elif shape_type == "square":
            return Square()
        else:
            print("Invalid shape type entered :(")


if __name__ == "__main__":

    # create instance of factory.
    factory = ShapeFactory()

    # create object of circle class using factory.
    obj = factory.get_shape("circle")
    print(f" Shape created of type : {obj.get_name()}")

    # create object of square class using factory.
    obj = factory.get_shape("square")
    print(f" Shape created of type : {obj.get_name()}")
