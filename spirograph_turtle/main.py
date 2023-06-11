from turtle import *
import random

tim = Turtle()
colormode(255)

tim.speed("fastest")
def get_color() :
  r = random.randint(0,255)
  g = random.randint(0,255)
  b=  random.randint(0,255)
  color = (r,g,b)
  return color
 

for i in range(180) :
  tim.color(get_color())
  tim.setheading(tim.heading() + 10)
  tim.circle(50)
