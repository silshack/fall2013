---
title: Grant's Turtle Drawing
layout: post
author: gmclendon
categories: gmclendon
---

I made a rather simple drawing (I'm not an artist), but made two functions to do it. I think the python-tk library includes similar, better functions. But that's no fun for learning

```python
import turtle 

turtle1 = turtle.Turtle()
turtle1.speed(0)
turtle2 = turtle.Turtle()
turtle2.pensize(5)

def draw_shape(turtle_name, sides, size, color, xpos, ypos, fill):
	turtle_name.showturtle()
	turtle_name.color(color)
	angle = 360/sides
	length = size/sides
	turtle_name.penup()
	turtle_name.setpos(xpos,ypos)
	turtle_name.pendown()
	turtle_name.fill(fill)
	for i in range(0,sides):
		turtle_name.forward(length)
		turtle_name.left(angle)
	turtle_name.fill(False)
	turtle_name.hideturtle() #Lets hide the turtle	

def draw_line(turtle_name, len, xpos, ypos):
	turtle_name.showturtle()
	turtle_name.pu()
	turtle_name.setpos(xpos, ypos)
	turtle_name.pd()
	turtle_name.forward(len)
	turtle_name.hideturtle()

draw_shape(turtle1, 30, 900 ,'yellow', -250, 0, True)
draw_shape(turtle1, 4, 4000, 'black', -400, -1050, True)
draw_shape(turtle1, 6, 200, 'red', 10, -60, True)
draw_shape(turtle1, 6, 250, 'red', 80, -140, True)
draw_shape(turtle1, 6, 600, 'red', 200, -320, True)
draw_line(turtle2, 250, 25, 200)
draw_line(turtle2, 200, 100, 150)
turtle.done()
```

![turtle drawing screenshot](http://i.imgur.com/b7xuCuY.png)
