---
title: Elizabeth's Flaskr
layout: post
author: epeele
categories: post
---

In my flaskr.py

```python

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    init_db()
    app.run()

@app.route('/about')
def about():
    return render_template('about.html')

```

In my templates/layout.html

```python

<!doctype html>
<title>Flaskr</title>
<link rel=stylesheet type=text/css href="((url_for('static', filename='style.css') ))">
<div class=page>
  <h1>Flaskr</h1>
  <div class=metanav>
  #Add this line:
  <a href="(( url_for('about') ))">about</a>
  {% if not session.logged_in %}
    <a href="(( url_for('login') ))">log in</a>
  {% else %}
    <a href="(( url_for('logout') ))">log out</a>
  {% endif %}
  </div>
  {% for message in get_flashed_messages() %}
    <div class=flash>(( message ))</div>
  {% endfor %}
  {% block body %}  {% endblock %}
</div>

```
