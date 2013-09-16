---
layout: post
author: carolinp
categories: post 
---
I stole the idea from the interactive version of our book: https://sphotos-b-lga.xx.fbcdn.net/hphotos-prn1/75915_10151828830269788_2026467913_n.jpg

Which was actually extremely helpful, so you guys should definitely check it out! I may not have the math totally down, but I feel like I understand how for loops work.
![My Python Turtle](https://sphotos-b-lga.xx.fbcdn.net/hphotos-prn1/75915_10151828830269788_2026467913_n.jpg)

```python
import turtle
wn = turtle.Screen()
wn.bgcolor("orange")
andy = turtle.Turtle()
andy.color("pink")
andy.shape("triangle")

print(range(5, 60, 2))
andy.up()

for size in range (5, 60, 2):
   andy.stamp()
   andy.forward(size)
   andy.right(24)
 

>> wn.exitonclick()

```
