---
layout: post
author: erholmes
categories: post
title: Dr.Jekyll and Git.Hub
published: true
---

I'd like to start out by saying that this will be my most boring and straightforward post so far. **collective gasp here**
<br \>That's right! I had no problems making a Github pages Jekyll site from scratch. **happy dance here** <br \>Since I didn't have any problems and this is just a broad strokes description of the process, it probably won't be that helpful to anyone. **kanye shrug here**

Step 1: create Queen Erin's Jekyll site <br \>
I issued a terminal command: ```jekyll new mysite``` Check!

Step 2: create a git repository <br \>
I used the terminal command: ```git init``` to initialize a git repository and used ```git add```and ```git commit``` commands to create the blank Jekyll site. Check!

Step 3: Test to make sure the site is working <br \>
Used terminal command: ```jekyll serve --watch``` and then used my internet browser to go to ```localhost:4000/qerin/``` Check!

Step 4: Push site to Github<br \>
Changed the name of the master branch to gh-pages and added my github.com repository as a remote repository. Check!

Step 5: Make the site look pretty<br \>
Updated the config.yml file to add the base site information ```baseurl: /qerin``` and also updated the links to the css in the layouts/default.html file to point to the base site. Then I updated index.html to add my personal contact information. Check!

Step 6: Revel in the glory of my new website! Check!

![Jekyll Site](http://www.unc.edu/~erholmes/jekyll_screenshot2.png)
