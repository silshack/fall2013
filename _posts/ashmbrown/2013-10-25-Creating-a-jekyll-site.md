---
author: abrown
layout: post
title: Creating a Jekyll Site (and how many times can I misspell Jekyll?)
---

So, I made a list for the command line post, which I have found super useful, so I am going to do the same thing here but try to jazz it up a bit.

Here's how to make a jekyll site (with the assumption it's already installed). Also for the sake of this example, 'ashleysite' is what I named my blog, but it can be whatever name I want my new jekyll site to be called...

### Make a Site

1) `jekyll new ashleysite`
(creates new site)

2) `cd ashleysite`
(change directory into your new site)


### Make a git repository

3) `git init`
(init = initialize, and it makes a new repository that has a clean slate.)

4)`git add .`
(this adds files to your repository)

5)`git commit -m "Added Ashleysite"`

### Make sure you did it right!

6) `git status`
(shows the status of your repository; make sure no `_site/` files are there).

7)`jekyll serve --watch`
( this will make sure the site updates correctly)

### Time for making this site github ready (ps... and this is embarrassing, but I just realized gh-pages stood for sithub pages...wow...lame.)

8)`git branch -m master gh-pages`
(this changes the name of the master branch into a branch name that github will recognize)


### Now it's time for github to enter stage left...

9) Go to [github.com](github.com).

10)Click "New Repository"

11) Name is "ashleysite" (same name as one created in commandline)

### Go back to the terminal and push this bad boy through...

12) `git remote add origin https://github.com/{ashmbrown}/ashleysite`
(adds your jekyll repository to github)

13) `git push origin gh-pages`
(this pushes the commits to github)

### Celebrate! And check out your post...

14) Realize it looks ugly. Shoot.

15) Frown

### Fix it by adding CSS styling

16) In the terminal:` cd ashleysite`
(naviagtes to ashleysite)

17) keep navigating until you get to ashleysite/_layouts/default.html

18) Once that file is open, change it so the following sentences read as follows:

```

<!-- syntax highlighting CSS -->
 <link rel="stylesheet" href="{{ site.baseurl }}/css/syntax.css">

<!-- Custom CSS -->
<link rel="stylesheet" href="{{ site.baseurl }}/css/main.css">

```

19) Check out your work again and see your page magically change... oh wait, no shoot. Still a not so pretty page.

20) Look over what your classmates did and try to figure it out.

21) Realize people have been making changes to their config file.

22) Make the following addition to your config file:
```
baseurl: /ashleysite
```
(helps direct jekyll to your css)

23) Check out your site. It looks like this:
![Ashleysite (original name)](https://lh3.googleusercontent.com/-oPprIU_i_b8/UmsHFGUff7I/AAAAAAAAALY/6Pu3JDSsEvg/w898-h484-no/jekyll_site.jpg)

24) In the words of Ke$ha... "just dance" (happy dance, not sloppy Ke$ha dance)


