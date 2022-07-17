from turtle import *
from random import *

def col():
	return randint(0, 255)

pu(); ht()

shape("square"); shapesize(2)

bgcolor("black"); colormode(255)

for i in range(5):
	for j in range(7):
		color(col(), col(), col())
		stamp()
		fd(40)
	goto(0, ycor() + 40)

done()