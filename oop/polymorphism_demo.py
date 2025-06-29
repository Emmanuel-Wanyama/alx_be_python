# polymorphism_demo.py

import math

class Shape:
    """
    Base class for geometric shapes.
    Defines a generic area method that must be overridden by derived classes.
    """
    def area(self):
        """
        Calculates the area of the shape.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.
    Overrides the area method to calculate the rectangle's area.
    """
    def __init__(self, length, width):
        """
        Initializes a Rectangle instance with length and width.

        Args:
            length (float or int): The length of the rectangle.
            width (float or int): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float or int: The area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.
    Overrides the area method to calculate the circle's area.
    """
    def __init__(self, radius):
        """
        Initializes a Circle instance with a radius.

        Args:
            radius (float or int): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle using the formula pi * radius^2.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

