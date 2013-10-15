---
layout: post
author: jpowell
published: true
title: Jaleesa's Turtles
---

# Hogwarts!

So I'm kind of sad that I didn't get the chance to be as creative as some of you with this assignment. Continuing with my obsession with Harry Potter, I named my turtles after some students at Hogwarts. Maybe in my free time I'll see if I can come up with more appropriate-looking turtles.

<3.

![Singin a song, all day long at HOOOOOOOOOOOOGWAAAAAAAAAARTS!](http://i947.photobucket.com/albums/ad316/dieschwarzeskobra/2e852328-6896-4f76-9271-14d10f2e6bfa_zps94e47f02.jpg)


```
import turtle
import turtlehack
from random import randint

hermione = turtle.Turtle()
ron = turtle.Turtle()
harry = turtle.Turtle()
draco = turtle.Turtle()

for x in range(0,11):
  turtlehack.colored_circle(ron, 55, 'orange', 2)
  turtlehack.n_sided_polygon(ron, 8, 'orange', 5, 25)

for x in range(0,3):
  draco.color('green')
  turtlehack.random_location(draco, 300, 50)
  turtlehack.dotted_line(draco, 20, 15, 'green')


for x in range(0,7):
  turtlehack.random_location(harry, 25, 335)
  harry.color('red')
  turtlehack.colored_circle(harry, 55, 'red', 2)
  turtlehack.n_sided_polygon(harry, 8, 'red', 5, 25)

for x in range(0,8):
  turtlehack.random_location(hermione, 200, 100)
  turtlehack.colored_circle(hermione, 33, 'yellow', 2)
  turtlehack.colored_circle(hermione, 55, 'yellow', 2)
  turtlehack.n_sided_polygon(hermione, 8, 'yellow', 5, 25)

turtle.done()

```
