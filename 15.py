import copy


class Point:
    """Represents a point in 2D space"""

class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

print(box)


def move_rectangle(rectangle, dx, dy):
    rectangle.corner.x += dx
    rectangle.corner.y += dy

move_rectangle(box, 50, 20)
print(box.corner.x, box.corner.y)

def move_rectangle_new(rectangle, dx, dy):
    rectangle_new = copy.deepcopy(rectangle)
    rectangle_new.corner.x += dx
    rectangle_new.corner.y += dy
    return rectangle_new

box_2 = move_rectangle_new(box, 30, 40)

print(box.corner.x, box.corner.y, box_2.corner.x, box_2.corner.y)