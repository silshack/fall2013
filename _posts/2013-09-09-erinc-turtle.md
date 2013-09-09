---
layout: post
title: Erin C.'s turtle drawing: box & circles
author: ecarter
---

This is my turtle code. It made a funny shape. I'll try to figure out how to upload the screenshot, too.

``` python

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
