---
layout: post
author: danielle
categories: post
---

I am not a graphic design person, so my turtle graphic is not the next Mona Lisa, but I have managed to include a few original figures.
There is a sun, a layered color circle figure (I don't know what to call it), and a face. 

I looked at the following sites to get inspiration about the code I wrote (they are not guilty of my creative strugglings):

[Chapter 25 of Turtle graphic documentation](http://www.python.org/doc//current/library/turtle.html#color-control)

[Chapter 24 of Turtle graphic documentation](http://docs.python.org/2/library/turtle.html#turtle-motion)

Here is my code:

```python
import turtle
kenny = turtle.Turtle()
kenny.penup()
## This is the excessively large sun.
kenny.goto(-200, 0)
kenny.pendown()
kenny.color('yellow')
kenny.begin_fill()
kenny.circle(150)
kenny.end_fill()
kenny.penup()
## This is the weird colorful circle figure that looked like it had potential.
kenny.goto(0,0)
kenny.pendown()
kenny.color('green')
kenny.begin_fill()
kenny.circle(10)
kenny.end_fill()
kenny.color('violet')
kenny.circle(20)
kenny.color('red')
kenny.circle(40)
kenny.penup()
## This is the left pupil.
kenny.goto(-90, -110)
kenny.color('black')
kenny.pendown()
kenny.begin_fill()
kenny.circle(10)
kenny.end_fill()
kenny.penup()
## This is the left eye.
kenny.goto(-90, -130)
kenny.pendown()
kenny.circle(30)
kenny.penup()
## This is the right pupil.
kenny.goto(10, -110)
kenny.pendown()
kenny.begin_fill()
kenny.circle(10)
kenny.end_fill()
kenny.penup()
## This is the right eye.
kenny.goto(10, -130)
kenny.pendown()
kenny.circle(30)
kenny.penup()
## This is the full face.
kenny.goto(-60, -260)
kenny.pendown()
kenny.circle(130)
kenny.penup()
## This is the mouth.
kenny.goto(-90, -190)
kenny.pendown()
kenny.forward(60)
turtle.done()
```

![This is my screen shot](http://i.imgur.com/jqo3Nqxs.jpg)
