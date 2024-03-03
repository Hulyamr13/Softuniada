import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def is_inside_circle(self, point):
        return (point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2 <= self.radius ** 2

class Rectangle:
    def __init__(self, top_left, top_right, bottom_left, bottom_right, center):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.center = center

    @staticmethod
    def parse(rectangle_string):
        rectangle_coords = list(map(float, rectangle_string.split(',')))
        if len(rectangle_coords) >= 4:
            return Rectangle(
                Point(rectangle_coords[0], rectangle_coords[1]),
                Point(rectangle_coords[2], rectangle_coords[1]),
                Point(rectangle_coords[0], rectangle_coords[3]),
                Point(rectangle_coords[2], rectangle_coords[3]),
                Point((rectangle_coords[0] + rectangle_coords[2]) / 2, (rectangle_coords[1] + rectangle_coords[3]) / 2))
        else:
            return None

    def is_inside_rectangle(self, point):
        return (self.top_left.x <= point.x <= self.top_right.x and
                self.bottom_right.y <= point.y <= self.top_right.y)

def main():
    T = int(input().strip())

    for _ in range(T):
        figure1_str = input().strip()
        figure2_str = input().strip()

        figure1_type, figure1_params = figure1_str.split('(', 1)
        figure2_type, figure2_params = figure2_str.split('(', 1)

        figure1_params = figure1_params.rstrip(')').split(',')
        figure2_params = figure2_params.rstrip(')').split(',')

        if figure1_type == 'rectangle':
            rectangle = Rectangle.parse(','.join(figure1_params))
            circle = Circle(Point(float(figure2_params[0]), float(figure2_params[1])), float(figure2_params[2]))
        else:
            rectangle = Rectangle.parse(','.join(figure2_params))
            circle = Circle(Point(float(figure1_params[0]), float(figure1_params[1])), float(figure1_params[2]))

        top_left_inside_circle = circle.is_inside_circle(rectangle.top_left)
        top_right_inside_circle = circle.is_inside_circle(rectangle.top_right)
        bottom_left_inside_circle = circle.is_inside_circle(rectangle.bottom_left)
        bottom_right_inside_circle = circle.is_inside_circle(rectangle.bottom_right)

        top_inside_rectangle = rectangle.is_inside_rectangle(circle.center)
        right_inside_rectangle = rectangle.is_inside_rectangle(Point(circle.center.x + circle.radius, circle.center.y))
        bottom_inside_rectangle = rectangle.is_inside_rectangle(Point(circle.center.x, circle.center.y - circle.radius))
        left_inside_rectangle = rectangle.is_inside_rectangle(Point(circle.center.x - circle.radius, circle.center.y))

        if (top_left_inside_circle and top_right_inside_circle and bottom_left_inside_circle and bottom_right_inside_circle):
            print("Rectangle inside circle")
        elif (top_inside_rectangle and right_inside_rectangle and bottom_inside_rectangle and left_inside_rectangle):
            print("Circle inside rectangle")
        else:
            center_distance_x = abs(circle.center.x - rectangle.center.x)
            center_distance_y = abs(circle.center.y - rectangle.center.y)
            width = rectangle.top_right.x - rectangle.top_left.x
            height = rectangle.top_left.y - rectangle.bottom_left.y

            if center_distance_x > width / 2 + circle.radius or center_distance_y > height / 2 + circle.radius:
                print("Rectangle and circle do not cross")
            elif (center_distance_x <= width / 2 or center_distance_y <= height / 2):
                print("Rectangle and circle cross")
            else:
                corner_distance = (center_distance_x - width / 2) ** 2 + (center_distance_y - height / 2) ** 2
                if corner_distance - circle.radius ** 2 <= 0:
                    print("Rectangle and circle cross")
                else:
                    print("Rectangle and circle do not cross")

if __name__ == "__main__":
    main()
