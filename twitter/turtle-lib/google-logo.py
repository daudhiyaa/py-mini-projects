from turtle import *

list_color = ['#4285F4', '#0F9D58', '#F4B400', '#DB4437']
# blue = '#4285F4', green = '#0F9D58', yellow = '#F4B400', red = '#DB4437'

def rightCircle(r, c1, c2):
    right(r)
    circle(c1, c2)

def coloring(c1, c2, clr):
    circle(c1, c2)
    color(clr, clr)

def turtleDirection(r1, r2, r3, f, c1, c2):
    right(r1)
    forward(f)
    right(r2)
    circle(c1, c2)
    right(r3)
    forward(f)

def colorFilling(r, c1, c2, clr):
    right(r)
    circle(c1, c2)
    color(clr, clr)

def changeDirection(r, f):
    right(r)
    forward(f)

pensize(5)
speed(5)
color(list_color[0], list_color[0])

forward(120)
right(90)

coloring(-150, 50, list_color[1])
coloring(-150, 100, list_color[2])
coloring(-150, 60, list_color[3])

# ------------ filling
begin_fill()
circle(-150,100)
turtleDirection(90, 90, 90, 50, 100, 100)
end_fill()

# ------------ filling
begin_fill()
color(list_color[2], list_color[2])
turtleDirection(180, 90, 90, 50, 100, 60)
rightCircle(90, -150, 60)
end_fill()

changeDirection(90, 50)

# ------------ filling
colorFilling(90, 100, 60, list_color[1])
begin_fill()
circle(100, 100)
turtleDirection(90, 90, 90, 50, -150, 100)
end_fill()

# ------------ filling
colorFilling(90, 100, 100, list_color[0])
begin_fill()
circle(100, 25)
left(115)
forward(65)
changeDirection(90, 42)
changeDirection(90, 124)
rightCircle(90, -150, 50)
changeDirection(90, 50)
end_fill()

penup()