---
title: Starpusher is now Packer football-pusher
layout: post
author: abrown
---

For hacking starpusher, I mainly messed around with the images in the image dictionaries. Here is what I did:

1) I downloaded the images I wanted from the web (particularly a packer helmet, a football, and a field goal post). I then resized them in GIMP.

2) I added the images to the starpusher folder where all the other images lived. 

3) I opened the starpusher.py folder: `nano starpusher.py`

4) I then just changed the imagesdict.  I didn't add the new images as variables, but rather changed the current variables to be the picture I wanted. This way, everytime the variable occurred, my new image would appear.

5) I also switched the "inside floor" tiles and the "outside floor" tiles so that the inside tiles looked like grass (like a football field).

6) I then saved the file; and checked out my handy work through `python starpusher.py`

Here are my screenshots:

![Starpusher screenshot](https://lh6.googleusercontent.com/-mtDaKycnAkE/UoJt2IN-FPI/AAAAAAAAAN8/BTWMdIjrhYg/w984-h553-no/starpusher_packers.jpg)

![Starpusher screenshot with code](https://lh5.googleusercontent.com/-2afmvTxOud8/UoJt94Jm-SI/AAAAAAAAAN8/mNlNIx410lI/w984-h553-no/starpusher_code.jpg)
