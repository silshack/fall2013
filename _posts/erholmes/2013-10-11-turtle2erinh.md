---
layout: post
author: erholmes
categories: post
title: The Revenge of the Turtle
published: true
---

Ta Da!

```python
import turtle
import turtlehack

edward = turtle.Turtle()
edward.pensize(3)

for i in range(48):
  mycolor = turtlehack.random_color()
  x = edward.xcor()
  y = edward.ycor()
  turtlehack.dotted_line(edward, 10, 5, mycolor)
  turtlehack.n_sided_polygon(edward, 6, mycolor, 3, 25)
  edward.penup()
  y = y + 1
  x = x + 1
  edward.setpos(x,y)
  edward.pendown()
  
turtle.done()  
```

![Erin's Second Turtle](http://www.unc.edu/~erholmes/turtle2.png)
