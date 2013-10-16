---
title: Howto&#58; post to the class blog
author: gmclendon
layout: post
---


First things first, I'm using a heavily customized windows shell. It looks different that Ubuntu or other *nix terminals, but behaves exactly the same. Don't let the appearance fool you. If you're curious I'm using the [Gnuwin32](http://gnuwin32.sourceforge.net/) toolset.

## Getting any changes
First thing we are going to do is clone our class blog git repo, add the master repository, and make sure everything is merged into out personal branch.  

```bash
$ git clone https://github.com/[user]/fall2013.git #put your github user name where [user] is
$ cd fall2013
$ git remote add upstream https://github.com/silshack/fall2013.git
$ git pull upstream gh-pages 
# at this stage you may have conflicts. Resolve them by editing the files using nano or another editor.
$ git commit -a -m "merged upstream" #in case any conflicts need to be merged
$ git push origin gh-pages
```

## Creating the post  
Now we're going to make and edit a post. It's pretty simple.  

```bash
$ nano _posts/[user]/[date]-[title].md #replace [user] with your user name, [date] should be formatted "1970-01-31"
```

Now that we're in nano you need to write your post. If you feel the need to include a colon use the '\&#58;' code instead. Jekyll will see a colon in the header as a yaml stuff and will fail to render your post correctly ('\&#58;' shows up as '&#58;'' when your browser renders the page).  
Be sure to format your header correctly:   

```yaml
---
title: Howto&#58; post to the class blog
author: gmclendon
layout: post
---
```  

It should look something like this in nano:  
![picture of nano](http://i.imgur.com/6Y20kW2.png)

Save the file using 'ctrl + o' and 'ctrl + x' to exit.  

Now run 'jekyll serve' and navigate to [http://localhost:4000/fall2013/](http://localhost:4000/fall2013/) and make sure your post looks the way you think it should.

If you don't have Jekyll installed you can get it by running:  

```bash  
$ sudo apt-get install ruby1.9.3  
$ sudo gem install github-pages  
```   


## Putting your post on the blog
Now we need to commit our changes and send them back to github.  

```bash  
$ git add . # adds all files that have changed from the last commit to the next commit
$ git commit -a -m "made an awesome post" # commits the changes and stages them to be shared with other repositories
# git push origin gh-pages # pushes your changes to github
```  

now go to github, open an pull request like so:
![picture of github](http://i.imgur.com/OXLCmPP.png)

Now it's on the commiters to review your post and commit it. 
