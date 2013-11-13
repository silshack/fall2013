---
title: Modify Pygame
author: zekuny
layout: post
---

## Modify Paygame
Firstly, I change the frame rates or other variables at the top:

```python

FPS = 10
WINWIDTH = 1000
WINHEIGHT = 800
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

TILEWIDTH = 60
TILEHEIGHT = 90
TILEFLOORHEIGHT = 50

CAM_MOVE_SPEED = 8

OUTSIDE_DECORATION_PCT = 30

BRIGHTBLUE = (155, 155, 155)
WHITE      = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

OUTSIDE_DECORATION_PCT = 30

BRIGHTBLUE = (155, 155, 155)
WHITE      = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE
```

Secondly, I change the default pictures used in the game.

It looks like:

![Image](https://pbs.twimg.com/media/BY9oTlkCcAACPHD.png)

Also, I make some changes in starPusherLevels.txt, so I can control the layout and difficulty of the game.

It looks like:

![Image](https://pbs.twimg.com/media/BY9oXY-CcAABl2P.png)

![Image](https://pbs.twimg.com/media/BY9oO63CYAAeggs.png)
