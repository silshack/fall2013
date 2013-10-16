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

![jim](http://landonandjana.files.wordpress.com/2011/07/newdrawing-pk.jpg)
