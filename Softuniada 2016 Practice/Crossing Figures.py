import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    @staticmethod
    def parse(circle_string):
        circle_coords = circle_string.split('(')[1].split(')')[0].split(',')
        center_coords = [float(coord.strip()) for coord in circle_coords[:2]]
        radius = float(circle_coords[2])
        return Circle(Point(center_coords[0], center_coords[1]), radius)

    def is_inside_circle(self, point):
        return (point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2 - self.radius ** 2 <= 0.01

class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    @staticmethod
    def parse(rectangle_string):
        rectangle_coords = rectangle_string.split('(')[1].split(')')[0].split(',')
        top_left_coords = [float(coord.strip()) for coord in rectangle_coords[:2]]
        bottom_right_coords = [float(coord.strip()) for coord in rectangle_coords[2:]]
        return Rectangle(Point(top_left_coords[0], top_left_coords[1]), Point(bottom_right_coords[0], bottom_right_coords[1]))

    def is_inside_rectangle(self, point):
        return self.top_left.x <= point.x <= self.bottom_right.x and \
               self.bottom_right.y <= point.y <= self.top_left.y


def relative_position(rectangle, circle):
    top_left_inside_circle = circle.is_inside_circle(rectangle.top_left)
    bottom_right_inside_circle = circle.is_inside_circle(rectangle.bottom_right)

    if top_left_inside_circle and bottom_right_inside_circle:
        return "Rectangle inside circle"
    elif circle.is_inside_circle(rectangle.top_left) or circle.is_inside_circle(rectangle.bottom_right):
        return "Circle inside rectangle"
    elif rectangle.is_inside_rectangle(circle.center):
        return "Circle inside rectangle"
    elif rectangle.top_left.x <= circle.center.x <= rectangle.bottom_right.x or \
         rectangle.bottom_right.y <= circle.center.y <= rectangle.top_left.y:
        return "Rectangle and circle cross"
    else:
        return "Rectangle and circle do not cross"


T = int(input())
for _ in range(T):
    circle_input = input()
    rectangle_input = input()
    circle = Circle.parse(circle_input)
    rectangle = Rectangle.parse(rectangle_input)
    result = relative_position(rectangle, circle)
    print(result)
