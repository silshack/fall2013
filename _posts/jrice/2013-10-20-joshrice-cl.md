---
layout: post
author: josh
title: How to write a command line post
categories: post
---

After the successful install of Ruby, GH-Pages, and Jekll, I went on to create
a clone of my branch that appears under our username/fall2013 on github.com.
I went ahead and did this earlier in the week and made my first post under
the _posts folder.

I then wanted to put that file in a newly created folder with my username. 
This was already after I had done an initial git clone. I went through and created a folder
for my posts and then created a new post within that folder. I then did a 
```
git pull 
``` 
to update it from the origin. I created the folder via the github website
although I do understand how to create folders and files via the cl.

Once the clone is complete, you should see a fall2013 folder when you 
type the command ```ls```. You should then change into that directory by using ```cd fall2013``` and see a copy of your fall2013 folder from 
gitub.com. 

Typing ```nano thenameofyourpost.md``` will allow you to edit the file within
a command line text editor. Typing control + O writes out the file and now 
we need to use git to make the magic happen. 

1. First we need to type ```git add thenameofyourpost.md``` to add the file
unless it was already created and had previously been committed
2. Then we need to commit by typing ```git commit -m "enter a commit message"
3. The last step is to push your post to the github site. We do this by 
typing ```git push origin gh-pages```. 

Then you go about finishing by opening a pull request like normal! 


