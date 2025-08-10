# polymorphism_demo.py
import math

class Shape:
    def area(self):
        """Base method meant to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle: length × width."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate area of a circle: π × radius²."""
        return math.pi * (self.radius ** 2)
