---
title: Olivia's First Command Line Post
layout: post
author: odorsey
categories: post
---

Yay! This is my first time creating a post from the command line! So what I
did first was install Ruby on my version of Ubuntu (via VirtualBox). To do 
that, you first go to the "Terminal." on Ubuntu. First, I cloned my version
of the class website by typing "git clone http://github.com/odorsey/
fall2013.git" in the"Terminal." Next, I moved to that directory by typing "cd
fall2013."

Next, I installed Ruby by typing "sudo apt-get install ruby ruby-dev rubygems 
python-dev python-pip." The installation process took a while to run, but 
after that, I checked to make sure the correct version of Ruby was running.
To do this, type "ruby -v". The version I wanted was, ruby 1.9.3., which is
what installed correctly on my computer. Perfect!

Afterwards, I installed Jekyll, the library that builds up the GitHub site for
my class blog, Silshack. To install Jekyll, I typed "sudo gem install github
-pages". Once that process was complete, I checked to see if it actually 
installed by typing "which jekyll" to see if it would display my directory. It
did.

In a new terminal window, I moved to the directory that I had cloned earlier,
odorsey/fall2013. To do this, I typed "cd fall2013." After that, I typed "git
remote -v" to make sure that my "origin" and "upstream" urls were correct. 
They were. 

Next, I typed "nano _posts/odorsey/2013-10-14-command-line-odorsey.md" to
create the pst that you are currently reading! This brought me to the nano 
editor, which allows me to write in markdown and save a file to be pushed
later. I pressed "ctrl + O" to save this file.
