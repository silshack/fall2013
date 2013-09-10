---
layout: post
author: dpcolar
title: Dave's Concentric Circles
categories: post
---

For this assignment, I expermented with sizes and fills of circles.  The code uses random numbers in a range to select the colors.
<br>

```python
# Concentric Circles of random colors

import turtle
from random import randint

graphic = turtle.Turtle()
color_list = ['red','orange','yellow','green','violet','brown','blue','gray']

for circle_size in range(135,15,-15):
    pencolor = color_list[randint(0,7)]
    fillcolor = color_list[randint(0,7)]
    graphic.color(pencolor,fillcolor)

    if circle_size%2 is 0:
      graphic.fill(True)
    else:
      graphic.fill(False)
    graphic.pensize(randint(1,4))
    graphic.circle(circle_size)

turtle.done()

```

![alternately filled concentric circles](http://www.unc.edu/~pcolar/screenshot.png)
