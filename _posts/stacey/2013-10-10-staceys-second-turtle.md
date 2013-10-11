---
title: I wonder how often April O'Neil washed that yellow jumpsuit
layout: post
author: smantooth
categories: post
---

My turtles look like they grew some really gnarly fungus.


BOOM!

![Pisanello, the oft forgotten fifth ninja turtle approves this python turtle image.](http://imageshack.us/a/img854/1432/gtjw.png)




And just for funzies, I did one with squares too.



![CIRCLES AND SQUARES.  CIRCLES AND SQUARES.](http://imageshack.us/a/img820/729/44ms.png)



```python

import turtle
from turtlehack import *
import random

bobbert = turtle.Turtle()
dukes = turtle.Screen()

turtle.hideturtle()

for i in range(random.randint(40, 90)):

  turtle.left(random.randint(1, 360))
  turtle.penup()
  turtle.forward(random.randint(25, 300))
  turtle.pendown()
  turtle.dot(random.randint(10, 125), random_color())
  colored_square(bobbert, random.randint(10, 300), random_color())  # leave this line out if you don't want the squares
  turtle.penup()
  turtle.home()
  dukes.bgcolor(random_color())  # change this to a single color if strobe lights give you seizures


turtle.done()

```





I originally wanted to make a function that produced random polka dots (or something that looked vaguely like chickenpox) and tried to use the random location function in turtlehack.
That did not work at all.  It just drew a bunch of dots in the center of the page while the turtle zoomed off to draw some random lines.  Also,
anyone know any good ways to keep the drawings on the canvas?  It took me an embarssingly long time to realize that sending the loop back to the
center everytime would help keep my dots from wandering off, but it also means they clump toward the middle.

Dots!

