---
layout: post
author: carolinp
categories: post 
---

Hey there!
So here's how I setup my Jekyll blog. You can take a look at the real live thing at http://www.carolinp.github.io/mysite

I already had Jekyll installed, so I opened up a new terminal and typed `jekyll new mysite`.
Then, I typed `cd mysite` to get into the folder for the site I just made.
To make a repo of the site on github, I then typed `git init` to make a new repo.
Github saw all the new Jekyll files, so I added them using `git add .` and them committed them with `git commit`.
I then started to make sure that the `_site/` folder was ignored using .gitignore, but apparently that was already taken care of. Awesome!
Then I typed in `jekyll serve --watch` to check out my new site locally in a web browser. It looked pretty good so far, so I proceeded onto putting my new repo on github.com.
I renamed the master branch to gh-pages by typing `git branch -m master gh-pages`
I then logged into my account on github.com and created a new repository by clicking the "New Repository" button in the upper right hand corner of the site (it looks like a little plus sign on a book). I named my shiny new repo mysite, just to make it simple.
I then added the new repo as a remote by typing `git remote add origin https://github.com/USERNAME/mysite`
I pushed all the changes to my new repo with `git push origin gh-pages`
All finished, right? Wrong! The path to the css files was all wrong, so the page looked very sad:
![Pretty, right?](https://lh4.googleusercontent.com/-rPbWyWfoq4s/UmmbBoSsMwI/AAAAAAAAAOI/rdJ9iCOn6GQ/w634-h277-no/sils2.JPG)

We discovered in the next class that it was due to Github using the default baseurl, which broke a lot of the paths. We then had to add `baseurl: /mysite` in the config file and fix the css paths in the default html file in the layouts folder so that `{{site.baseurl}}` was in front of the css folder in the link to the stylesheets (like this: `<link rel="stylesheet" href="{{site.baseurl}}/css/main.css">`). Much better!
![Much better!](https://lh4.googleusercontent.com/--QHxeZMaraE/Umma9WqC_WI/AAAAAAAAAOA/_6MufDYFAiw/w633-h282-no/sils1.JPG)

The hard part was over, but I went back and changed the blog name in the config file, put a tiled background image in the main css as well as changed a couple font colors to make them more readble on the new background. So here's what my blog looks like now:
![It's not much, but I like it.](https://lh6.googleusercontent.com/-LSGcNAk1Q8w/UmqRe81opBI/AAAAAAAAAO4/2vNMoAi21sk/w633-h283-no/sils4.JPG)
