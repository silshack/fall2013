---
layout: post
author: elliott
title: Eleventh Class Notes
---

## Announcements 

* Thanks to Kyle for posting a project idea: web scraping/content analysis.  You'll see some of Grant's work on Gutenberg might be useful for the latter part of that.
* Github pages.  http://{your-username}.github.io/fall2013 is different than how Github.com will display markdown snippets.  Check the github.io site to see if it's building right
* Mini-activity: Merge from master into your repository.

Questions?

## Code Review

Let's look at some code.

### Codingbat

Anyone have a codingbat solution that you're particularly proud of?  Let's see it!

### Alex's Extra-curricular Code

A [python script](http://silshack.github.io/fall2013/2013/09/28/alex-batman-python-sql-generator.html) to generate SQL Insert statements for a comic book database.  Very cool!

### Grant's Extra Credit

Grant's [Extra Credit exercise](http://silshack.github.io/fall2013/post/2013/09/25/Grant-extracredit.html), explained by the man himself.

### File I/O

Fire up Ubuntu.  Open up two Terminal windows.

There's a built-in function called `open()` that we can use to deal with files in python.

In one Terminal, create a text file:

```
> nano names.txt

Elliott
George
Sally
```

(In nano, press Ctrl-O to save, Ctrl-X to exit)

We can see what's in that file by typing `cat names.txt`.

```
> cat names.txt
Elliott
George
Sally
>
```

Now let's use the **other** Terminal window.  Fire up python by typing (you guessed it), `python`

```
> python
 [some text will be displayed here]
>>>
```

The `>>>` is the python prompt, letting you know Python is ready to do your bidding.  Let's read in our text file and print it out:

```
# I read in the text file to a variable I chose to call "text_file"
>>> text_file = open('names.txt')
```

This stores the way to get to the file in the text_file variable.  If we want to see what's inside of it, we have to tell Python to read the file contents.

```
# the text_file variable is just a pointer
>>> text_file
<open file 'names.txt', mode 'r' at 0x3564f0>

# but we can also read in the contents of the file
>>> text_file.read()
Elliott
George
Sally
```


### Program time

You'll find the following file [here](https://raw.github.com/silshack/fall2013/gh-pages/_includes/add_names.py).  Visit that link (in Ubuntu) and save it to your home folder (the one containing the Documents, Downloads, Music etc folders).

Complete the two exercises and submit your code by the end of class or midnight.

{% highlight python %}
{% include add_names.py %}
{% endhighlight %}
