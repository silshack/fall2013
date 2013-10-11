---
layout: post
author: odorsey
categories: post
title: In-Class Exercises
---

Here is my result from the in-class exercises today, thanks in part to Leslie's guidance!  

```python
def add_names(list_of_names, file):
  """
  Opens and adds a list of names to the end of file, each on its own line
  """
  # We open a file in 'a' mode, for appending to it.
  names_file =open(file, 'a')
  
  # For each line in the list, we print that to the file.
  # This assumes one file per line. 
  for name in list_of_names:
    print >> names+files, name
    
  # Close the file so the changes are visible.
  names_file.close()
  
# Exercise: make new_names customizible:
new_names= input('Enter a list of names: ')

# Exercise: make the file name used here customizible:
new_file=input('Enter a file: ')
add_names(new_names, new_file)
```
