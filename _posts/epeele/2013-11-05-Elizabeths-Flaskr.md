---
title: Elizabeth's Flaskr
layout: post
author: epeele
categories: post
---

So here is my flask site ![Flask](http://www.unc.edu/~epeele/file/flask_shot.png)  But, getting to this point is a longer explanation.

First, I couldn't get my 'about' section to work.  Everytime I tried to view it, I kept getting this ![Debug](http://www.unc.edu/~epeele/file/pic.png)  I looked up this error message, and all the boards said it was because flask couldn't find the about function so it didn't know what it was supposed to be doing.  I couldn't understand since I had done what the instructions said.  However, when I talked to Elliott, he explained that since I had the @app.route at the end of the flaskr.py file that it wasn't reading right.  The last statement needs to be <code>if __name__ == '__main__':  init_db()  app.run()</code> because that corresponds to the beginning tag and the code knows to look for that if statement and read everything in the file and process it.  Since I had my 'about' section underneath this, the program wasn't even reading it.

But, this problem led to a bigger problem when I tried to post the problem code on github.  I kept getting email after email saying 'page build error' and when I ran <code>jekyll serve --watch</code>, I kept getting something about angle brackets or a block.  This is one of the many error messages I received ![Screen](http://www.unc.edu/~epeele/file/screenpage.png)  Elliott posted to the Google Plus page that the way to solve it would be to add  <code>{% raw %}</code> and <code>{% endraw %}</code> tags around my code so that Liquid would quit trying to process the code and just show it like I wanted to.  The finished code looks like the below.

In my templates/layout.html:

```
{% raw %}
<!doctype html>
<title>Flaskr</title>
<link rel=stylesheet type=text/css href="{{url_for('static', filename='style.css')}}">
<div class=page>
  <h1>Flaskr</h1>
  <div class=metanav>
  #Add this line:
  <a href="{{url_for('about')}}">about</a>
  {% if not session.logged_in %}
    <a href="{{ url_for('login') }}">log in</a>
  {% else %}
    <a href="{{ url_for('logout') }}">log out</a>
  {% endif %}
  </div>
  {% for message in get_flashed_messages() %}
    <div class=flash>(( message ))</div>
  {% endfor %}
  {% block body %}  {% endblock %}
</div>
{% endraw %}
```

Overall, this was an informative, if entirely frustrating process.
