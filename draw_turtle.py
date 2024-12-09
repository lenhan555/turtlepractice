import turtle as t

t = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
t.shape("turtle")
t.color("red")
num_sides = 3


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for shape_size_n in range(3, 11):
    draw_shape(shape_size_n)
