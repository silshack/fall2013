---
title: Turtle Hack - Fractal
layout: post
author: abrown
categories: post
---

Greetings all,

So I am reading a book for a class called 'Leadership and New Science' by Margaret Wheatley.  The book argues that organizations should take some of their leadership and management principles from new science theories, especially in quantum physics (focusing on chaos and order).  The amazon review is located [here](http://www.amazon.com/Leadership-New-Science-Learning-Organization/dp/1881052443).

Anyway, one of the concepts Wheatley discusses is fractals. Fractals form patterns because they are self-similar. In geometry, two figures are “similar” if they have the exact same shape. So all squares are similar to each other, but not all rectangles have to be similar (shape can differ; think a wide rectangle versus a tall rectangle).  And we’re talking about the shape, not the size.  Since fractals are self-similar that means they essentially create copies of the same shape; and these shapes are repeated over and over again to create patterns. Wheatley wrote about how fractals could be represented in simple computer programs.  So, I set out to see if I could create a fractal with our turtle hack.

To create a fractal, I first added a function to my local copy of the turtlehack.py by using nano.  I borrowed code from the Open Book Project, which you can find [here](http://openbookproject.net/thinkcs/python/english3e/recursion.html). 

So, I then tried to run the function in a second terminal.  My turtle (I named him Jack) started to spin but he did not move. He looked like he was getting very dizzy.  I knew I had to get him moving, so off to google I went.  I figured out that I had to move his position.  I also discussed this with a friend of mine who is a programmer.  He walked me through some of the thought processes. I used the setpos, up, and down commands to set his position and then have him move based on the fractal function written early.  I'm going to be honest here, this took a while and a lot of googling, and I think I only understand some of it.  Having it to talk through with someone has been helpful, as well. 

So without further ado, here are my screen shots, and my code:

![The function I put into turtlehack.py](https://lh5.googleusercontent.com/-v2YngV27q_0/Uldn8QUzaMI/AAAAAAAAAKw/G9unoV9FPvw/w880-h495-no/turtle_hack_fractal.jpg)
![The python code to execute Jack, the turtle](https://lh4.googleusercontent.com/-BS-fD1H6BNQ/Uldn8b2AOhI/AAAAAAAAAK0/6YrZceEkNxI/w880-h495-no/turtle_hack_fractal_2.jpg)

So don't let the neatness of the second screenshot fool you, I messed that up a lot. I just kept closing the terminal and starting fresh because I got frustrated seeing the error messages over and over again.

Here is the code for the function:

```python

def koch(turtle, order, size):
  if order == 0:
    turtle.forward(size)
  else:
    for angle in [60, -120, 60, 0]:
        koch(turtle, order-1, size/3)
        turtle.left(angle)
        
```

Here is the code to execute the function:


```python

import turtle
from turtlehack import *
import random

jack= turtle.Turtle()
  jack.speed(5)
  jack.up()
  jack.setpos(-200, 0)
  jack.down()
  koch(jack, 3, 500)
  
```

So, I guess the next step would be to merge my function in my local copy of turtlehack into the master copy. However, I am still confused about out to use the command line to do this.  Does anyone have any good notes on this?

Thanks!

Ashley

