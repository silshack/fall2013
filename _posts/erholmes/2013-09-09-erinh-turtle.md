---
title: Erin H's First Turtle
layout: post
author: erholmes
categories: post
---

For my first turtle, I made the Olympic rings. I'm hoping to avoid litigation from the IOC since I'm using it for educational purposes. My code and a link to the screenshot are below.

```python
#olympic rings
import turtle

edward = turtle.Turtle()
edward.pensize(10)
edward.color('white')
edward.setpos(-150,0)


for color in ['blue', 'black', 'red']:
  edward.color(color)
  edward.circle(75)
  edward.penup()
  edward.forward(175)
  edward.pendown()

edward.penup()
edward.setpos(-65,-95)
edward.pendown()

for color in ['yellow', 'green']:
  edward.color(color)
  edward.circle(75)
  edward.penup()
  edward.forward(175)
  edward.pendown()

turtle.done()
```

![Olympic Rings Screenshot](http://www.unc.edu/~erholmes/olympic_rings.png)

Source: 
Python Turtle Library Documentation: http://docs.python.org/2/library/turtle.html
