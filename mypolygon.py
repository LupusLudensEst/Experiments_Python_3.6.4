from swampy.TurtleWorld import *
import math

# world = TurtleWorld()
# bob = Turtle()

# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)

# for i in range (4):
#     fd(bob, 100)
#     lt(bob)

# print(bob)

# for i in range(4):
#     print('Hello!')

# wait_for_user()

# 4.3 Exercises
# The following is a series of exercises using TurtleWorld. They are meant to be fun, but they
# have a point, too. While you are working on them, think about what the point is.
# The following sections have solutions to the exercises, so don’t look until you have finished
# (or at least tried).
# 1. Write a function called square that takes a parameter named t, which is a turtle. It
# should use the turtle to draw a square.
# Write a function

# world = TurtleWorld()
# t = Turtle()
# def square(t):
#     for i in range(4):
#         fd(t, 50)
#         lt(t)
#     print(t)
#
# print(square(t))
# wait_for_user()

# 2. Add another parameter, named length, to square. Modify the body so length of the
# sides is length, and then modify the function call to provide a second argument. Run
# the program again. Test your program with a range of values for length.

# world = TurtleWorld()
# t = Turtle()
# length = int(input('Enter the length: '))
# def square(t):
#     for i in range(4):
#         fd(t, length)
#         lt(t)
#     print(t)
#
# print(square(t))
# wait_for_user()

# 3. The functions lt and rt make 90-degree turns by default, but you can provide a
# second argument that specifies the number of degrees. For example, lt(bob, 45)
# turns bob 45 degrees to the left.

# world = TurtleWorld()
# t = Turtle()
# length = 100
# angle = 90
# def square(t):
#     for i in range(4):
#         fd(t, length)
#         lt(t, angle)
#     print(t)
#
# print(square(t))
# wait_for_user()

# Make a copy of square and change the name to polygon. Add another parameter
# named n and modify the body so it draws an n-sided regular polygon. Hint: The
# exterior angles of an n-sided regular polygon are 360/n degrees.

# world = TurtleWorld()
# t = Turtle()
# length = 5
# polygon = int(input("Enter the quantity of sides of polygon: "))
# def square(t):
#     for i in range(polygon):
#         fd(t, length)
#         lt(t, 360 / polygon)
#     print(t)
#
# print(square(t))
# wait_for_user()

# 4. Write a function called circle that takes a turtle, t, and radius, r, as parameters and
# that draws an approximate circle by invoking polygon with an appropriate length
# and number of sides. Test your function with a range of values of r.
# Hint: figure out the circumference of the circle and make sure that length * n =
# circumference.
# Another hint: if bob is too slow for you, you can speed him up by changing
# bob.delay, which is the time between moves, in seconds. bob.delay = 0.01 ought
# to get him moving.

# world = TurtleWorld()
# t = Turtle()
# length = float(input('Enter the length: '))
# polygon = 100
# t.delay = 0.0001
# def circle(t, length, polygon):
#     for i in range(polygon):
#         fd(t, length)
#         lt(t, 360 / polygon)
#     print(t)
#
# print(circle(t, length, polygon))
# wait_for_user()

world = TurtleWorld()
bob = Turtle()
# ray = Turtle()
#
# length = float(input("Enter the length: "))
# def square(t, length):
#     for i in range(4):
#         fd(t, length)
#         lt(t)
# square(bob, length)
# square(ray, length)
# wait_for_user()
#
def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)
polygon(bob, n=7, length=70)
wait_for_user()
#
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)
polygon(bob, n=7, length=70)
wait_for_user()