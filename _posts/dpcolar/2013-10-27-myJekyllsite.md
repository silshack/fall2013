---
title: My new Jekyll site
layout: post
author: dpcolar
categories: post code
---
Creating a new Jekyll site

To make things a little more interesting, I  upgraded my distro to Salamander this morning: <br>

```
pcolar@aaladm81:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 13.10
Release:	13.10
Codename:	saucy
```

Checking the Jekyll install

```
pcolar@aaladm81:~$ sudo apt-get check jekyll
Reading package lists... Done
Building dependency tree       
Reading state information... Done
```

Create my new site

```

pcolar@aaladm81:~$ jekyll new Jekyll_site
New jekyll site installed in /home/pcolar/Jekyll_site.
pcolar@aaladm81:~$ cd Jekyll_site/
pcolar@aaladm81:~/Jekyll_site$ git init
Initialized empty Git repository in /home/pcolar/Jekyll_site/.git/
pcolar@aaladm81:~/Jekyll_site$ git commit -a -m "New Jekyll empty site"
[master (root-commit) c955e25] New Jekyll empty site
 8 files changed, 314 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 _config.yml
 create mode 100644 _layouts/default.html
 create mode 100644 _layouts/post.html
 create mode 100644 _posts/2013-10-27-welcome-to-jekyll.markdown
 create mode 100755 css/main.css
 create mode 100644 css/syntax.css
 create mode 100644 index.html
 
pcolar@aaladm81:~/Jekyll_site$ 
```

Rename the default master branch to gh-pages

```
pcolar@aaladm81:~/Jekyll_site$ git branch -m master gh-pages
```

Push to the new repo

```
pcolar@aaladm81:~/Jekyll_site$ git push origin gh-pages
Username for 'https://github.com': Pcolar
Password for 'https://Pcolar@github.com': 
Counting objects: 13, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (12/12), done.
Writing objects: 100% (13/13), 3.42 KiB | 0 bytes/s, done.
Total 13 (delta 0), reused 0 (delta 0)
To https://github.com/Pcolar/Jekyll_site
 * [new branch]      gh-pages -> gh-pages
```

![Here is a screen shot of my home page:](http://www.unc.edu/~pcolar/2013-10-27_Jekyll.png)
