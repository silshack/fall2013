---
author: elliott
layout: post
title: Sixteenth Class Notes
---

## Announcements 
* Github Check-in


## Making a new Jekyll site

With Jekyll installed, type: 

```
jekyll new mysite
```

Jekyll will set up a brand new site in the `mysite/` folder.  

To get there, then type  

```
cd mysite
```

You can `ls` to see what Jekyll did.  

## Making a git repo

To make a new git repo in the site, type: 

```
git init
```

`init` stands for initialize.  This will make a git repo with no commits in it.  Type `git status` to see what the status is; you'll see that all of your files are new files.

Let's make a commit. 

```
# This adds all the files:
git add .

# This commits them:
git commit -m "Added my blank Jekyll site"
```

There are a bunch of files in the `_site/` directory that we want to ignore: they're a write-only dump and we don't need them up on Github.  To do this, type `nano .gitignore` and add the following to the file that comes up: 

```
_site/
```
The `.gitignore` file can be set to ignore all sorts of irrelevant stuff, depending on your project.

We must add and commit these changes:

```
git add .gitignore
git commit -m "Ignore _site/ directory"
```

When you do this, type `git status` to check that no `_site/` files are there.

You could also start up the Jekyll server to see what it looks like: 

```
jekyll serve --watch
```

The `--watch` flag is optional, but makes the site update when you change it.  `jekyll serve` will create the `_site/` directory but you shouldn't see those files in `git status` if you've done the `.gitignore` correctly.

## Getting ready for Github Pages

Github looks for a branch called `gh-pages` to display on the Internet.  We need to rename the default `master` branch to `gh-pages`.  Do that this way:  
 
```
git branch -m master gh-page
```

The `-m` flag "moves" (renames) the existing branch for us.  Nice!

## Creating a Repo on Github.com

Go to Github.com and log in if you're not already.  Create a new repository by clicking the "New Repository" button.  This is most easily accessed from your profile page.

I recommend calling your repo the same thing you called your Jekyll site, for simplicity.  So we'd name ours `mysite`.

Don't check the box that creates a README.

## Pushing to Github.

We can now add our new repo as a remote: 

```
git remote add origin https://github.com/{your-username}/mysite
```

And push our commits 

```
git push origin gh-pages
```

## Exercise Due by Monday

Open an **Issue** in our silshack fall2013 repo with a link to your new Jekyll repo by midnight tonight.
