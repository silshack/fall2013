---
title:  Elizabeth's Jekyll How to Post
layout:  post
author:  epeele
categories:  post
---

To make a Jekyll site, the first thing you need to do is open the terminal.  Then, once you have opened the terminal, it might be a good idea to go ahead and run a <code>git pull upstream gh-pages</code> to refresh everything you've done on github so far.  While this may be a new site, it's good to get into the practice so that you don't accidentally create a clone and then can't figure why things won't merge until your very helpful professor has to walk you through the problem.  Not that that happened or anything.

Moving on, to actually build a Jekyll site you will need to type <code>jekyll new {name of your site}</code>.  Then, you need to change the directory you are working in by typing <code>cd {name of your site}</code>.  This will move you into the directory for your new site.  You can check to see what is in there by typing <code>ls</code>. 

Once this is done, you need to make a new git repo.  To do this, type <code>git init</code>.  Since this repo will not have commits, you will make a commit to it now.  Type <code>git add .</code> to add the files and then <code>git commit -m "{insert your own message here}"</code> to commit them.

Then, for a very important step, you are going to want to make sure that you have a .gitignore file that will cause git to ignore your <code>_site/</code> files.  To do this, type <code>nano .gitignore</code> and add <code>_site/</code>.  

To commit this, we need to go through the same process we did before, type <code>git add .gitignore</code> and then <code>git commit -m "Ignore _site/ directory"</code>.  

This is a very important step, so to ensure that you have completed it properly, type <code>git status</code> to check that no <code>_site/</code> files are there.  If there are, you will need to check to see if you had a previous error for why it didn't work, or post a question somewhere and ask what is going on.

Now, in order for your pages to show up online, we're going to rename the default branch from <code>master</code> to <code>gh-pages</code>.  I repeat, it needs to be renamed to <code>gh-pages</code>.  Renaming it to <code>gh-page</code> means you will have to go back and delete it later on.  To do this change, type <code>git branch -m master gh-pages</code>.

Penultimately, you need to go to Github.com and create a new repository by clicking the "new repository" button.  It should be the one that looks like a notebook with a plus sign on that is to the right of your name on the top right part of your screen.  Name the repo the same thing you called your jekyll site.  Please don't check the box that creates a README.

Finally, you can add and push your commits of your repo as a remote by typing <code>git remote add origin https://github.com/{your-username}/mysite</code> and then <code>git push origin gh-pages</code>.   


After all of this, you then need to go to github.com to make changes to the css.

First, go to <code>mysite/index.html</code> and here add in <code>{{ site.baseurl }}/</code> to the line of code that starts with a href=.  The spaces in there make it easier for people to read, so while not 100% necessary, it is good coding practice.  (Thanks for the tip Elliott and Grant!)).  Then, go to <code>_config.yml</code> to add a line that states <code>baseurl:  /{name of your site}</code> underneath the name, markdown, and pygments categories.

From here, you should be able to play with the css and continue growing your own repo.  Have fun!
