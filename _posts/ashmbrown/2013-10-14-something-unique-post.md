---
author: abrown
layout: post
title: How I made this happen...
---

## Through the command line

List it out:

1.cd fall2013 (change directory)

2.nano _posts/ashmbrown/nameoffile.md (open text file to update)

3.ctrl - o (save the file)

4.ctrl - x (leave the file)

5.git status (shows me the changes as an untracked file)

6.git add _posts/ashmbrown/nameoffile.md (adds file)

7.git status (shows that the file has been added - in green, ready to commit)

8.git commit -m "message about commit" (this will add a message to commit)

OPEN NEW TERMINAL

9.cd fall2013 (change directory)

10.jekyll serve --watch (open up the local host)

11.(check commit is reading)

BACK TO ORIGINAL TERMINAL

12.git push origin gh-pages (push the commit to github)
 
Go to github.com

13.Create a pull request 


