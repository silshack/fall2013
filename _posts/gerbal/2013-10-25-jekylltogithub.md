---
author: gmclendon
title: How to create a Jekyll github blog
layout: post
---

So you want to put up a jekyll blog on github? It's really straightforward. This tutorial assumes you have Git, Ruby, and Jekyll installed and working. 

#Create your site 

First things, first go [make a blank repo](https://github.com/repositories/new) on github. Now leave it alone. 

Open up your terminal, navigate to wherever you want your new site to live and run the following:  

```bash
$ jekyll new sitename #makes a new site
$ cd sitename
$ git init #initiates a local git repository
$ git add . #adds all the local files to the repo
$ git commit -a -m "Initialized repo" #commits additions to new repo
$ git branch -m master gh-pages #renames repo to the gh-pages github looksfor to serve a jekyll page
$ git add remote origin https://github.com/[username]/sitename.git
$ git push origin gh-pages
```

Now you can check to see that your jekyll site exists and works locally by running `jekyll serve` and navigating to [localhost:4000](http://localhost:4000). And you should be able to see a bare bones un-styled page at [username.github.io/sitename](http://username.github.io/sitename).  

Local should look like this:
![local jekyll](http://i.imgur.com/5nt2vH2.png)  
Github should look like this  
![github](http://i.imgur.com/1JeGhsd.png)

#With Style

Default jekyll is looking in all the wrong places for it's stylesheets. This is pretty easy to change.

Edit `_config.yml` to look like so:  

```yaml
name: Your New Jekyll Site
markdown: redcarpet
pygments: true
baseurl: /sitename
```  

Now, `baseurl` is a variable jekyll can see across the whole site by stating `{{"{{site.baseurl"}}}}` in a page. We need to add this variable to everywhere Jekyll is trying to link somewhere else in the site.

Jekyll uses a series of layout templates to generate its pages. These can be found in the `_layouts/` directory. We need to edit `default.html`. Change the following lines:

```html
        <!-- syntax highlighting CSS -->
        <link rel="stylesheet" href="/css/syntax.css">

        <!-- Custom CSS -->
        <link rel="stylesheet" href="/css/main.css">
```

becomes

```html
        <!-- syntax highlighting CSS -->
        <link rel="stylesheet" href="{{"{{site.baseurl"}}}}/css/syntax.css">

        <!-- Custom CSS -->
        <link rel="stylesheet" href="{{"{{site.baseurl"}}}}/css/main.css">
```

and 

```html  
            <h1 class="title"><a href="/">{{ "{{site.name" }}}}</a></h1>
            <a class="extra" href="/">home</a>
```

becomes

```html
            <h1 class="title"><a href="{{"{{site.baseurl"}}}}/">{{ "{{site.name" }}}}</a></h1>
            <a class="extra" href="{{"{{site.baseurl"}}}}/">home</a>
```

Now run `jekyll serve` in jekyll directory and go to [localhost:4000/sitename/](http://127.0.0.1:4000/sitename/) and you should see your jekyll site with all the pretty styles working.

Now commit your changes and push them to github.

```bash
$ git commit -a -m "made everything very pretty"
$ git push origin gh-pages
```

Your [username.github.io/sitename](http://username.github.io/sitename) should now have styles enabled and look rather pretty. 