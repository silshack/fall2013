---
author: carolinp
layout: post
title: My first command line post 
---

Hi! Hey! Hello!

So here's how I commited to my repository through the command line:
First, I installed Ruby using
 
```
sudo apt-get install ruby ruby-dev rubygems python-dev python-pip
```
Then, I installed Jekyll and GitHub Pages with 
```
sudo gem install github-pages
```
That didn't work, and it turned out I had an older version of Ruby. I tried Elliot's method of installing the new Ruby in class, but that didn't work either. So I just installed
```
sudo gem install jekyll
```
instead, and somehow that seemed to work. 

Then, I opened a new terminal and entered 

```
git clone http://github.com/{your-user-name}/fall2013.git
```
I then changed directories using 'cd fall2013.' 

I did
```
git remote add upstream http://github.com/silshack/fall2013.git
```
to add the original repository, and then typed `git remote -v` to make sure that both remotes were there.
I then made my first post by typing `nano _posts/FILENAME.md` and typed control o to save and control x to exit.
I typed 'git status' to see my new, untracked file, added it using `git add _posts/FILENAME.md`, and then committed it using `git commit -m` 

To preview my new post, I closed out an opened a new terminal, typed 'cd fall 2013,' and then typed 'jekyll serve --watch.' I went to http://localhost:4000/fall2013, but the post wasn't there. Fortunately, when Elliot corrected the url by putting a backslash on the end in class on Wednesday, it worked!

To push my new post to my repository, I opened up a new browser and typed in `git push origin gh-pages`, but I had just updated my repository, so git got really mad at me and told me to do that first. So I had to type `git pull origin gh-pages`, add and commit again, and then push to origin again. But trouble struck yet again! Somehow, the _site folder had gotten copied to my repository on Ubuntu, and when I committed I was too lazy to type the file name and just did `git add -A` and `git commit -a` because I figured that the changes were there for a reason, right? WRONG! This became clear to me when I had to open a pull request for silshack. So I had to delete the files and re-commit them to my repository, and then it was fixed! Gods be praised!  
