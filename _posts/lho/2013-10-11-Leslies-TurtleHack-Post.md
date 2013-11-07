---
layout: post
author: lho
categories: post
---

This is my TurtleHack post!

```python
import turtle
from turtlehack import *

bri=turtle.Turtle()
bri.penup()
bri.setpos(0,-100)
bri.pendown()
for i in range(0,200):
   bri.circle(i)
   bri.color(random_color())
   random_circle(bri,25,max_size=100)

```

<img src="http://i.imgur.com/E2ohTne.png">
