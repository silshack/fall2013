---
layout: post
author: odorsey
categories: post
title: My Jekyll Site
---

In order to create a new Jekyll site, first open up a Terminal in Ubuntu. Then type in the following to create a new site:
```
jeykll new sitenamehere
```

After that, go to that directory by typing:
```
cd sitenamehere
```
Then create a new repository for the site and add all of the files associated with the repository:
```
git init
git add .
```

Commit those files
```
git commit -m "Add new Jekyll site"
```

Ignore the _site/ directory
```
nano .gitignore
```

Once in nano, type _site/ so that directory is ignored. Then after saving .gitignore (by typing ctrl+O to save and then ctrl+X to exit)
```
git add . gitignore
git commit -m "Ignore _site"
```

Name the master branch as gh-pages
```
git branch -m master gh-pages
```

Create a new repository and add that repository to origin
```
git remote add origin https://github.com/odorsey/sitenamehere
```
And finally push those commits!
```
git push origin gh-pages
```

My Jekyll site is located [here](http://odorsey.github.io/mysite/)

![My First Jekyll site](http://img201.imageshack.us/img201/7043/sri7.jpg "My First Jekyll Site")
