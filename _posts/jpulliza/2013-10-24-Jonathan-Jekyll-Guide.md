---
layout: post
author: jpulliza
categories: post
---

This will serve as a guide to installing Jekyll on your local machine for the purpose of a GitHub hosted site.

Update your apps: `sudo apt-get update`

Install Ruby: `sudo apt-get install ruby ruby-dev rubygems python-dev python-pip`

Install GitHub Pages: `sudo gem install github-pages`

Now we can create a site, so let's name ours "mysite"

`jekyll new mysite`

This will set up a folder with a couple of folders and files within it.

![mysite Folders](https://dl.dropboxusercontent.com/u/4614624/mysite_folders.png)

Before we set up this folder as a Git, we are going to make some changes to the Jekyll configuration so that everything gels. 

`cd mysite` and `nano _config.yml` Add `baseurl: /mysite` to the bottom of that file. Now Ctrl+O to save, and Ctrl+X to exit.

What we did there was create a variable "baseurl" which we can refer to in other files Jekyll uses to build our site.

Now we can add `{{site.baseurl}}` to the one spot in `index.html` file and to the four spots in `_layout/default.html` files so that the references aren't broken. I did this using `nano index.html` and `nano _layouts/default.html`

The change in `index.html` makes sure your posts are linked properly on your homepage as `mysite/[whatever the name of your post is]`
![index](https://dl.dropboxusercontent.com/u/4614624/index.png)

The changes in `_layouts/default.html` makes sure the CSS is linked to the proper file in your `mysite` directory. 
![_layout/default](https://dl.dropboxusercontent.com/u/4614624/layout_default.png)

So, now we have a properly set up Jekyll site that can run locally. To see if it works, make sure you are in the `mysite` directory and type in terminal `jekyll serve --watch`. Now point your browser to `localhost:4000/mysite` and you should see a site ready to go.

![Local Jekyll Site](https://dl.dropboxusercontent.com/u/4614624/jekyll_local.png)

Awesome sauce. So now I would recommend creating a repository on GitHub called `mysite` to point the Git we will create to. *DON'T CHECK CREATE A README.*

Once that is complete, now get back into terminal and make sure you are in the `mysite` directory. Type in `git init`, which will create a Git for that repository, and then `git add .` which will add all of the files in the repository to the Git.

Now we want to commit these files, so we type in `git commit -m "Added Jekyll Site`. 

Before we push this Git to GitHub, we want to rename our master branch `gh-pages` so GitHub knows we want them to host this as a site. `git branch -m master gh-pages`

Now we can add our GitHub location as a remote (which we will by convention name origin) by `git remote add origin https://github.com/{your-username}/mysite` and then push our commits to GitHub through `git push origin gh-pages`

Once complete, there should be a site at `http://[your username].github.io/mysite/` that looks and acts exactly like your local site.

Now feel free to have fun with the CSS of the site and with creating variables in that `_config.yml` file to use in your posts and in the site layouts. 
