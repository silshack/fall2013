---
layout: post
author: odorsey
categories: post
---

After today's experience in class, I was slightly frustrated with the syntax errors I kept receiving, but I finally got my Turtle program working! I definitely wouldn't say that the experience was all bad; simply trial-and-error (as the case usually is with coding!). As a result, I was able to learn more about what Python likes and doesn't like. I realize that it is important to note when an ellipsis (ie. ...) occurs and when it shows a set of arrows (ie. >>>). I'm not sure if I'm using the correct technology here, but the ellipsis seems to continue a statement and the set of arrows implies that a new statement is being created. 

I played with my Turtle code in python for some time, just trying to get a feel for the code and what different parameters would do. Here is the code that I came up with: 

```python
import turtle
timothy = turtle.Turtle()
for color in ['red', 'blue', 'green', 'yellow']:
  timothy.color("blue")
  timothy.forward(80)
  timothy.left(120)
  timothy.forward(80)
  timothy.left(120)
  timothy.forward(80)
  timothy.left(120)

caleb = turtle.Turtle()
caleb.shape("turtle")
caleb.color("red")
caleb.left(45)
caleb.forward(50)

sam = turtle.Turtle()
sam.shape("turtle")
sam.color("orange")
sam.forward(80)

corrinne = turtle.Turtle()
corrinne.shape("turtle")
corrinne.color("yellow")
corrinne.right(50)
corrinne.forward(70)

sephy = turtle.Turtle()
sephy.shape("turtle")
sephy.color("green")
sephy forward(50)
turtle.done()
```

I really wanted to make some actual turtles appear (they're so cute!), so I found some code to do so! You'll see that I have four colorful turtles coming out from the corner of their triangle. Here's a screenshot of the result:

![Turtles screenshot](https://plus.google.com/?utm_source=bk&utm_medium=ha&utm_campaign=plusgeneralb2c&utm_term=%2Bgoogle%20%2Bplus&gclid=CNqU4pbavrkCFeRj7Aod4nkAiQ&partnerid=ussebr)

I found my code from the following web resource: here[Hello, little turtles!](http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html). 
