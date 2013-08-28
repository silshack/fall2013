---
layout: post
author: lho
categories: post
---

Hey guys, so just looking at some Python code and this was something that Java has, if-else statements, so here's some Python code for that:

```python
if i < 20:
    print "That is less than 20."
    if i % 3 == 0:
        print "It is divisible by 3."
elif i == 20:
    print "That is exactly twenty.  How nice for you."
else:
    if i % 2 == 1:
        print "That is an odd number."
    else:
        print "That is twice", i / 2, '.'
    print "Wow! That's more than 20!"
```

