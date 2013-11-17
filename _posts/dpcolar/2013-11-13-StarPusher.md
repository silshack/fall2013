---
layout: post
author: dpcolar
title: Starpusher Images and Commands
categories: post
---

There are issues with having an iPad emulate a command line and graphical interface.<br>

Running a remote Ubuntu instance requires mapping the interface via VNC.  Some of the keys are just not available - like Escape! <br>
This is where a few code hacks are valuable!  Like changing all K_ESCAPE to K_q  (must be lower case)

I grabbed a few images from the web, resized them with gimp and then refactored the code:<br>

'''
# A global dict value that will contain all the Pygame
    # Surface objects returned by pygame.image.load().
    IMAGESDICT = {'uncovered goal': pygame.image.load('RedSelector.png'),
                  'covered goal': pygame.image.load('Selector.png'),
                  'star': pygame.image.load('Star.png'),
                  'corner': pygame.image.load('Wall_Block_Tall.png'),
                  'wall': pygame.image.load('Wood_Block_Tall.png'),
                  'inside floor': pygame.image.load('bricks1.png'),
                  'outside floor1': pygame.image.load('bricks2.png'),
                  'outside floor2': pygame.image.load('bricks3.png'),
                  'outside floor3': pygame.image.load('bricks4.png'),
                  'outside floor': pygame.image.load('Grass_Block.png'),
                  'title': pygame.image.load('star_title.png'),
                  'solved': pygame.image.load('star_solved.png'),
                  'princess': pygame.image.load('animal.png'),
                  'boy': pygame.image.load('crab.png'),
                  'catgirl': pygame.image.load('catgirl.png'),
                  'horngirl': pygame.image.load('Gorilla.png'),
                  'pinkgirl': pygame.image.load('pinkgirl.png'),
                  'rock': pygame.image.load('Rock.png'),
                  'short tree': pygame.image.load('Tree_Short.png'),
                  'tall tree': pygame.image.load('Tree_Tall.png'),
                  'ugly tree': pygame.image.load('Tree_Ugly.png')}
'''

The dictionary is extensible, but the code code doesn't easily refactor for random images.<br>

'''
# in the level file to the Surface object it represents.
    TILEMAPPING = {'x': IMAGESDICT['corner'],
                   '#': IMAGESDICT['wall'],
                   'o': IMAGESDICT['inside floor'],
                   ' ': IMAGESDICT['outside floor1'],
                   'p': IMAGESDICT['outside floor2'],
                   'q': IMAGESDICT['outside floor3'],
                   'r': IMAGESDICT['outside floor']}
'''

Creating other character maps and changing the starPusherLevels.txt encoding changes up the images.<br>



![image1](http://www.unc.edu/~pcolar/starpusher1.png)


![image2](http://www.unc.edu/~pcolar/starpusher2.png)
