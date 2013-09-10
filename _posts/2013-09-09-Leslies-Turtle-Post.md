---
layout: post
author: lho
categories: post
---

This is my turtle post, will update it when I get turtle working.

```python
import turtle
turtle=turtle.Turtle()
turtle.begin_poly()
turtle.shape("turtle")
turtle.fill(True)
for _ in range(3):
  turtle.forward(100)
  turtle.left(120)
turtle.fill(False)
turtle.heading()
turtle.setheading(90)
turtle.setposition(0,-10)
turtle.setposition(0,-100)
turtle.setposition(100,-100)
turtle.setposition(-100,-100)
turtle.setposition(-50,-50)
turtle.setheading(50)
```
