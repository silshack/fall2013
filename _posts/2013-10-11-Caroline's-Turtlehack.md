---
layout: post
author: carolinp
categories: post 
---

![my python turtlehack drawing](https://lh3.googleusercontent.com/--wt2U_IdVP4/Ulg1miqTcjI/AAAAAAAAAMk/e094NHv7i-U/w737-h553-no/python_turtlehack.png)

```python

import turtle
import random
from turtlehack import *
lisa = turtle.Turtle()

size = 50
for i in range(10):
  colored_square(lisa, size, random_color())
  size += 10

for i in range(3):
  lisa.forward(75)
  lisa.left(120)
  lisa.color(random_color())
  random_circle(lisa, 5, 10)


```

