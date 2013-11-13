---
author: gmclendon
title: Bulk filters in Gimp (and Starpusher)
layout: post
---

Intrigued by the prospect of scripting GIMP from the commandline I decided to see if I could figure out how to apply filters in a batch to a whole bunch of images. And I did.  
And the results are terrifying.  

![](http://i.imgur.com/KOFqFen.png)  

###Code and Things
So Gimp uses a Scheme scripting language called ScriptFu. It's a quite a bit different from Python and a bit lower level. The script I got working is based on [this tutorial](http://chrisspeck.com/2011/02/batch-application-of-filters-in-gimp-to-make-many-old-photos/).  

There were some issues with transparency and stuff so it took a bit of experimenting to get it to work. And I don't understand ScriptFu's syntax very well, so there's that. Anyway, here's the code:

```scheme
(define (bulk-filter pattern)
(let* ((filelist (cadr (file-glob pattern 1))))
    (while (not (null? filelist))
        (let* ((filename (car filelist))
            (image (car (gimp-file-load RUN-NONINTERACTIVE filename filename)))
            (drawable (car (gimp-image-get-active-layer image))))
            (plug-in-glasstile 1 image drawable 20 20)
            (set! drawable (car (gimp-image-get-active-drawable image)))
            (gimp-file-save RUN-NONINTERACTIVE image drawable filename filename)
            (gimp-image-delete image))
(set! filelist (cdr filelist)))))
```

Save it as `scriptname.scm` in `~/.gimp-2.8/scripts`. The file name doesn't really matter. 

To run the script, navigate into the folder you want to effect in the terminal then run the following command:  

```bash
$ gimp -i -b "(bulk-filter \"*.png\")" -b "(gimp-quit 0)"
```

Be sure your images are backed up somewhere (or, like we are doing, in a git repo that can be `git reset --hard` when things are ugly).  

#### Modifying the script  
The line of code that does the magic is:  

```scheme
(plug-in-glasstile 1 image drawable 20 20)  
```  

You can modify it to take almost any GIMP filter (though bugs may result). You can find the code for more filters by running the Script Fu console in GIMP:

![](http://i.imgur.com/60RYANK.png)

Clicking on `Browse`  
![](http://i.imgur.com/wgYZoJ9.png)

Searching for the name of a filter
![](http://i.imgur.com/lLu34rl.png)

Note on the right hand side of the window the parameters.The best way to figure out what the variables should be is to run the filter in GIMP on a trial image and see what variable values it suggests.

For reference `INT32` parameters are Boolean values (1 or 0) and `FLOAT` are numbers. Image and Drawable are already set by the script.   

So to use the cubism plugin I change the code to say:   

```scheme  
(plug-in-cubism 1 image drawable 10 2.5 1)
```    

Producing:   
![](http://i.imgur.com/ZQJmvTu.png)  



If you want to do more complicated batch file processing in GIMP I would recommend the [BIMP Batch Image Manipulation Plugin](http://registry.gimp.org/node/26259). It does all of the heavy lifting for you and isn't nearly as finicky.



