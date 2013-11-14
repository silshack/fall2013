---

layout: post
author: jpowell
title: Star Pusher... and Sweets!
---


# Star Pusher... and Sweets!


If you haven't noticed already, I'm a fan of all things cute. So I did a bit of a re-skin of 
the game to look more [Sweet Lolita](http://en.wikipedia.org/wiki/Lolita_fashion#Sweet_Lolita) inspired.


I added and changed some images, changed some fonts...

## Code

```
# Changed bgcolor from BRIGHTBLUE to peach
BGCOLOR = (249, 237, 215)

# Changed textcolor from white to gold
TEXTCOLOR = (214, 192, 42)
# TEXTCOLOR = (255, 215, 215)
```

```
# Changed
    BASICFONT = pygame.font.Font('loliSkin/A_Lolita_Scorned.ttf', 24)

    # A global dict value that will contain all the Pygame
    # Surface objects returned by pygame.image.load().
    IMAGESDICT = {'uncovered goal': pygame.image.load('RedSelector.png'),
                  'covered goal': pygame.image.load('Selector.png'),
                  'star': pygame.image.load('Star.png'),
                  'corner': pygame.image.load('loliSkin/Wall_Block_Tall.png'),
#                  'wall': pygame.image.load('Wood_Block_Tall.png'),
                  'wall': pygame.image.load('loliSkin/walls.png'),
#                  'inside floor': pygame.image.load('Plain_Block.png'),
                  'inside floor': pygame.image.load('Grass_Block.png'),
                  'outside floor': pygame.image.load('Grass_Block.png'),
                  'title': pygame.image.load('loliSkin/star_title.png'),
                  'titlebg': pygame.image.load('loliSkin/bgtitle.png'),
                  'bg': pygame.image.load('loliSkin/bg.png'), # Added backgrounds
                  'solved': pygame.image.load('star_solved.png'),
                  'princess': pygame.image.load('princess.png'),
                  'boy': pygame.image.load('boy.png'),
                  'catgirl': pygame.image.load('catgirl.png'),
                  'horngirl': pygame.image.load('horngirl.png'),
                  'pinkgirl': pygame.image.load('pinkgirl.png'),
                  'rock': pygame.image.load('loliSkin/Rock.png'),
                  'short tree': pygame.image.load('loliSkin/Tree_Short.png'),
                  'tall tree': pygame.image.load('loliSkin/Tree_Tall.png'),
                  'ugly tree': pygame.image.load('Tree_Ugly.png')}
```


```
       # Changed from DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(IMAGESDICT['bg'], IMAGESDICT['bg'].get_rect())
```

## Screenshots

![Game splash]({{ site.baseurl }}/files/jpowell/starpusherSplash.png)
![Sweets!]({{ site.baseurl }}/files/jpowell/sweets.png)
![More sweets...]({{ site.baseurl }}/files/jpowell/moresweets.png)
![EVEN MORE SWEETS]({{ site.baseurl }}/files/jpowell/evenmore.png)
