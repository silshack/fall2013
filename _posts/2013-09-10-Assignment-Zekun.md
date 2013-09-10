---
title: assignment
layout: post
author: zekuny
categories: post
---

Codes:
```python

from turtle import *
import time
 
color("green")

up()

goto(0,-50)

down()

circle(50)
up()

goto(0,0)
down()
 
color("blue")
for deg in range(0, 61, 6):
    right(90 + deg)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
     
up()
goto(-150,-120)
color("red")
write("Done!")
 
time.sleep(10)
```

![Image](http://ww4.sinaimg.cn/mw1024/a5997331jw1e88hno5o51j20mm0cejtb.jpg)
