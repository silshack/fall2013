---
layout: post
author: elliott
date: 2013-09-09 7:00am
---

Announcements

* Feedback: G+ not a great place to turn in assignments.  We'll start turning everything in via Github.  Add `draft= true` to your posts if you don't want them to show up under your name.
* Extra Credit Experience: Seeking commiters.  Students who feel comfortable on Github and want commit access.  These people will help me categorize issues, manage milestones, etc.  We'll all eventually be core committers, but these are people who don't mind learning early.  [Email me](mailto:eah13@live.unc.edu).
* Problem reports:  You guys are going a great job in the community, reporting problems and helpping each other.  Bonus points for reporting problems that tripped you up but you solved, along with the solution. 
* Post subdirectories: You can put your posts in a `_posts` subdirectory with your user name if you want.  Helps keep things more organized.  See `_posts/elliott` for an example.

**Quesions?**


## Hands on
We're diving in.  Don't worry about understanding in this first section- focus on getting things to work.

### Hello Turtle
1. Fire up your Ubuntu instance.  There are one or two of you who don't have Ubuntu installed.  Use http://skulpt.org and make sure to contact me if you haven't already. 

2. Open two terminal windows.  You'll have to right click on the Terminal icon to get the second one.  Put them so you can see them both.  In one of them, type command `sudo apt-get install python-tk` and press enter to install the turtle module.

3. Type "python" in one of your terminals and hit enter.  Look at the following code:

```python
{% include program.py %}
```

Type it in your python console, line for line.  You may run into errors.  If you press up you can get to previous lines.  The `for` loop will be trickiest: two spaces in front of those lines!

You should see a window pop up with an arrow (the Turtle) that makes a colored box.  Awesome!

#### Interlude: nano
Typing into the console is fun, but there are faster ways to program.

There is a terminal text editor we'll be using called nano.  Open it in your non-python window by typing "nano" and pressing enter.  Nano is a great little program and is on almost every Linux computer.  From now on, open a browser inside Ubuntu and you can copy and paste these programs into nano to get started.  (you may even have configured the copy/paste between machines function) 

The two nano commands you need to know for now are Ctrl-O to *Output* a file and Ctrl-X to *Exit* the program.  You can also type `nano file.txt` to open file.txt.  Nano will make this file for you if it doesn't exist.  Most of our files will have a `.py` extension, which is idiomatic and turns on syntax highlighing (yay!).

Once you've created and *saved* a new file in your nano terminal, you should be able to run it in the other one.  If you're still in the Python console, type `quit()` or Ctrl-C to get out of it.  Then, type `python edward.py` (if your file's name is edward.py)

### How's this Turtle stuff work?

Once your turtle is drawing a box, try to read what's going on in the code above for understanding.  Then, read the code below that I've commented to help explain what's going on:

```python
{% include program_commented.py %}
```

Check out [the source code to turtle]({{ site.baseurl }}/turtle.html).  Just skim it.  It's well-documented code that you don't have to understand (or even read) to make turtles do fun things.  That's a sign of a good library: easy and somewhat intuitive to use, with good documentation and instructions, and well formed, well commented code.  

### Many Paths to the Top of the Mountain
There are literally infinite ways to make the computer do this exact thing.  Here's one:

```python
{% include program_two.py %}
```

1. Read this code to try to see how it accomplishes the same thing.  

2. Paste it into nano and add comments explaining what's going on.


### Code & Creativity
There are many ways to make this turtle draw boxes, and many names to five him/her.  In fact, you can even make the turtle draw other shapes.

This is the fun part of the class.  Work alone or in groups to make an awesome turtle picture.  Create multiple turtles, perhaps.  Work on colors, or figure out how to get curved lines.  Google and the Web are your friends, but keep track of any sources you use.

**By the end of class (or the day), create a new post with your turtle code, any sources you used, and a screenshot of your turtle drawing.  Bonus points for reflections, links to resources, or etc.  Heck, you could even post a few :)**


