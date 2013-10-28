---
categories: post
layout: post
user: jgeer
---

Hey folks, today we're going to create a git website using the command line. We'll keep this down to business

First, we're going to type 'jekyll new mysite' and CD to that site from your command line

You can change 'mysite' to whatever you want, but for ease of understanding you can name it mysite

Below is a screenshot showing you what the home directory will look like

![](http://i.imgur.com/1PwygLk.png)

Now before you do anything else, create a repository on git thats named whatever your site's name is

now, make sure you're CD'd into your site directory on the command line, and type 'git init' then type 'git add'

this will create a git repository and then add the existing files to that git. Now commit your changes by typing
'git commit -m "insert a commit message here" '

Now it's important to change your master branch to gh-pages, at least the name. So type 'git branch -m master gh-pages'

Now you want to connect your command line site to your newly created Git, so type git remote add origin https://github.com/{yourgitsite}/mysite 
 then push your commits to gitHub by typing the following: 'git push origin gh-pages'
 
 Check out http://yourgithubusername.github.io/mysite/ and you should see your github site
 
 Now you'll notice your website looks horrible. You can do this from github or from the command line, I did it from github
 for ease, so navigate to your layouts -> default.html file and add /fall2013 to the beginning of all existing links.
 
 Then go to _config.yml and add 'baseurl: /mysite' to the bottom of the file and your site should look more like this:
 
 ![](http://i.imgur.com/t35DGZR.png)
 
 Congratulations! You've made a jekyll site
