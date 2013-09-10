---
layout: post
author: kshaffer
categories: post
---

So after doing a bit of sleuthing on Python's capabilites, I found that not only is it a great language for creating games and computing data (as well as learning to code to begin with), but it can also be used to *manipulate audio files!!!* There are a number of audio modules that can be used for anything from manipulaing raw audio data to ripping CD's to generating your own synths! Pretty awesome, and you can read more about it here: https://wiki.python.org/moin/Audio.

In summary here's a short function I wrote describing the effect this new knoweldge has had on me. You can try it out by copying it and pasting it into your Terminal and then hitting Enter/Return until you see the Python >>> prompt. Next, type the function name mind_blower followed by your name and whatever you're currently doing in parentheses (e.g. "Jon", "sleeping"). Make sure the "name" and "state" are in quotes and are comma separated. What does Python return? What happens when you type in "Kyle" and "read article"? Can you tailor the function to print something similar for your name?

```python
def mind_blower(name, state):
  if name == "Kyle":
    if state == "read article":
      print "Mind. Blown!"
    elif state != "read article":
      print "You're Kyle, but you didn't read the article."
  elif name != "Kyle":
    if state == "read article":
      print "Well, at least YOU read it..."
    else:
      print "Who are you, and what did you do?"
```
