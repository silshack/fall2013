---
author: elliott
title: "Forteenth Class Notes: Local Class site!"
layout: post
---

## Laptops Down Announcements
* Comments on this assignment?
* Turtlehack showoffs
* Namespaces
* For the most recent turtlehacks, `git pull`

## 	Laptops Up Announcements
* Github check-ins
* G+ & Meetups check-ins

## Local Jekyll

Our class blog is built around a blocing library called [Jekyll](http://jekyllrb.com).  This is what Github uses to make our site, and we've been using Github to preview our changes.  This is simpler than running code locally, but has plenty of limitations.  We're now going to install Jekyll and hack our class site locally.

### Installing ruby (and some other stuff we need)

Install Ruby:
```
sudo apt-get install ruby ruby-dev rubygems python-dev python-pip
```

If you get any errors or 404s, you may need to `sudo apt-get update`, but this can take a while so only do it if you need to.

Install Jekyll and Github-Pages:
```
sudo gem install github-pages
```
If this doesn't work for you, sometimes just installing Jekyll will work instead:
```
sudo gem install jekyll
```
This gem (package of Ruby software) includes Jekyll and several other things needed to make our copy of Jekyll just like Github's.  That way we should see the same errors, etc, that they do.  To verify you've got a copy of Jekyll installed after this, type `which jekyll`.  If you have Jekyll, this will print out a directory location.  If not, it will do nothing- make sure your apt-get command didn't have any errors.

### `git clone` your version of our class website

Open a new Terminal

```
git clone http://github.com/{your-user-name}/fall2013.git
```
*Note: this may not work if you already have a copy of the project in a directory called `fall2013/`.  I so, you can move the existing directory by typing `mv fall23013/ fall2013old/`. `mv` is UNIX for 'move <this> <there>`*

Change directories into the `fall2013/` directory by typing `cd fall 2013`.

Add the main project as a remote called `upstream`:
```
git remote add upstream http://github.com/silshack/fall2013.git
```
Now, when you type `git remote -v`, you should see this:
```
origin	git@github.com:{your-user-name}/fall2013.git (fetch)
origin	git@github.com:{your-user-name}/fall2013.git (push)
upstream	git@github.com:silshack/fall2013.git (fetch)
upstream	git@github.com:silshack/fall2013.git (push)
```

Remember, `upstream` is the conventional name for the master project, while `origin` is the conventional name for your fork of it.  

### Write a post

Jekyll looks for posts in the `_posts/` directory, so just make a post there as normal.  

Type `ls` to see what's in your directory:
```
$ ls
LICENSE.md           _pages               favicon.ico          people.markdown
README.md            _posts               feedback.markdown    schedule.markdown
_config.yml          _site                files                showoffs
_includes            assignments.markdown index.html           syllabus.markdown
_layouts             css                  music.markdown       turtle.markdown
```
You can see the _posts directory is right there.  To make a post, type `nano _posts/2013-10-14-post-title.md`, where 'post-title' is the title of your post.  If you're using a subdirectory, you can insert that after `_posts/` like this: `nano _posts/{your-directory}/2013-10-14-post-title.md`.

Make your post about your first time posting from the command line (if it is) or talk a little about how and why you worked ahead if you've already been active from the command line.

When you're done, type `ctrl-o` to save and `ctrl-x` to exit nano.  

### Add & Commit your post.

Type `git status` to see what's going on.  You should see your new post there listed as an 'untracked file'.  We tell git to add it to the files to be commited by typing `git add _posts/2013-10-14-post-title.md` (replacing that with the actual file name you used).

Type `git status` again and you should see the same file, but now in green, and listed as a change to be committed.  To commit the change, type `git commit -m "Message describing the commit"`, replacing that message with a real one describing what you did (i.e. made a new post).

### Preview your post

In a separate Terminal, Change directories into the `fall2013/` directory by typing `cd fall 2013`.  (you can check your location by typing `pwd`.  This should return `~/fall2013/`.)

Fire up Jekyll by typing `jekyll serve --watch`.  'serve' is a mode of Jekyll that will display your site at http://localhost:4000/fall2013.  '--watch' is a flag that will make it update the site automatically if you make any changes.

Open a web browser and go to http://localhost:4000/fall2013 and you should see a local copy of the website with you post in it!  If you get any errors, there is likely something about your post that is confusing Jekyll.  Instead of the cumbersome process of trying to figure out what Github pages didn't like, we can now do the slightly less cumbersome process of debugging our code locally using error messages.

Once the site is running, make some changes to your post, wait a few seconds, and refresh your browser.  Like magic, the site is changed.  Once you've got it the way you want it, it's ready to get pushed to our main site!

### Push your post to `origin` (your fork of our repo) & open a pull request

You're now ready to push your post to Github.  Do so by typing `git push origin gh-pages`.  If you get any errors, first type `git pull origin gh-pages` to merge in any remote changes then push them back out normally.

Open a pull request by comparing your `gh-pages` branch on github.com with the silshack `gh-pages` branch.  Make sure to note in the pull request or a comment that it's not ready for merging yet- we've got more work to do.

You're done for now.  The exercise below will have you modify, save, add, commit, and push an update to your post.  This new commit with automatically show up on your existing pull request.  You can then comment to indicate it's ready for review.  Please do so before the deadline of midnight tonight..

## Exercise: A post-from-the-command-line post, with screenshots
Your post should explain in your own words what the process of posting or our class blog from the command line.  Bonus points for screenshots and correct code blocking. This is due by the end of the day **Wednesday**.
