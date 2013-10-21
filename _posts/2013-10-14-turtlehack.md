---
layout: post
author: jgeer
categories: post
---

This took me forever and I'm late on the deadline anyways but I think it's worth it to get what I want. I'm a big 
Modest Mouse fan and this picture just reminds me of their song 'Other People's Lives' which is one of my favorites
(listen to it if you haven't). It's very repetitive and mixed up but it has patterns and connections and it's just great.

Note the circles don't really contribute to this idea. i also tried random_coloring the words and didn't like it very much.
Although I did like that the cursor ended up off the lines like it was 'out of road' which is a major lyric of the song,
but that wasn't intentional.

Here's the code:

import turtle
from turtlehack import *
import random

james = turtle.Turtle()

for i in range(random.randint(0, 10)):
  random_location(james, 50, 50)
  cruz.color(random_color())
  random_circle(james, 2, 4)
  
words = ['out', 'of', 'everything', 'at', 'last']
for i in range(random.randint(0, 30)):
  rando_word = random.choice(words)
  james.penup()
  random_location(james, 150, 100)
  james.write(rando_word)
  james.pendown()
  
words = ['out', 'of', 'gas', 'car', 'road']
for i in range(random.randint(30, 50)):
  rando_word = random.choice(words)
  james.penup()
  random_location(james, 150, 100)
  james.write(rando_word)
  james.pendown()
  
  
![Modest Mouse Turtlehack](http://i.imgur.com/WXP8j3l.png)
