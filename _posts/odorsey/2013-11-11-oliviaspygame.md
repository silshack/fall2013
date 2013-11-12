---
layout: post
author: odorsey
categories: post
title: Olivia's Pygame Hack
---
After enduring multiple Virtual Box crashes and the slow process of using Ubuntu on my laptop, I finally added some hacks to the Starpusher game! I removed all of the characters associated with the original game and added in new images in the form of three Avatar the Last Airbender characters. I also replaced the stars with rainbows and changed the default colors of the game.

Here are the lovely characters that I used!

![Aang](http://img440.imageshack.us/img440/2030/m1v.png)
![Katara](http://img706.imageshack.us/img706/3999/u5j9.png)
![Zuko](http://img823.imageshack.us/img823/5390/mc2r.png)

```python
....
BRIGHTBLUE = ( 0, 170, 255)
PURPLE = (128, 0, 128)
BGCOLOR = PURPLE
TEXTCOLOR = WHITE
```

I also changed the instructions of the game slightly:

```python
...
instructionText = ['Help the Avatar the Last Airbender characters push rainbows and save the day!',
                   'Push the rainbows over the marks.']
``` 

As a result, when you start the game, you get this:

![Start game](http://img15.imageshack.us/img15/1852/ixyr.jpg)


```python
...
IMAGESDICT = {.....,
'star' : pygame.image.load('rainbow.png'),
'princess' : pygame.image.load('katara.png'),
'catgirl' : pygame.image.load('aang.png'),
'pinkgirl' : pygame.image.load('zuko.png'),
}
...
```

I kept all of the original name assignments for each image... I can't help but think it's hilarious to think of Zuko as a "pinkgirl"! Anyways, after doing that, I was able to change each character at the press of the "P" button. Here is an image of Aang's character being in use: 

![Character Change](http://img577.imageshack.us/img577/5168/qhcc.jpg)

From here, I think I would find some Avatar the Last Airbender-esque landmarks and things to block the path of that rainbow!



