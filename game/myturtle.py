#AUTHOR TARUN BISHT
import turtle
# SETTING UP SCREEN
def set_screen(title="Turtle Window",width=600,height=600,bgcolor="white"):
    window=turtle.Screen()
    window.title(title)
    window.bgcolor(bgcolor)
    window.setup(width=width, height=height)
    # turns off screen updates
    window.tracer(0)
    return window
# CREATING A TURTLE
def create_turtle(color="white",shape="square",direction=None,pos=(0,0)):
    tut=turtle.Turtle()
    # animation speed of turtle in turtle module set to zero to get maximum responsiveness
    tut.speed(0)
    tut.color(color)
    tut.shape(shape)
    # To let the turtle not to draw lines
    tut.penup()
    # Start position of turtle 0,0 set it to middle of screen
    tut.goto(pos[0],pos[1])
    if dir!=None:
        tut.direction=direction
    else:
        tut.direction="stop"
    return tut
# PEN TURTLE
def create_pen(color="white",shape="square",pos=(0,0)):
    tut=create_turtle(color=color,shape=shape,pos=pos)
    tut.hideturtle()
    return tut
