---
title: Cowabunga, Dude
layout: post
author: smantooth
categories: post
---

So, I really like circles.  Here's my python code!

```python
import turtle
canvas = turtle.Turtle()
palate = turtle.Screen()


turtle.pensize(5)
palate.bgcolor('white')
turtle.hideturtle()


turtle.color('purple')
turtle.circle(20)
turtle.circle(-20)
turtle.setheading(90)
turtle.circle(20)
turtle.circle(-20)


palate.bgcolor('green')
turtle.color('red')
turtle.circle(50)
turtle.circle(-50)
turtle.setheading(180)
turtle.circle(50)
turtle.circle(-50)


palate.bgcolor('lightblue')
turtle.color('white')
turtle.circle(100)
turtle.circle(-100)
turtle.setheading(90)
turtle.circle(100)
turtle.circle(-100)


turtle.done()
```

Screenshot:
![This is where a pythonian turtle should be.  The horror!](http://imageshack.com/a/img823/946/zgk1.png)

This turtle changes background color as it draws, which you can't really tell from the screen shot.

There's probably a better way to do all the repeating circles.  Anyone have any ideas?

Source:  [Python Turtle Library Documentation](http://docs.python.org/2/library/turtle.html)
