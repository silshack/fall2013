---
author: jgeer
layout: post
title: My first command line post
---

## Here's my explanation of the post from the command line with screenshots

First, you need to clone the git blog repo so you can access, edit and 
push files. To do that, enter the code in the screenshot, but substituting
your username for where I entered "jkgeer".

![screenshot1](http://i.imgur.com/mw7fdOZ.png)

Now you need to access the fall2013 directory. If you type ls from your
command line you should see new files added to your home directory. Now cd
to the fall2013 directory, type ls and look at the files within that directory.
Now, because you want to create/edit a post from the command line, you need to access
the _posts directory, which you would do by typing 'cd _posts'. Once you're there,
type ls and you should see whichever posts were present the last time you forked
the silshack github site to your personal one.

![screenshot2](http://i.imgur.com/sxf94n6.png)

Now, you need to use the Nano text editor to edit an existing post and change it to
suit this assignment. To do this you type nano "exact post file name". So for
instance, I typed "nano 2013-10-14-jkgeer-commandline-post.md". Keep in mind once
you've typed far enough on the file name to distinguish it from all other files
you can press TAB to auto-complete the file title.

![screenshot3](http://i.imgur.com/6vPpB9m.png)

You should see the basic interface of the Nano text editor. Now you're going to 
include your username, the category and the post title. From there, simply edit
the content to include what you need to include, then press Ctrl + O to save
and rename the file to an appropriate name

![screenshot4](http://i.imgur.com/3lPkvp3.png)

At this point you will type 'git status' and see that the file you've just edited
is 'untracked.' So from here, type "git add 'file name here'. Typing git status again
should have the file as green and ready to be committed. So type
"git commit -m "commit message belongs here"

Now you've committed your post, and you need to push it to your github site
So type "git push origin gh-pages" to put it under the gh-pages branch of your
github site. From there you're going to access Github and open a pull request!

Congrats, you're done. 


