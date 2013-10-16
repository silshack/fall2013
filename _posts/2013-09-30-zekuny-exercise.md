---
title: Exercise
layout: post
author: zekuny
categories: post
---


Exercise codes:

```python

def add_names(list_of_names, file):
  """
  Opens and adds a list of names to the end of a file, each on its own line
  """
  # We open a file in 'a' mode, for appending to it.
  names_file = open(file, 'a')

  # For each line in the list, we print that to the file. 
  # This assumes one file per line.
  for name in list_of_names:
    print >> names_file, name
    print name + " written to file"

  # Close the file so the changes are visible.
  print "The names have been added successfully"
  names_file.close()


# Exercise: make new_names customizible:
new_names = input('Enter a list of names:')

# Exercise: make the file name used here customizible:
file_name = input('Enter a file name:')
add_names(new_names, file_name)
```
