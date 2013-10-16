---
title: Christopher's Flower on Sun on Flower Turtle
layout: post
author: ckenrick
categories: post
---

Here's my sad attempt at a Turtle post. I spent all day trying to figure it out, but I'm happy enough with how it turned out.

```python

import turtle
import turtlehack
import random

slowpoke = turtle.Turtle()
from turtlehack import *
for i in range(0, 10):
  random_location = (slowpoke, i, i)
  n_sided_polygon(slowpoke, 9, color=random_color(), line_thickness = 3, line_length = 75)
  
from turtle import *
color ('blue', 'green')
begin_fill()
while True:
  forward(175)
  left(75)
  if abs(pos()) < 1:
    break
end_fill()

from turtlehack import *
for i in range(95, 109):
  random_location = (slowpoke, i, i)
  n_sided_polygon(slowpoke, 9, color=random_color(), line_thickness = 3, line_length = 25)
  
turtle.done()
```
![Slowpoke the Turtle Screenshot!](http://i.imgur.com/kFMWxqb.png)
  
