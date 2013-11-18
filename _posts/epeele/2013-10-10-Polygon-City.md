---
title: Elizabeth's Turtlehack Post
layout: post
author: epeele
categories: post
---

It's not a Kandinsky, but it's pretty.

```python

>>> import turtle
>>> from turtlehack import *
>>> import random
>>> 
>>> harry = turtle.Turtle()
>>> 
>>> #speeds us up, courtesy of Elliott Hauser
... harry.speed(20)
>>> 
>>> #random circles
... for i in range(random.randint(0, 30)):
...   random_location(harry, 450, 500)
...   harry.color(random_color())
...   random_circle(harry, 10, 30)
... 
>>> #back to another point
... for i in range(random.randint(0, 10)):
...   random_location(harry, 200, 150)
...   n_sided_polygon(harry, 6, color="#FF00FF", line_thickness=3, line_length=65)
... 
0
0
0
>>> #back again to another point
... for i in range(random.randint(0, 5)):
...   random_location(harry, 150, 200)
...   n_sided_polygon(harry, 8, color="#FFFF00", line_thickness=5, line_length=50)
... 
0
0
0
0
0
>>> turtle.done()

```

![Turtlehack](http://www.unc.edu/~epeele/file/peele_turtlehack.png)
