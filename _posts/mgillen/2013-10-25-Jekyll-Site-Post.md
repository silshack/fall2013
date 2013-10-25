---
author: mgillen
title: Creating a Jekyll Site through Github
layout: post
---

Getting a Jekyll site created and up is a pretty painless process. 

The first thing to know is that you'll need Ruby, Jekyll and Github-Pages installed, so if you haven't done that, let's do it! To install them, type the following into the command line from Ubuntu:

Ruby
```
sudo apt-get install ruby ruby-dev rubygems python-dev python-pip
```

Github-Pages and Jekll (as a package)
```
sudo gem install github-pages
```

If Jekyll for whatever reason doesn't install with this package, then you can install it by itself using ```jeykll sudo gem install jekyll```

Once all of our languages are installed, we are ready to begin making our site. Go to Github and create a repository. Name it something for your site that you remember and want to keep, such as 'mysite.' Now, time to begin with the actual website!

Type:

```
jekyll new mysite
cd mysite
```

It's time to create a new, blank repository within the site. Type the following code into the terminal:

```
git init
git add .
```

Commit changes and change branches:

```
git commit -m "Added new Jekyll site"
git branch - m master gh-pages
git add remore origin https://github.com/[username]/[sitename].git
git push origin gh-pages
```

If you choose to ignore certain files, you can. This would be done be creating a nano file telling Git to ignore specific things you tell it to. You would then need to specify in your commit again that these files are to be ignored. Continuing...

Your page is going to look kind of ugly at this point... But we can fix that! Jekyll is looking for CSS in all the wrong places on Github (even though things locally are looking nice). First things first, get to `_layouts/default.html`  and add `/fall2013` to all the links. ```html <link rel="stylesheet" href="/css/main.css"> ``` becomes ```html<link rel="stylesheet" href="/fall2013/css/main.css">```. Then, navigate to the ```git _config.yml file``` and add a new variable ```baseurl: /[mysite]``` (where the brackets indicate whatever you named your site). Commit and you're good to go!

![Mysite screenshot](http://i.imgur.com/J5qKA0r.png)
