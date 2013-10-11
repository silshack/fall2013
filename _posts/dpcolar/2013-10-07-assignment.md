---
layout: post
author: dpcolar
title: Implement the n-sided polygon
categories: post
---

The n-sided polygon is implemented using turtlehack.
<br>

```python

import turtle
import turtlehack
import random

# A function that draws an n-sided polygon
def n_sided_polygon(turtle, n, color="#FFFFFF", line_thickness=1):
	'''
	Draw an n-sided polygon
	input: turtle, number of sides, line color, line thickness
	'''
	# for n times:
	# Draw a line, then turn 360/n degrees and draw another

	# set initial parameters
  	turtle.degrees()
	line_length=80
  	turtle.pensize(line_thickness)
  	turn_angle = (360/n)
  	i = 1

	# Draw each line segment and turn

  	while (i <= n):
		turtle.color(color)
    		turtle.pendown()
    		turtle.forward(line_length)
   		turtle.penup()
    		turtle.right(turn_angle)
    		i += 1

	return 0
 
## MAIN ##
# set initial parameters
n=random.randint(3,12)

# create the Turtle instance
graphic = turtle.Turtle()
# Call the polygon code
n_sided_polygon(graphic, n, turtlehack.random_color(), random.randint(4,8))

# Close and exit
ignore = raw_input("hit any key to continue:")

```

![N-sided Polygon](http://www.unc.edu/~pcolar/nsidedpolygon.png)
