---
layout: post
author: kshaffer
categories: post
---

Here's the graphic: 

![](http://i.imgur.com/C3ofI79.png)

And here's the code:

```python
import turtle
from turtlehack import *

samo = turtle.Turtle()

for i in range(0, 10):
  random_location = (samo, i, i)
  n_sided_polygon(samo, 6, color = random_color(), line_thickness = 5, line_length = 80)
```
