---
layout: post
author: jpowell
title: Blog Scraper
---

# I made a blog scraper!



I am researching blogs for my master's paper, and my advisor suggested that I automate the process so that I don't have to go through hundreds of blogs by hand. I thought it was appropriate to craft it in Python using some of the skills we have learned earlier in the semester - particularly what we did for the Input/Output exercise. I figured I'd post it here since A) I used Python to make it and B) our guest today mentioned that learning to automate tasks would be a good takeaway for the course. Code below. It works just fine for me on Ubuntu.

``` python
import urllib2
import time

y = 0
sec = 0
numPosts = 1

for x in range(numPosts):
  print 'Scraping page...'

# Name document
  z = str(y)
  docName = 'blogger' + z + '.html'

# Create new file to save the HTML of the scraped page

  req = urllib2.Request('http://www.blogger.com/next-blog?navBar=true&blogID=1120725995044390317')
  response = urllib2.urlopen(req)
  html = response.read()
  docName = 'blogger' + z + '.html'
  f = open(docName, 'w')
  f.write(html)
  f.close()
  print "\033[1;31m"  + docName + 'created ' + u"\u2764"

# Trim the file to a single blog entry

  file = open(docName, 'r')
  filteredHTML = file.read()

# Find the start and end (start of the next entry) of the first entry on the page

  docStart = filteredHTML.find("<h2 class='date-header'><span>")
  filteredStart = docStart + 22
  filteredStartHTML = filteredHTML[filteredStart:]
  docEnd = filteredStartHTML.find("<h2 class='date-header'><span>")
  docEnd = docEnd + docStart
  filteredHTML = filteredHTML[docStart:docEnd] + '<!----- END POST ------>'

# Check that entry exists

  print "\033[31m" + filteredHTML[:50] + '...'
  
# Append entry to Blogger document

  bloggerDocument = open('bloggerPosts.html', 'a')
  bloggerDocument.write(filteredHTML)
  bloggerDocument.close()

  y += 1
  if (y < numPosts):
    print "\033[0m" 'Wait a minute please? *chu*~'
    time.sleep(60)


print "\033[0m" 'Done!'
```


I'm not entirely sure how legal it is to have these sorts of things, to be honest, but since I'm using it for research and not to actually post any of the content I think I should be safe. I have to go through the IRB soon! But I still wanted to share with you all. I did run into some issues when trying to gather lots of posts one after another, which is why I added the "time sleep" tidbit. That way, the servers don't freak out and yell at me for being a robot.


Resources include

* Active State: [here](http://code.activestate.com/recipes/578101-colours-inside-text-mode-python/)
* silsHack: [here](http://silshack.github.io/fall2013/2013/09/30/eleventh-class-notes.html)
* Python for beginners: [here](http://www.pythonforbeginners.com/python-on-the-web/how-to-use-urllib2-in-python/)
* Python documentation: [here](http://docs.python.org/2/library/time.html#time.sleep)
* FileFormat.info: [here](http://www.fileformat.info/info/unicode/char/2764/index.htm)


Here's what the output looks like for me:

![Scraper screenshot]({{ site.baseurl }}/scraperOutput.png)

