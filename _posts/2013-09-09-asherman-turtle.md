---
title: Amber Attempts to Draw a Turtle using turtle
layout: post
author: asherman
categories: post
---

In the end, this just turned out to be a dot (or filled in circle) with an inverted semicirlcle and line attached.  Trying to add feet and a tail got complicated...

```python

import turtle

sam = turtle.Turtle()
def draw_side(turtle_name, color, length, angle):
  turtle_name.color(color)
  turtle_name.forward(length)
  turtle_name.left(angle)

sam.pensize(10)
sam.color('white')
sam.setpos(-150,0)

for color in ['green']:
  sam.color(color)
  sam.dot(75)
  sam.penup()
  sam.forward(175)
  sam.pendown()

  sam.penup()
  Sam.setpos(95,-95)
  sam.pendown()
  sam.left(90)
  sam.circle(120,180)
  sam.setpos(95,-95)
  sam.right(180)

turtle.done()
```

![Turtle Screenshot](http://www.flickr.com/photos/101542990@N02/)

Source: 
Python Turtle Library Documentation: http://docs.python.org/2/library/turtle.html
