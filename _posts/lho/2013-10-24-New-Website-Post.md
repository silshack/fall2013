---
layout: post
author: lho
categories: post
title: Leslie's Jekyll Website Post
---

So I didn't have any problems updating my website or adding a website thank goodness!  I think I'm somehow getting progressively better at Github and I'm not a total complete fail at Github Command Line!  WOHO! Anyways, here is my step by step process in creating a new Jekyll website from the command line:

1. So after I installed Jekyll, I then issued this command in the command line: ```jekyll new mysite```. This created my site.

2. After Jekyll created this ```mysite/``` folder, I needed to create a repository to which I can add files and change files on Github.  I used ```git init``` to create a new repository.

3.  I needed to check the status of my repository to make sure I did not commit it by using the command ```git status```. (side note: this git status is super helpful because it has colors in the Git Command Line which helps me automatically know what hasn't been commmitted)

4.  I then committed the additions, using ```git add .``` and then committing using ```git commit -m "Added my blank Jekyll site"``` which also added a commit message.

5. I then did ```jekyll serve --watch``` to see the changes on my local Jekyll server.  

6. I renamed the default branch from ```master``` to ```gh-pages``` by using the command ```git branch -m master gh-pages```.

7.  After I checked the site to make sure it was okay on my local Jekyll server, I then added my new repository as a remote: ```git remote add origin https://github.com/leslieho/mysite``` and then I pushed the changes to the site: ```git push origin gh-pages```

8. After doing all of this, I then updated config.yml file to add the base url information ```baseurl: /mysite``` and updated the index.html with my contact information.

Here's my screenshot: 
<img src="http://i.imgur.com/aXFsHc3.png">

