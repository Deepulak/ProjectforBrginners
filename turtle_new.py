from turtle import *
from random import *

ht(); color('white'); bgcolor('black')

for i in range(4):
	fd(120); bk(120); rt(90)

def rnd():
	return randint(127, 255)

colormode(255); width(4)

for i in range(0, 110, 2):
	color(rnd(), rnd(), rnd())
	circle(i, 50)

done()