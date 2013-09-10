---
layout: post
author: lgrindheim
categories: turtle
---

The more I messed with my drawings, the uglier they became. I took a step back and tried to make one look a little nicer. Here's the code for Jim.

import turtle

jim=turtle.Turtle()

for color in ['purple', 'blue', 'green', 'yellow', 'orange', 'red', 'purlple', 'blue', 'green', 'yellow', 'orange', 'red','purple']:
  jim.color(color)
  jim.circle(60)
  jim.fill(45)
  jim.forward(35)
  jim.circle(30)
  
turtle.done()


And here's what Turtle drew:
![jim](https://plus.google.com/u/0/photos/110811624909797200563/albums/posts/5921798785468515074?pid=5921798785468515074&oid=110811624909797200563)
