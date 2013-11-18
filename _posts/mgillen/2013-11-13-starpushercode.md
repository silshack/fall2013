---
title:  Chicken Chase
layout:  post
author:  mgillen
categories:  post
---

I did a very simple hack on the Starpusher game. I chose to remodel the game through pictures and colors, specifically Link chasing chickens. Here are my results:

This is the title screen that greets the player. In addition to changing the title picture, I also altered the text a little bit.

![Title](http://i.imgur.com/2mjXsli.png)

This is what gameplay looks like. Rather than stars, we have chickens! But don't pick them up because they may attack...

![Gameplay](http://i.imgur.com/GOOXi2a.png)

Level completed! You're a winner!

![LevelComplete](http://i.imgur.com/1UjvLWx.png)


The background color was modified by looking up the RGB code for green. 

```python
green = (76, 153, 0)
white = (255, 255, 255)
bgcolor = green
textcolor = white
```

The pictures were modified by replacing other pictures with my own. I left the 'titles' of the picture alone so that I wouldn't have to go through the entirety of the code and change every instance. This results in code that isn't really clean, but it was efficient to do. Just think of it as a hack within a hack... Yes.

![Code](http://i.imgur.com/EeJYAQL.png)
