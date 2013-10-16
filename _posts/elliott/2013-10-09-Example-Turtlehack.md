---
author: elliott
layout: post
---


Here's my Turtlehack:

![](http://puu.sh/4LZtG.png)

Generated off of this code:

```
import turtle
from turtlehack import *
import random

cruz = turtle.Turtle()

# Speeds us up:
cruz.speed(10)

# Make a bunch of random circles
for i in range(random.randint(0,10)):
  random_location(cruz, 300, 300)
  cruz.color(random_color())
  random_circle(cruz, 5, 15)

# Go back to the origin and make the last circle
random_location(cruz, 0, 0)
cruz.color(random_color())
random_circle(cruz, 5, 15)

words = ['random', 'tuna salad', 'Mark Hamil', 'mug', 'narwhal', 'carpet']
for i in range(random.randint(0,10)):
  rando_word = random.choice(words)
  cruz.penup()
  cruz.color(random_color())
  random_location(cruz, 250, 205)
  cruz.write(rando_word)
  cruz.pendown()

turtle.done()
```