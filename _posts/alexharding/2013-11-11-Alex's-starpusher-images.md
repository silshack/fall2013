---
layout: post
author: alexharding
published: true
---

#Images!

So I wanted to add some of my own images. I figured changing tiles would be pretty zany, so I decided to make the stars my face, and the player default Batman. I used photoshop's magnet lasso to quickly cut each out of a picture, and pasted them into a new image with the right size (50px/80px) and deleted the background for transparency. I noticed that the images were all saved in the starpusher directory, so I loaded them there as .png files. 

Next I edited the starpusher.py file, and added both to the dictionary containing all the images. I then changed the 'star' to reference myface.png, so instead of having to change every instance in the game, every time it calls for 'star' it instead loads my face. I also added batman as the first character entry, so it would load by default.

![](http://i.imgur.com/xyr0sfg.jpg)

#Final product
![](http://i.imgur.com/srY0n7Y.jpg)
