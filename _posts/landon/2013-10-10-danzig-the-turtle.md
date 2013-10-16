---
layout: post
author: lgrindheim
categories: posts
---

I made a drawing with a some of the functions that were developed in our turtlehack project. Pretty fun.

Here's the code:

```
import turtle
from turtlehack import *
import random

danzig= turtle.Turtle()

#following elliot's example and speeding things up
danzig.speed(15)

#this is mostly an experiment
for i in range(random.randint(0, 150)):
  danzig.write("GLENN")
  danzig.color(random_color())
  danzig.pendown()
  random_location(danzig, 300, 300)
  danzig.circle(random.randint(5,105))
  
turtle.done()


```

![danzig](http://landonandjana.files.wordpress.com/2013/09/screen-shot-2013-10-10-at-8-17-21-pm.png?w=300&h=189)
