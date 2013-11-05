---
layout: post
author: lgrindheim
title: Jekyll Post Process
categories: post
---

I started creating a Jekyll website a couple of weeks ago while trying to get ahead of things. I started the process by installing Ruby, Ruby Gems and Jekyll, then created the new file structure with the following commands:
```
$sudo apt-get install ruby
$sudo gem install jekyll
$jekyll new jekyllblog
```

I should say that I could have done that. What I actually did was install Ruby, Ruby gems (as well as RDiscount and Pygments) and Jekyll as per the recommendation of Andrew Musnell, a Jekyll apologist. I'll say that the route we took in class was a bit more concise and direct. I also took his recommendations and created the file structure, which Jekyll would have done for me had I used the simple `jekyll new` command. Nevertheless, the file structure is built. I created a config file by typing `nano _config.yml` in the command line and populated the file with the front matter that Jekyll relies on to create a page. I did this with the assistance of [JekyllRB](http://jekyllrb.com), and later Elliott Hauser. Between the two, I have thought a lot about how the front matter and other aspects of Jekyll work. It's been very helpful.

I needed files to occupy the directories I had made earlier (inluding `_layouts`, `_posts`, `_site` and `_includes`). So I changed directories and copied and pasted some html from Musnell to form a default file that Jekyll would refer to when I told it to do so in the front matter. Again, I recommend going with the steps we took in class. I took his advice to experiment with [Twitter Bootstrap](http://getbootstrap.com). I have, but I don't think it was the best use of my time. It has at least allowed me to know there are more resources out there. Note:  I did download some of their CSS files and have put them to use on my site.

Cut to the present. Had I simply empolyed the `jekyll new jekyllblog` command, I would have been ready right out the gate to customize my _config.yml file and push it all to github using my account. This is what I did, but in a more roundabout way. Same as before, when I was ready to add the files I did the following:

```
git status
git add (all my files)
git commit -M"(my message)"
git push origin gh-pages
(enter username)
(enter password)
```

Magically, I could go to [my site](landongrindheim.github.io/jekyllblog) and see what I had done, before doing a single thing on the github site itself.
