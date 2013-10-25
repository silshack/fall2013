---
layout: post
author: mbaxter
category: posts
---
So, using the turtlehack library wasn't working for me. I took the parts of the code that I wanted to try and use and had to put it into my turtle program manually. I still included it in the code I've written here, but when I ran it through the terminal I removed that part because it resuted in an error. Oh well.

I first tried some code that resulted in a crazier picture than I was originally intending.
![Crazy Turtle Picture](https://lh4.googleusercontent.com/-RC6Gpwkkj3k/UlhbPqYSP-I/AAAAAAAAAWc/Kz5dMiYoaS0/w539-h504-no/Screen+Shot+2013-10-11+at+3.36.44+PM.png"crazy turtle picture")

And here's the code I used for it:

```python

import turtle
from turtlehack import *
import random

finn = turtle.Turtle()

def random_color():
   color_value = format(random.randint(0, 16777215), '06x')
   return "#" + color_value

def random_location(turtle, x, y):
   random_x = random.randint(-x, x)
   random_y = random.randint(-y, y)
   turtle.setpos(random_x, random_y)

turtle.shape("turtle")
turtle.color("white")
wn = turtle.Screen()
wn.bgcolor("black")

for i in range(random.randint(25, 300)):
  turtle.left(random.randint(0, 200))
  turtle.forward(random.randint(25, 300))
  turtle.pendown()
  turtle.dot(random.randint(23, 175), random_color())
  turtle.stamp()
  turtle.home()

turtle.done()
```

Then, I messed around with some of the numbers and got a better picture:
![Better Turtle Picture](https://lh5.googleusercontent.com/-SzB0umWli6Q/UlhbPoYSD_I/AAAAAAAAAWY/cjtUwkW6Cc4/w567-h526-no/Screen+Shot+2013-10-11+at+3.40.48+PM.png"better turtle picture")

And the code:

```python

import turtle
from turtlehack import *
import random

finn = turtle.Turtle()

def random_color():
   color_value = format(random.randint(0, 16777215), '06x')
   return "#" + color_value

def random_location(turtle, x, y):
   random_x = random.randint(-x, x)
   random_y = random.randint(-y, y)
   turtle.setpos(random_x, random_y)

turtle.shape("turtle")
turtle.color("white")
wn = turtle.Screen()
wn.bgcolor("black")

for i in range(random.randint(25, 300)):
  turtle.left(random.randint(0, 200))
  turtle.forward(random.randint(25, 300))
  turtle.pendown()
  turtle.dot(random.randint(23, 175), random_color())
  turtle.stamp()
  turtle.home()

turtle.done()
```

A lot of tears and panic went into this. A. LOT. So appreciate it for what it is: little turtles hanging out on happy balloons.
