import turtle as t
import random

t = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


########### Challenge 2 - Draw a Dashed Line ########
t.shape("turtle")
t.speed("fastest")

for _ in range(100):
    t.color(random_color())
    t.circle(100)
    current_heading = t.heading()
    t.setheading(current_heading + 1)
