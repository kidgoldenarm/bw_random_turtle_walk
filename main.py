from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
heading = [0, 90, 180, 270]

def rand_color():
    for rando in range(0,3):
        r = random.randint(0, 255)
        rgb = (r, r, r)
    return rgb

def rand_heading():
    nesw = random.choice(heading)
    return nesw

for x in range(1500):
    tim.speed("fastest")
    tim.pencolor(rand_color())
    tim.width(80)
    tim.setheading(rand_heading())
    tim.forward(40)

    


screen.exitonclick()