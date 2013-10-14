---
title: Grant's Turtle Drawing 2
layout: post
author: gmclendon
categories: post
---  


Sadly without any cool ninja turtle references:  
![turtledrawing2](http://i.imgur.com/F1CxqiK.png)

and the code:  

```python  
import turtle 
import turtlehack
from random import randint

bob = turtle.Turtle()
bob.ht()
bob.speed(0)

def bobfill(turtle):
	if randint(0,2) == 0:
		turtle.fill(True)
for i in range(randint(20,50)):
	bob.pendown()
	n = randint(0,3)
	if n == 0:
		bobfill(bob)
		turtlehack.colored_circle(bob,randint(0,50), turtlehack.random_color())
		bob.fill(False)
	if n == 1:
		bobfill(bob)
		turtlehack.colored_square(bob,randint(0,50), turtlehack.random_color())
		bob.fill(False)
	if n == 2:
		bobfill(bob)
		turtlehack.random_circle(bob, randint(1,10))
		bob.fill(False)
	if n == 3:
		bobfill(bob)
		turtlehack.n_sided_polygon(bob, randint(1,10),turtlehack.random_color(), randint(1,20), randint(5,120))
		bob.fill(False)
	if randint(0,2) == 1:
		bob.right(randint(0,360))
		turtlehack.dotted_line(bob, randint(5,40), randint(1,10), turtlehack.random_color())
	if (randint(0,90)%3)!=0:
		bob.penup()
	turtlehack.random_location(bob, 200,200)
print "done"
turtle.done()
```  
