
# Contributor's Guidelines #
Contributors to this repository are students in the fall 2013 section of INLS560 - Programming for Information Professionals at the University of North Carolina - Chapel Hill's SILS program. As such, most commits in this repository will be blog posts pertaining to assignments given in class. 


##### The Golden Rule: #####
Never commit in the Silshack repository. Always do your commits in your own fork and send a pull request to the Silshack repo. 



##### The Other Golden Rule: #####
Never merge your own pull requests. Allow your instructor and other student committers to do it for you.




## Posts ##

This repository uses [Jekyll](http://jekyllrb.com/) on top of [Github Pages](http://pages.github.com/) to function as a class blog. As such, certain Markdown standards are needed in the formatting of posts so that all pages can be served correctly.

* All posts need to be created as markdown files in the `_posts` directory. For more informaiton on the directory structure of a Jekyll blog, [see here](http://jekyllrb.com/docs/structure/).


* In order for Jekyll to properly convert posts to HTML, two things are required. First, the file must be named correctly, using the format `YYYY-MM-DD-title.md`.


* Second, the post must contain a block of [YAML front matter](http://jekyllrb.com/docs/frontmatter/). For the purposes of this site, posts will typically include `layout`, `author` and `categories`. 


* Although Jeykll is also capable of using Textile, this site uses Markdown for consistency and ease of use. For more information, read [Jekyll's documentation](http://jekyllrb.com/docs/posts/) or go straight to the source and read [Daring Fireball's much more helpful markdown documentation](http://daringfireball.net/projects/markdown/).
