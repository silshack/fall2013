---
title: Turtle Circle Crazy Party
layout: post
author: odorsey
categories: post
---
Here's my turtlehack picture!<br />

![Turtlehack Picture](http://img9.imageshack.us/img9/9534/l1ir.jpg)

And my corresponding code... 

```python
import turtle
import turtlehack
import random

larry = turtle.Turtle()

for i in range(random.randint(0,10)):
  larry.color(turtlehack.random_color())
  turtlehack.random_circle(larry, 10, 15)
  turtlehack.random_location(larry, 125, 125)
larry.color(turtlehack.random_color())
turtlehack.random_circle(larry, 34, 10)

turtle.done()
```
