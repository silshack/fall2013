---
author: abrown
layout: post
title: How I made this happen...
---

## Through the command line

List it out:
*cd fal2013 (change directory)
*nano _posts/ashmbrown/nameoffile.md (open text file to update)
*ctrl - o (save the file)
*ctrl - x (leave the file)
*git status (shows me the changes as an untracked file)
*git add _posts/ashmbrown/nameoffile.md (adds file)
*git status (shows that the file has been added - in green, ready to commit)
*git commit -m "message about commit" (this will add a message to commit)

OPEN NEW TERMINAL
*cd fall2013 (change directory)
*jekyll serve --watch (open up the local host)
*(check commit is reading)

BACK TO ORIGINAL TERMINAL
*git push origin gh-pages (push the commit to github)
 
Go to github.com
*Create a pull request 


