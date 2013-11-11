---
title:  Cat and Mouse Game
layout:  post
author:  epeele
categories:  post
---

To change starpusher, I decided to go with something near and dear to my heart:$

```
                 IMAGESDICT = {'uncovered goal': pygame.image.load('RedSelector$
                  'covered goal': pygame.image.load('Selector.png'),
                  'star': pygame.image.load('ball_of_yarn.png'),
                  'corner': pygame.image.load('Wall_Block_Tall.png'),
                  'wall': pygame.image.load('Wood_Block_Tall.png'),
                  'inside floor': pygame.image.load('Plain_Block.png'),
                  'outside floor': pygame.image.load('Grass_Block.png'),
                  'title': pygame.image.load('star_title.png'),
                  'solved': pygame.image.load('star_solved.png'),
'princess': pygame.image.load('princess.png'),
                  'boy': pygame.image.load('boy.png'),
                  'catgirl': pygame.image.load('catgirl.png'),
                  'horngirl': pygame.image.load('horngirl.png'),
                  'pinkgirl': pygame.image.load('pinkgirl.png'),
                  'rock': pygame.image.load('Rock.png'),
                  'short tree': pygame.image.load('Tree_Short.png'),
                  'tall tree': pygame.image.load('Tree_Tall.png'),
                  'ugly tree': pygame.image.load('Tree_Ugly.png'),
                  'cat': pygame.image.load('cat_black.png'),
                  'yarn': pygame.image.load('ball_of_yarn.png')}
```

Along with this, I changed the text at the introduction of the game to reflect $

```
instructionText = ['Help the cat have fun!  Move the arrow keys to push the$
                       'Arrow keys to move, WASD for camera control, P to chang$
                       'Backspace to reset level, Esc to quit.',
                       'N for next level, B to go back a level.']
```

And, I changed the starting demo level by moving the black cat to the bottom of$

```
; Starting demo level:
 ########
##      #
#   .   #
#   $   #
# .$ $. #
####$   #
   #.   #
   #@   ##
   #####

```
I also changed the color of the opening screen from blue to green.

Here are some screenshots showing how everything turned out:

