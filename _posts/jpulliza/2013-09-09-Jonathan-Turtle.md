---
layout: post
author: jpulliza
categories: post
title: Jonathan's Turtle Post
---

Test text for this post.

Here is an image of my turtle example:

![Turtle Example](https://dl.dropboxusercontent.com/u/4614624/SILS%20Hack%20Box.png)

I chose to change the color of the turtle and pen in increments of one using RGB. Here is the code:

```python
import turtle

nancy = turtle.Turtle()
turtle.colormode(255)

for i in range(254)

  nancy.color((255-i,255-i,i),(255-i,255-i,i)
  nancy.forward(i*2)
  nancy.left(i*2)
  
turtle.done
```
