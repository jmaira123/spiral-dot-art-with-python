import turtle 
import random 

# Setup the turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

# Function to draw spiral alien dots
def draw_spiral_dots():
    for i in range(100):
        t.color(random.random(), random.random(),random.random())
        t.penup()
        t.goto(0, 0)
        t.forward(i * 5)
        t.pendown()
        t.dot(i * 0.5)
        t.right(45)

# Draw the spiral alien dots
draw_spiral_dots()

# Hide the turtle and finish
t.hideturtle()
turtle.done()
