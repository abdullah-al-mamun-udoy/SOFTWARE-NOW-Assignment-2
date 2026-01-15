import turtle

screen = turtle.Screen()
screen.setup(width=1000, height=600)
screen.title("Recursive Polygon")

turt = turtle.Turtle()
turt.speed(0)
turt.hideturtle()

# Recursive function to draw one modified edge
def draw_edge(length, depth):
    if depth == 0:
        turt.forward(length)
        return

    part = length / 3

    draw_edge(part, depth - 1)
    turt.left(60)

    draw_edge(part, depth - 1)
    turt.right(120)

    draw_edge(part, depth - 1)
    turt.left(60)

    draw_edge(part, depth - 1)

# Draws a regular polygon using recursive edges
def draw_polygon(sides, length, depth):
    angle = 360 / sides

    for _ in range(sides):
        draw_edge(length, depth)
        turt.left(angle)


# User inputs
sides = int(input("Enter the number of sides: "))
length = int(input("Enter the side length: "))
depth = int(input("Enter the recursion depth: "))

# Adjust starting position so the shape fits on screen
turt.penup()
turt.goto(-length / 2, length / 2)
turt.setheading(270)
turt.pendown()

draw_polygon(sides, length, depth)

turtle.done()