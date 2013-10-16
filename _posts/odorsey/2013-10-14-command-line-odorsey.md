---
title: Olivia's First Command Line Post
layout: post
author: odorsey
categories: post
---

Yay! This is my first time creating a post from the command line! I realized during this process that using the command line isn't so scary, but actually makes coding a whole lot easier! If you break down each step, it basically involves installing the programs that you need and then moving through the same processes that you would on the interface for Github.

So what I did first was install Ruby on my version of Ubuntu (via VirtualBox). 
To do that, you first go to the "Terminal." on Ubuntu. First, I cloned my version
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

In order to add the blog markdown file that you are currently reading, I typed 
"git add _posts/odorsey/2013-10-14-command-line-odorsey.md." "git status" allowed 
me to see that the post was created and ready to be committed. In order to officially 
move the file to my personal directory (odorsey/fall2013), or commit it, I typed "git 
commit-m "Created command line post."

After this, I created another Terminal and once again moved to the fall2013 directory. 
In order to create my localhost version of the class site, I typed, "jekyll serve --watch."
Once I opened up Firefox, I immediately typed in the URL, "http://localhost:4000/fall2013."
To my disappointment, I received a "Not Found" error. It was not until I typed "http://
localhost: 4000/fall2013/" (thanks to Grant's tip on Google Plus!) that I was able to view my post.

After a few edits, I used "git push origin gh-pages" in order to move my post to my branch!

I'm excited to see how else one can interact with the terminal and localhost to test and develop websites now! Here
is my final result:

![Command Line Screenshot](http://img843.imageshack.us/img843/2772/zq7q.jpg)
