---
layout: post
author: sburnham
published: true
title: "Sarah's turtle"
---

# Tessie!

I like adding a colored background to the turtles - next time, I might let it auto select a color!


![Screen shot 1](https://lh3.googleusercontent.com/Hr6XPxOP3fkDLAwh3vPwP52UGuek8vPK1-xjUQd32t0=w444-h541-no)
![Screen shot 2](https://lh4.googleusercontent.com/cximLLJ6g5gv3MXrmuQPm0VORTihrkVAwyNRM2x46h4=w459-h541-no)


```

import turtle
import random

tessie = turtle.Turtle()

def random_color():
   color_value = format(random.randint(0, 16777215), '06x')
   return "#" + color_value

def random_location(turtle, x, y):
   random_x = random.randint(-x, x)
   random_y = random.randint(-y, y)
   turtle.setpos(random_x, random_y)

wn = turtle.Screen()
wn.bgcolor("dark blue")


for i in range(random.randint(0, 250)):
   turtle.left(random.randint(0, 175))
   turtle.forward(random.randint(25, 175))
   turtle.dot(random.randint(20, 75), random_color())
   turtle.forward(50)
   turtle.left(90)
   turtle.left(90)
   turtle.left(90)
   turtle.left(90)

turtle.done()   

```
