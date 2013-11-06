---
layout: post
author: danielle
categories: post
title: Truly random circles
---
This is my use of the turtlehack library. Results will vary.

![This is my screen shot](http://i.imgur.com/NNg0SQ4.png)

This is my code:

```python
import turtle
from turtlehack import *
import random
fido = turtle.Turtle()
canvas = turtle.Screen()
canvas = bgcolor("black")
for i in range(20):
  random_circle(fido, 3, max_size = 100)
  fido.color(random_color())
  fido.penup()
  random_location(fido, 50, 70)
  fido.pendown()
dotted_line(fido, 50, 12, random_color())
```
