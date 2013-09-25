---
title:  Stacey and Michelle Slightly-Suicidal Gaming Adventure
layout: post
author:
- mbaxter
- smantooth
categories: post
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


Basically the idea is to have the computer select a random number between 1-6 which represents the chamber the bullet is in.  Every time the player
enters 'y'/pulls the trigger, the program checks to see if you've hit the selected chamber.  Once you hit the right (wrong!) chamber, you die
(figuratively) and the game ends.


Some of the things we had trouble with in this code and wanted to mention were:

*  We originally had __input__ instead of __raw_input__, and everytime the user would enter a 'y' or 'n' about whether or not they wanted to play, we got a syntax error.
From what I understood, __input__ tries to interpret the response from the user as a numeric expression, while __raw_input__ treats everything like a string.
So __raw_input__ was much better suited for our purpose.

*  This code was much longer, because we started out testing __chamber__(the random number selected) against 1, then 2, then 3, all the way to 6.  One of the
workshop instructors pointed out that we had actually already created a variable that was essentially doing that for us.  Comparing __chamber__ to __num_tries__
did the exact same thing and let us really cut down the code.  In retrospect, it's a really simple fix, but it didn't occur to me that we could
double dip with a variable like that.  I guess the lesson is to check to see if something you already did can serve multiple purposes.
Recycle, reduce, re-use!  Captain Planet!

*  Lastly, I wanted to mention the __break__ that's in this code several times.  When we first wrote this code, it kept running all the way though all the chambers instead
of stopping between each turn or when the person died.  Not cool!  The lovely people at the workshop let us know that if we put __break__ at the end of our condition
clauses it would stop the loop without having it run all the way through.  There's more about it on the [python website](http://docs.python.org/2/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops).  We found it very handy!
