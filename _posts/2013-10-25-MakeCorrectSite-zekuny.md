---
title: Make correct site
author: zekuny
layout: post
---

## Make correct site
Firstly, we should change the URL in all files to put baseurl in by add

```python
/fall2013
```

like:

```python
/fall2013/**/**
```

Secondly, in the _config.yml file, we should set the baseurl to mysite like: 

```python
baseurl: /mysite
```

Finally, in index.html, we should add 

```python
{{site.baseurl}}
```

in URL to let it populate the site with changed data automatically.


Then, we can modify the default.html or index.html pages to make them look cool.

My site looks like:

![Image](https://pbs.twimg.com/media/BXbmraSCQAA8HLB.png)
