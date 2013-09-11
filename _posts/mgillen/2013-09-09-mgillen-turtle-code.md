---
title: Mary's First Work with Turtle
layout: post
author: mgillen
categories: post
---

What a long day. Jeez.

The first thing that happened this morning was that Ubuntu wouldn't recognize my password. As it's operating as a virtual machine, there isn't really a way to boot into the mode necessary to change the administrator password (at least not easily as far as I can tell). As a result, I had to reinstall Ubuntu which failed over and over again (literally about 10 times - thanks, Virtual Box!). Needless to say, I didn't get to spend class as I wanted and participate in the mini coding fest. More work and class followed and I'm only now uploading my code for Turtle and it isn't nearly as fancy as I would like. Hopefully, I will have some free time soon to fool around with it a bit.

I did take some time to mess around with Turtle though, and it seems pretty flexible for as simple as it is. I saw some really neat drawings online and tried my hand at making the Triforce from Zelda but I just couldn't make it cooperate with me. With time running out, I decided to alter our example in class a little bit (and I do mean only a little).


```python
import turtle

edward = turtle.Turtle()
edward.pensize(10)

for color in ['red','yellow','green',blue']:
   edward.color(color)
   edward.forward(200)
   edward.right(90)

turtle.done()
```

And that looks like...

![Turtle Square](http://i.imgur.com/3T3bZyN.png)

Like I said, basic, but better than nothing. 
