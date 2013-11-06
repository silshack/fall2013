---
layout: post
author: jpulliza
categories: post
title: Jonathan's Flask Guide
---

This will serve as a guide to installing Flask on your local machine to serve up dynamic webpages.

Install Flask: `pip install Flask`

Install Flaskr (a Flask blog example on GitHub): 
`git clone https://github.com/silshack/flaskr.git`
`cd flaskr`
`python flaskr.py`

The program is now looking in your Flaskr directory for files to serve up to your web browser at `http://127.0.0.1:5000/`

The log in is admin and password is default. This can be changed in the file `flaskr.py`

Instead of static pages, Flask uses what they call "routes" to return a page when the user asks for it. We will now create an about page as an example.

Go into templates and create a file called `about.html`

The file will be a mix of HTML and *Jinja* (similar to Liquid) as template for a page.

```html
{% raw %}
{% extends "layout.html" %}
{% block body %}
  <h2>About</h2>
  <p> This is being written between two &ltp&gt tags.</p>
{% endblock %}
{% endraw %}
```

Notice the special characters for '<' and '>' since this is actually HTML between the `<p>` tags.

Now we will add the route to the `flaskr.py` file in the flaskr directory. Copy and paste the below code to go right beneath the last route, which should be logout.

```python
@app.route('/about')
def about():
    return render_template('about.html')
```

Now we add a link in the `layout.html` file found in templates. This goes right after `<div class=metanav>` and before `{% raw %}{% if not session.logged_in %}{% endraw %}`.

`<a href="{{ url_for('about') }}">about</a>`

If everything worked out you should have a new `about` link that should point to a page that looks like this.

![flask about page](https://dl.dropboxusercontent.com/u/4614624/flask_about.png)
