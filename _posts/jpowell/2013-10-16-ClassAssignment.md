---
layout: post
author: jpowell
categories: post
title: How to post to the class blog from the command line
---

# How to post to the class blog from the command line

* First, you will need to develop your post locally. Create a new markdown file in the _posts directory. Once you're done editing this file, make sure you save it before moving on to the next step.
* Then, preview your changes locally to make sure they actually work with Github / Jekyll and don't break the site. To do this, try running jekyll server in the background.
```
source /home/jaleesa/.rvm/scripts/rvm
jekyll serve --watch
```

![Everything Works! The screenshot.](http://i947.photobucket.com/albums/ad316/dieschwarzeskobra/buildpostjekyll_zpsf6be7a22.png)

* If everything looks good and your post is showing up with no problems, add your post to the git stage.
* Commit the changes. Make sure you're putting a descriptive message with your commits.
* Push to your own repository.

```
git add $YOURPOST
git commit -m $YOURMESSAGE
git push $YOURREPOSITORY
```

* Create a pull request to have your post reviewed by the committers on the class blog.
