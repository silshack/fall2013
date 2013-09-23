---
title:  Stacey and Michelle Slightly-Suicidal Gaming Adventure
layout: post
author:
-mbaxter
-smantooth
category: post
---

So Michelle already posted on Google+ about the [python workshop](https://plus.google.com/u/0/111805292479048821920/posts/HgrBGGLxbKi) that we 
went to in Raleigh.  One of the excercises was creating and modifying a number guessing game.  That wasn't quite thrilling enough for Michelle and I,
so we upped the vodka-soaked, backalley ante with a Russian Roulette game.  After a lot (A LOT) of refactoring, we came up with this code:

```python
import random
"""
An attempted game made by Stacey and Michelle!
"""

chamber = random.randint(0, 5)
trigger_pulls = 6
num_tries = 0

print ("Let's play a game.\nRussian Roulette.\n\nYou have a gun.\nThere is one bullet, and six chambers in the gun.\n\n\nGood luck.")

guess = 0
while guess != chamber and num_tries < trigger_pulls:
    guess = raw_input("Do you want to play?\n")
    if guess == "y" and chamber == num_tries:
        print ("You die! Thanks for playing!")
        break
    elif guess == "y" and chamber != num_tries:
        print ("You're still alive, I see. Try again.")
    else:
        print ("Lame. Get out.")
        break
    num_tries = num_tries + 1
```

