---
layout: post
author: elliott
title: Thirteenth Class Notes
---

Announcements:  

* Github looking good (Merge @gerbal's pull request) 
* G+ check in
* Thanks for the feedback - keep it coming
* Local git installs, Jekyll, and site hacking oh my!
* Guest Eric Martindale on Weds, so vim & emacs that day.  See Emacs reading [here](http://blog.zenspider.com/blog/2012/06/my-emacs-workflow.html)
* See exercise due Wednesday, below.

## Installing `git`

Git is the open source version control program that underlies the Github collaboration website.  We tried it last week, now we'll install and use it.

Installing git on Ubuntu is super easy.  From a Terminal, type
```
sudo apt-get install git
```

Some tutorials might tell you to install `git-core`, which will work too.  To check whether git is installed, type
```
which git
```
`which` is a UNIX program that locates the location of the file that would be run if you typed a command.  It's useful for checking if you have a program installed and, if so, where it is.

## NEW: First- Time Setup

Git has an excellent first-time git setup turorial [here](https://help.github.com/articles/set-up-git#set-up-git).  We did this during class and you should too if you're making up the work.

## Cloning your first repo

Github does a pretty good job making it easy to clone repos.  In the bottom right of every project page there is a box with the URL you'll need to clone.  The syntax for cloning is 
```
git clone URL
```
In the case of the [turtlehack repo](https://github.com/silshack/fall2013turtlehack) the URL is https://github.com/silshack/fall2013turtlehack.git.  It's essentially the project's URL with a `.git` on the end.

Go ahead and clone turtlehack: 

1. Open a terminal 
2. Type `git clone https://github.com/silshack/fall2013turtlehack.git`
3. Type `cd fall2013turtlehack` to **change directories** into the folder git just created for you
4. Type `ls` to see what's in there.

## Using a library

There's a file in the repo we cloned called `turtlehack.py` that has code we can use in it.  We can access it in python by importing it.

1. Fire up python by typing `python` in a terminal.
2. from the `>>>` prompt type `import turtlehack`
3. you can then use custom functions by typing `turtlehack.functionname()`.  For instance, after importing the turtlehack library, we could use the `random_color()` function by typing `turtlehack.random_color()`

## Turtlehacking

So let's see what we can do!  Type each line in sequence at a python prompt (`>>>`), then play around yourself.

```python
import turtle
import turtlehack

roger = turtle.Turtle()

# draw a circle
roger.circle(20)

# random_color() returns a color value, so we put it where we'd normally put a color.
# you should see the 'turtle' chance colors at this point.
roger.color(random_color())

# draw another circle, slightly different in size, and see the different color!
roger.circle(30)
```

## Contributing

`random_color()` is pretty sweet, but there are lots of improvements we can make to the Turtlehack project.  Check out the Issues of the project to see what the organizer has identified as things that need improvement.

## Exercise due Friday

By the end of Friday, particpate in the Turtlehack project in a meaningful way, and post a post showing how you've used the library to make a better Turtle drawing.  Your post should have 1) a screenshot and 2) your code.
