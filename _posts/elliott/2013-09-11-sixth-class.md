---
layout: post
author: elliott
title: Sixth Class Notes
published: true
---

Announcements:

* Follow-through on pull requests
* Empty lines before lists and code blocks
* Embedding - Make sure you have a link to a *file*  Dropbox tricks you.

* Fix your pull requests.  I'll post comments- get to them as soon as you're able.  [Notifications](http://github.com/notifications) are your friends.
* Commiters: Erin H, Elizabeth and Danielle

* [Show-offs]({{ site.baseurl }}/showoffs/turtle.html)

* Next week will be a light week.  I'll be remote for class on Weds.  We'll be using CodingBat.com for exercises, so that class will be fun, helping each other out and completing exercises.  Go over concepts and skills you're unsure of, and get caught up before we dive in to some nitty gritty.

Questions?


## Commiters & Duties

1. Everyone make this change to their test posts:  Add `published: false` to the header (the part in between the hyphens ---)

2. Open a pull request describing those changes.  Include a link to your site.

3. Committers: For each Pull Request, tag it to the "All students have made their test posts drafts" Milestone.

4. Committers: View the site, check that the test posts are gone.  If there are problems, @mention me.

5. Committers: If all looks good with the pull request, go ahead and merge.

Looking ahead: 

* Commit access for everyone.
* Contributor guidelines for our repository

Questions?


## Python and Data

1. Open two terminals. Start Python in both by typing `python`

2. Type `help(bin)` to see the help page for the `bin` function.

3. Let's convert some numbers to binary!  Use the other terminal for these:

* `bin(54)`
* `bin(10)` 
* `bin(10.01)`

Why does this give an error?  

4. Let's do some math on variables!  Type these:

* `a = 3` - assignment.  What happens if you `print a`?
* `a += 1` - augmented assignment. What happens if you `print a`?

Augmented assignment does something to the variable in the process of assigning it a value.

* What happens if you type `b += 1`?  Why?

The augmentation performed here is addition.  Are there other augmentation operators?  In your help terminal, type `help('+=')`.

* `a = 5`
* `a ^= 2`  What is a now?

* `b = 50`
* `b /= 2`  What is b now?

Advanced: Shifts

* `c = 2`
* `c <<= 3`  What is c?  What has happened?  Hint: use `bin` to find a pattern.

From the readings: Conversions

* `print int('2') + 3`
* `print 2 + str((3)`

### Break: Discuss some results

________________

## If there's time

Let's refactor this code:

```python

import turtle
canvas = turtle.Turtle()
palate = turtle.Screen()


turtle.pensize(5)
palate.bgcolor('white')
turtle.hideturtle()


turtle.color('purple')
turtle.circle(20)
turtle.circle(-20)
turtle.setheading(90)
turtle.circle(20)
turtle.circle(-20)


palate.bgcolor('green')
turtle.color('red')
turtle.circle(50)
turtle.circle(-50)
turtle.setheading(180)
turtle.circle(50)
turtle.circle(-50)


palate.bgcolor('lightblue')
turtle.color('white')
turtle.circle(100)
turtle.circle(-100)
turtle.setheading(90)
turtle.circle(100)
turtle.circle(-100)


turtle.done()
```


Two approaches:

* The `for` Loop
* The function
* See also [Dave's code](http://silshack.github.io/fall2013/post/2013/09/09/Daves-circles.html)
