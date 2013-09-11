---
layout: post
author: kshaffer
categories: post
---

After tinkering for a while (probably too long) I wound up with this interesting accident. Below is my Turtle code.

```python
import turtle

edward = turtle.Turtle()

edward.penup()
edward.setpos(50, 150)
edward.pendown()

for color in ['blue', 'green', 'red']:
  for radius in range(0, 100, 10):
    edward.color(color)
    edward.circle(radius)
    edward.right(45)
    edward.forward(100)
    
edward.penup()
edward.setpos(0, 20)
edward.pendown()
edward.write('STOP!')

turtle.done()
```

And below is a picture of the result.

![](http://i.imgur.com/3Ydh0qg.png) 
