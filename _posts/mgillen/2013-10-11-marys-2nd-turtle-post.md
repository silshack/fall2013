---
title: Mary's Take on Modern Art, An Experiment with Turtle
layout: post
author: mgillen
categories: post
---


Calling it, I'm going to be rich some day. They don't make art like this anymore. I also want to say I am still working on getting my triforce to work. It will happen. I'll make an announcement when it's working and beautiful!

![My Turtle](http://i.imgur.com/bmSfhZr.png)

Code:

```python

import turtle
from turtlehack import *
import random

mary = turtle.Turtle() 

mary.speed(14)

for i in range(random.randint(0,10)):
  random_location(mary, 300, 300)
  mary.color(random_color())
  random_circle(mary, 5, 15)

for i in range(random.randint(0, 5)):
   random_location(mary, 150, 200)
   n_sided_polygon(mary, 8, color=random_color(), line_thickness=5, line_length=50)

turtle.done()
```
