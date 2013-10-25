---
layout: post
author: asherman
categories: post
title: Making a Jekyll Site
---

My Jekyll site [My Jekyll site](http://ans729.github.io/mysite/)

![My Jekyll Site](http://farm3.staticflickr.com/2852/10476612455_6642653edd_s.jpg)


To set up a new Jekyll site, open a new terminal and type:
```
jeykll new mysite
```
Replacing ‘mysite’ with whatever you would like to call it.  Then change directories to the new site by typing: 
```
cd mysite
```
Add a git repository by typing:
```
git init
git add .
```
Commit and comment on your commit by typing
```
git commit -m "Added my blank Jekyll site"
```
I think I already had .gitignore, so I didn’t need to add that, but I did need to change the master branch to gh-pages by typing:

```
git branch -m master gh-pages
```
On Github.com – make a new repository called mysite, then go back to the terminal and add a remote by typing:

```
git remote add origin https://github.com/ans729/mysite
```
Push the commit with:

```
git push origin gh-pages
```

From there, I made changes from github.com and not the terminal.  So to make the site look better by adding the CSS, I followed along with Grant in class and added {{site.baseurl}} in _layouts/default.html to:  

```
<!-- syntax highlighting CSS -->
<link rel="stylesheet" href="{{site.baseurl}}/css/syntax.css">

<!-- Custom CSS -->
<link rel="stylesheet" href="{{site.baseurl}}/css/main.css">
```

To edit things like the name, go to _config.yml 

![Change Name](http://farm8.staticflickr.com/7347/10476631946_44d991dc1f_o.jpg)

And to edit the github.com and twitter (I don’t use twitter, so I put in my google+ instead) go to _layouts/default.html 

![Change Links](http://farm4.staticflickr.com/3678/10476631706_f3573253be_o.jpg)
