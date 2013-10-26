---
title: If you build it, your ghost daddy won't play baseball in your cornfield, but you will have a webpage.
author: smantooth
layout: post
categories: post
---

#Pre-steps: Setting up on github

Before you start make sure you have Ruby and Jekyll on your machine.  You'll also need a github account.  
Go ahead and set up a new repo by selecting the 'Repositories' tab on your profile then clicking the green 'New' button.  Pick an awesome name for your repo/future site (I'm going with 'doogie').  Don't check the 'Initialize this repositroy with a README' and then click the 'Create repository' button.


#Creating your site

Open up Terminal.  Type `jekyll new doogie` (sub doogie with your site name).  This will create a new folder with all the default site files.  `cd doogie` and then type `ls` to see your new site files.


#Getting your site onto github

So you've got a site on your machine. Now we've got to push the site to github.

`git init` will start a local git repo
`git add .` adds all the local files to the repository we just opened
`git commit -m "Added new doogie site" `  Commits your files--means their ready to push
`git branch -m master gh-pages`  Github always looks for a branch called gh-pages.  This step renames our branch so Github will display it.
`git add remote origin https://github.com/{your_username}/doogie.git` tells your computer where on the internet your site should be sent to 
`git push origin gh-pages` pushes you local site to Github
Finally, `jekyll serve --watch` allows you to view a copy of your site if you go to localhost:4000/doogie/.


#Fix that funky .yml

If you've looked at the css files for your site, you might have noticed that they don't match your current site.  That's because your site isn't looking at that file yet.
Can we fix it?  Yes, we can!

You need to find the `_config.yml` in your local directories.  Then `nano _config.yml`.
You need to add `baseurl: /doogie` to this file and save.  This will get jekyll to look in the correct place for the stylesheet it applies to templates.

Run the same `git add .` and `git commit -m "Added baseurl to config"` we ran before.

And once again, `jekyll serve`.  Check your local version again. 

Now whatever changes you make to your css files should apply to your jekyll site.

Here's a simple example:

![doogie is a very simple site](http://imageshack.us/a/img822/3310/51fi.png)
