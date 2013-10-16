---
layout: post
author: alexharding
published: true
---

# Right triangles!

I decided to try and make a function that builds regular right triangles. Everone's familiar with the grade-school idea of the pythagorean theorem, with a^2 + b^2 = c^2.
So I wrote a function that takes three inputs... a width, a height and a direction. The width and height make up the right angle of the triangle, and the function creates the hypotenuse.
The direction input decides which direction it draws in, or which side the right angle will face.

Instead of making this only work with standard triangles (45/45/90 or 30/60/90), I brushed up on geometry and trig a little to make it work for any two lengths. The function requires some math importing to get this to work.

At the end of each triangle, the turtle gets reset to the home position.

There're other things that could be added to this for fun... right now it only draws right and left, making it able to flip up or down would be cool. Or add a fill component so it fills a color too. Lots of fun to be had!
#Function

```
import turtle

from math import sqrt, asin, pi

def right_triangle(height,width,direction):
# takes direction to mean which side of the triangle will have the hypoteneuse


#	using pythagorean theorem: hyp is the sqrt of height^2 + width^2
	hypotenuse=sqrt((height**2)+(width**2))
	
#	using radians for sin functions
	turtle.radians()

	if direction == 'right':
		turtle.forward(width)
		#90 degrees in radians
		turtle.setheading(1.57079633)
		turtle.forward(height)
		#pi is 180 degrees in radians, arcsin of side over hypotenuse equals angle
		turtle.setheading(pi+asin(height/hypotenuse))
		turtle.forward(hypotenuse)
		turtle.home()

	if direction =='left':
		turtle.setheading(pi)
		turtle.forward(width)
		#90 degrees in radians
		turtle.setheading(1.57079633)
		turtle.forward(height)
		#arcsin of side over hypotenuse equals angle, subtracted
		turtle.setheading(-asin(height/hypotenuse))
		turtle.forward(hypotenuse)
		turtle.home()
```


#Screenshot
![](http://i.imgur.com/v3bk98n.png)
