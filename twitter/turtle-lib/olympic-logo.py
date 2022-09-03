from turtle import *

speed(7)
width(10)

def drawing(a, b):
    penup()
    goto(a, b)
    pendown()
    
def function(clr, a, b):
    color(clr)
    circle(80)
    drawing(a, b)

drawing(-190,-10)
x = -190
first_line = ['blue', 'black', 'red']
for i in first_line: function(i, x + ((first_line.index(i) + 1) * 185), -10)

drawing(-100, -90)
x = -100
second_line = ['yellow', 'green']
for i in second_line: function(i, x + ((second_line.index(i) + 1) * 185), -90)

hideturtle()
done()