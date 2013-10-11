---
layout: post
author: carolinp
categories: post 
---

![new turtlehack](https://dl.dropboxusercontent.com/u/4614624/new_turtle.jpg)

```python

import turtle
from turtlehack import *
import random

qrt = turtle.Turtle()

for i in range(random.randint(0,50)):
  qrt.color(random_color())
  n_sided_polygon(qrt, random.randint(5,10), random_color())
  random_location(qrt,50,100)
  
turtle.done()

```

