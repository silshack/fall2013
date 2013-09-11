---

layout: post
title: Erin C.'s turtle drawing, box & circles
author: ecarter
categories: ecarter

---



This is my turtle code. It made a funny shape. Here's a screenshot, as well.


![My strange Turtle drawing](http://i.imgur.com/E0KngfV.jpg)



```python

import turtle

edward = turtle.Turtle()

def draw_side(turtle_name, color, length, angle):
  turtle_name.color(color)
  turtle_name.forward(length)
  turtle_name.left(angle)
  turtle_name.circle(50)

draw_side(edward, 'red', 75, 75)
draw_side(edward, 'blue', 75, 105)
draw_side(edward, 'green', 75, 75)
draw_side(edward, 'yellow', 75, 105)


turtle.done()


```
