---
title: Command line post
author: zekuny
layout: post
---

## Post from command line
First, we should make some preparations. I start with cloning my own repository
to my local laptop. Then I change my directory to fall2013. I set the remote url
of the main project as 'upstream' and the url of my own fork as origin.

Here's the codes:

```python

git clone http://github.com/zekuny/fall2013.git
cd fall2013
git remote set-url origin http://github.com/zekuny/fall2013.git
git remote add upstream http://github.com/silshack/fall2013.git
```


Then I open nano and create a new .md file, which is this one. After modifying
it, I save and exit the nano.

![Image](https://pbs.twimg.com/media/BWtd6PfCMAEIf50.png)

Then I check the status, and there's a untracked file which I just created. I a$
it to files to be commited. And then commit the file with message. Finally, I c$
push my new post to Github.

Here's the codes:

```python

git status
git add _posts/2013-10-16-new-zekuny.md
git status
git config --global color.ui true
git status
git commit -m "Added my first command line post"
git status
git push origin gh-pages
```

![Image](https://pbs.twimg.com/media/BWtd95ECEAAm8SK.png)

It now exists in my own repository on Github. Finally, I send a pull request to
merge the new post into the main repository.
