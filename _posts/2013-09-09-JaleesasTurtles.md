---
layout: post
title:  "Meet Nagini"
date:   2013-09-09 13:23:23
categories: post
author: jpowell
---

I wanted to attempt to make [this adorable snake](http://i947.photobucket.com/albums/ad316/dieschwarzeskobra/cobra_zpsebc1bac9.jpg) [(source)](http://cache2.allpostersimages.com/p/LRG/30/3066/MFIDF00Z/posters/northcott-david-albino-monocled-cobra-native-to-se-asia.jpg). I don't think I even came close, but it's nearing time to be done with this. So [here's a link to the screenshot](http://i947.photobucket.com/albums/ad316/dieschwarzeskobra/Screenshotfrom2013-09-09232703_zps17e74735.png), and my code is below.

Sources:
* [Python documentation](http://docs.python.org/2/library/turtle.html)
* [Documentation provided on silshack](http://silshack.github.io/fall2013/turtle.html)

```python

import turtle
turtle.bgcolor('tan')

nagini = turtle.Turtle()
nagini.shape('circle')
nagini.color('black')
nagini.penup()
nagini.setpos((-150,-150))
nagini.pendown()
x = -150
y = -150
for x in range(-150,0):
  x = x+1
  y = y + 0.07
  nagini.setpos((x,y))

for x in range(0,100):
  x = x+1
  y = y + 0.17
  nagini.setpos((x,y))

for x in range(100,200):
  x = x+1
  y = y + 0.27
  nagini.setpos((x,y))

nagini.circle(50,150)

nagini.penup()
nagini.setpos((-20,170))
nagini.pendown()
nagini.circle(-30,110)


nagini.pendown()
nagini.circle(-30,110)

x=-20
y=220

for x in range(-20, 10):
  x = x+1
  y = y+0.5
  nagini.setpos((x,y))

for x in range(10, 50):
  x = x+1
  nagini.setpos((x,y))

for x in range(49, 90):
  x = x+1
  y = y-0.5
  nagini.setpos((x,y))


nagini.penup()
nagini.setpos((50,214.5))
nagini.pendown()
nagini.circle(-30,200)
nagini.setpos((70,100))
nagini.setpos((225,-5))
nagini.penup()
nagini.setpos((125,-5))
nagini.pendown()
nagini.setpos((10,80))
nagini.setpos((-25,180))


nagini.setpos((10,80))
nagini.setpos((-25,180))
nagini.penup()
nagini.setpos((125,-5))
nagini.pendown()
nagini.setpos((-5,-25))
nagini.setpos((-135,-35))
nagini.penup()
nagini.setpos((15,220))
nagini.dot(5,'red')
nagini.pendown()
nagini.color('red')
nagini.setpos((20,218))
nagini.penup()
nagini.setpos((45,220))
nagini.pendown()
nagini.dot(5,'red')
nagini.setpos((41,218))
nagini.penup()
nagini.setpos((50,200))
nagini.pendown()
nagini.color('black')
nagini.setpos((30,208))
nagini.setpos((10,200))
nagini.shape('turtle')

voldemort = turtle.Turtle()
voldemort.penup()
voldemort.setposition((-100,50))
voldemort.pendown()
voldemort.color('red')
voldemort.setposition((-100,0))

voldemort.color('red')
voldemort.setposition((-100,0))

voldemort.penup()
voldemort.setposition((-80,50))
voldemort.pendown()
voldemort.setposition((-80,0))
voldemort.setposition((-80,50))
voldemort.setposition((-60,0))

voldemort.penup()
voldemort.setposition((-60,25))
voldemort.pendown()
voldemort.setposition((-80,25))
voldemort.penup()
voldemort.setposition((-55,50))
voldemort.pendown()
voldemort.setposition((-55,0))
voldemort.setposition((-55,50))
voldemort.setposition((-45,0))
voldemort.setposition((-35,50))
voldemort.setposition((-35,0))

voldemort.penup()
voldemort.setposition((-100, -5))
voldemort.pendown()
voldemort.setposition((-100,-55))
voldemort.setposition((-80, -55))

voldemort.penup()
voldemort.setposition((-75,-5))
voldemort.pendown()

voldemort.setposition((-75,-5))
voldemort.pendown()
voldemort.setposition((-65,-5))
voldemort.setposition((-65,-55))
voldemort.setposition((-75,-55))
voldemort.setposition((-75,-5))

voldemort.penup()
voldemort.setposition((-60,-5))
voldemort.pendown()
voldemort.setposition((-60,-55))
voldemort.setposition((-60,-5))
voldemort.setposition((-50,-5))
voldemort.setposition((-50,-10))
voldemort.setposition((-60,-10))
voldemort.setposition((-50,-55))

voldemort.penup()
voldemort.setposition((-45,-5))
voldemort.pendown()
voldemort.setposition((-45,-55))
voldemort.setposition((-35,-55))
voldemort.setposition((-35,-5))
voldemort.setposition((-45,-5))

voldemort.penup()
voldemort.setposition((-100,-60))
voldemort.pendown()
voldemort.setposition((-90,-110))
voldemort.setposition((-80,-60))
voldemort.penup()
voldemort.setposition((-75,-60))


voldemort.penup()
voldemort.setposition((-75,-60))
voldemort.pendown()
voldemort.setposition((-75,-110))
voldemort.setposition((-65,-110))
voldemort.setposition((-65,-60))
voldemort.setposition((-75,-60))
voldemort.penup()
voldemort.setposition((-60,-60))
voldemort.pendown()
voldemort.setposition((-60,-110))
voldemort.setposition((-50,-110))

voldemort.penup()
voldemort.setposition((-45,-60))
voldemort.pendown()
voldemort.setposition((-45,-110))
voldemort.setposition((-35,-110))
voldemort.setposition((-35,-60))
voldemort.setposition((-45,-60))

voldemort.penup()
voldemort.setposition((-30,-60))
voldemort.pendown()
voldemort.setposition((-20,-60))
voldemort.setposition((-20,-70))
voldemort.setposition((-30,-70))
voldemort.setposition((-30,-60))
voldemort.setposition((-30,-110))
voldemort.setposition((-20,-110))

voldemort.penup()
voldemort.penup()
voldemort.setposition((-15,-60))
voldemort.pendown()
voldemort.setposition((-15,-110))
voldemort.setposition((-15,-60))
voldemort.setposition((-5,-110))
voldemort.setposition((5,-60))
voldemort.setposition((5,-110))

voldemort.penup()
voldemort.setposition((10,-60))
voldemort.pendown()
voldemort.setposition((10,-110))
voldemort.setposition((20,-110))
voldemort.setposition((20,-60))
voldemort.setposition((10,-60))


voldemort.penup()
voldemort.setposition((25,-60))
voldemort.pendown()
voldemort.setposition((35,-60))
voldemort.setposition((35,-70))
voldemort.setposition((25,-70))
voldemort.setposition((25,-60))
voldemort.setposition((25,-110))
voldemort.setposition((25,-70))
voldemort.setposition((35,-110))

voldemort.penup()
voldemort.setposition((40,-60))



voldemort.penup()
voldemort.setposition((40,-60))
voldemort.pendown()
voldemort.setposition((50,-60))
voldemort.setposition((45,-60))
voldemort.setposition((45,-110))



turtle.done()

```
