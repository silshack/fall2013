---
layout: post
author: kshaffer
categories: post
---

Creating the new Jekyll site from the command-line was fairly painless. The first step was to tell Jekyll to work its magic by issuing the <code>jekkyl new website</code> command. (Note that I named my site 'website' as opposed to 'mysite' on accident here - a testament either to my jitters or aversion to narcissism). The terminal at this point hadn't cussed me out or displayed a giant middle finger, so I figured I was in the clear for this part.

Step two was then to create a new git repository for this website using the <code>git init</code> command. I was initially a bit confused about why this was a necessary step, thinking that since I created the site surely there would be a repo there waiting for me. Only after (admittedly blindly) following the directions, having everything work out, and reflecting on it did it make sense that both these steps were necessary. I was then very relieved to hear that the <code>.gitignore</code> stuff could be skipped, which made the process in general go all the more quickly.

Seeing Jekyll at work with the <code>jekyll serve --watch</code> command was pretty rad. The utility of this was immediately obvious -- you get an additional barrier (for better or worse) between you and the actual repo you're contributing to. This allows you to make sure your changes are worth committing and opening pull requests for and, for me, ensures that you can try new things locally without worrying about breaking things.

All that was left to do at this point was to add our new repo as a remote like this: <code>git remote add origin https://github.com/kylerthecreator/website</code>, and then push the new commits like so: <code>git push origin gh-pages</code>. Bam! The final tweaks to make our site not look completely horrible were to then fiddle with <code>_config.yml</code> file by adding a new variable <code>baseurl: /website</code> (again, keeping in mind that my site is named 'website' in this case). All that was left to do was to embed <code>{{ site.baseurl }}</code> brackets in the links to the layout pages and <em>voila</em>! There's my <a href="http://kylerthecreator.github.io/website>website</a>!

![](http://i.imgur.com/cF3PtGv.png) 
