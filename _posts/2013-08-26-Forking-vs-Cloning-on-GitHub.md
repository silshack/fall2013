---
layout: post
author: mbaxter
categories: post
published: false
---
#Forking vs. Cloning on GitHub - What's the difference?#
First off, **forking** is a vocabulary term that is unique to GitHub.

As best as I can understand it, based on the sources I was able to find, "forking" 
is different from "cloning" based on where the 'copy' of the repository lives.

If you **clone** a repository, it means that you're making a copy of it and storing 
it on your personal computer's hard drive, and therefore if you work on a piece 
of the repository and want to submit a change (aka make a pull request), 
you have to upload the edited file back onto the GitHub server.

If you **fork** a repository, though, it means that you make a copy that lives in your user account on 
the GitHub server (so no time or data is lost between downloading and uploading the repository 
between your computer and GitHub). It lives on the GitHub server, 
which makes it easier to pull back into the original repository/webpage code after you make edits to the code.

This is different from making **branches** in a workflow. Branches are changes you make within a repository, so
in my understanding a branch is similar to an entry in a workflow log. For example, Branch 1 is one change/set of changes you've
within a repository, Branch 2 is yet another change you've made, etc. You then create a pull request to have *your* repository
merged with the *original* repository, which would apply the changes you made to the original.
<br></br>
##My Original Question##
My main reason for asking why it was called 
"forking" instead of "cloning" or "copying:" From the new user's 
standpoint, "forking" something doesn't really 
denote what the action accomplishes. 
Compare it to another feature on this website, 
"follow." You can 'follow' people on GitHub, which means 
you get updates and notices on their activities. 
This makes sense - the vocab and its definition are 
related in an obvious way. It's not the same with "fork" (at least, at first glance).
<br></br>
###Sources###
[http://blogs.atlassian.com/2013/05/git-branching-and-forking-in-the-enterprise-why-fork/](http://blogs.atlassian.com/2013/05/git-branching-and-forking-in-the-enterprise-why-fork/)
[http://stackoverflow.com/questions/3329943/git-branch-fork-fetch-merge-rebase-and-clone-what-are-the-differences](http://stackoverflow.com/questions/3329943/git-branch-fork-fetch-merge-rebase-and-clone-what-are-the-differences)
[http://www.youtube.com/watch?v=_jGUFpWYm60](http://www.youtube.com/watch?v=_jGUFpWYm60)
[http://www-cs-students.stanford.edu/~blynn/gitmagic/ch03.html#_forking_a_project](http://www-cs-students.stanford.edu/~blynn/gitmagic/ch03.html#_forking_a_project)
[http://stackoverflow.com/questions/6286571/git-fork-is-git-clone?rq=1](http://stackoverflow.com/questions/6286571/git-fork-is-git-clone?rq=1)
