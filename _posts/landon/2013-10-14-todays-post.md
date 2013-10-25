---
layout: post
author: lgrindheim
title: my first command line post
---

##My First Command Line Post

**Hello, World!

The more challenging, and at this point, less intuitive, portion of this process is working with git from the command line. First, I made a clone of my branch that appears on github.com.

```

git clone http://github.com/landongrindheim/fall2013.git

```

The title and subtitle above were the content of the post that was my first artifact made purely on the command line. Fancy. After cloning the fall2013 repository I opened the repository using the `cd` command. I then created the post with Ubuntu's text editor by typing `nano 2013-10-14-todays-post.md`.

After saving the file I checked its status using `git status`. I saw that my recent was hanging out in limbo so I typed `git add 2013-10-14-todays-post.md`. I check on the posts status and saw that it was ready to be sent to github. `git commit -m"something or other"` allowed me to do so. I went to github.com and sure enough, it was there in my repository. Pretty cool. I'll do the same for these changes. First, I better take a screenshot, so I can complete this mother.


![first command line post](http://landonandjana.files.wordpress.com/2013/10/first-command-line.png?w=500&h=375) 

Here I thought I was done, but I was not. I looked at my view of the course blog and couldn't see the changes that I had made. I couldn't figure out why until I read Jaleesa's post. I had forgotten to `git push` my repository. My classmates offer the solution again.

One more change, to make this tedious, unedited post even more tedious. I was having trouble pushing my changes to github when I looked at Ashley's post. I had forgotten to push to `origin gh-pages`. I had to pull in some unrelated changes I had made on github before I could push this file, but that was quickly done.
