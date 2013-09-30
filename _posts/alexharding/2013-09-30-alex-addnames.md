---
layout: post
author: alexharding
published: true
---






#My Code

What follows is my python code which allows the user to add their own list of names and choose a file name to write out to.

```

def add_names(list_of_names, file):
  names_file = open(file, 'a')
  for name in list_of_names:
    print >> names_file, name
  names_file.close()


new_names = input('Type a list of names. ')
file_name = input('Type a file name ')+'.txt'
add_names(new_names,file_name)
print 'This program created '+str(file_name)+' in your home directory.'

```
