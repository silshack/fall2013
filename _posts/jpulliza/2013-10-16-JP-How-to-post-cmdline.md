---
layout: post
author: jpulliza
categories: post 
title: How to Post from Command Line
---

This is some clarification on my first post from command line, which can be found [here.](http://silshack.github.io/fall2013/2013/10/14/new-post.html)

There are a few "objects" that you will need to manipulate:

1. Your local Git repository
2. A post formatted in markdown on your local machine.
3. Your GitHub repository
4. The class GitHub repository

First make sure you have set up a git of the SILSHACK repository on your machine. The instructions can be found [here](http://silshack.github.io/fall2013/2013/10/14/forteenth-class.html)

Next create a text file in the '_posts' directory (with the added optional subdirectory with your name)

Open up a terminal and change your directory to where your git is, in this case 'cd fall2013.' Now if you run 'git status' you should see your new file in red. You need to 'git add [file name]', and then 'git commit' that file.

When you commit that file, that is going into your LOCAL repository. You need to push that file to your GitHub repository, so you can through pushing your changes to your GitHub repository (in this case named origin) by entering 'git push origin gh-pages'. You should be prompted for your GitHub username and password.

Now you can run a normal pull request from GitHub.com to merge that into the SILSHACK site.
