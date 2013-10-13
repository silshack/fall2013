---
title: assignment
layout: post
author: zekuny
categories: post
---

Codes:

```python

import turtle
from turtlehack import *
import random

focus=turtle.Turtle()

for i in range(random.randint(0,10)):
  random_location(focus, 300, 300)
  focus.color(random_color())
  random_circle(focus, 5, 15)

for i in range(random.randint(0,5)):
  colored_square(focus, 50, random_color())

random_location(focus,300,300)

for i in range(random.randint(0,8)):
  n_sided_polygon(focus,8,color=random_color(),line_thickness=3,line_length=80)

for i in range(random.randint(0,12)):
  n_sided_polygon(focus,8,color=random_color(),line_thickness=3,line_length=80)
```

![Image](https://pbs.twimg.com/media/BWUlsfOCcAAO4zi.jpg)
