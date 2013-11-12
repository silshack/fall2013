---
author: danielle
layout: post
title: My First Command Line Post

---
## How to post from your terminal to the class site:

Here are the steps you need to perform in order to post from the command line. 

- Install Jekyll and Github-pages
- Make sure you are running ruby 1.9
- Clone your version of the class website
- Make sure origin is your version of the class site & upstream is the actual class website  
- Create your post
- Add, commit, & view the post locally
- Push to origin & open pull request

I am going to provide further information on the steps I had the most trouble with.

## Checking to make sure you are running the correct version of ruby

```
ruby -v
```
If the result in your terminal is not 1.9 then you will need to change to that version manually by typing in:

```
sudo update-alternatives --config ruby
```
Follow the instructions provided to switch to the 1.9 version of ruby.

![This is my screen shot](http://i.imgur.com/YrdEr9K.png)


## After creating the post 

Need to make sure you are in the right directory when creating your post. 
You can find where you are by typing:

```
pwd

```

Then type:

```
cd #The path where you want to be

```
This will allow you to change around in your directories. 


Once your post is written and saved.

You can type this:

```
git status

#This should show the changes made in red

git add #Name of post here

git status

#Changes should now show up in green

git commit -m "Message about your commit here"

```

Then you can view your creation locally by typing this in your terminal:

```
jekyll serve --watch

```
This will some times come up with errors for me. I wait a little bit and make sure that my post is correct in markdown. Then I try it again.
Also make sure you are in the right directory for this as well: /fall2013/
It has worked for me around the second or third attempt, even if I didn't need to change anything in my post.

Open your browser and type in this address: http://localhost:4000/fall2013/

If it shows up and looks right, then it is ready to be pushed to the origin, which is your version of the class site on github.

```
git push origin gh-pages

```
Then you go to the github site and create a pull request for your commit.

That's it!
