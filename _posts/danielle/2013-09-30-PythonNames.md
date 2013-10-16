---
layout: post
author: danielle
categories: post
title: Python Naming File
---
This is what I have done so far with the code for the naming file assignment. It is functional.

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

  # Close the file so the changes are visible.
  names_file.close()


# Exercise: make new_names customizible:
new_names = input('Enter a list of names:')

# Exercise: make the file name used here customizible:
# This works as long as the user just types in the text file name without brackets or ', ". 
add_names(new_names, raw_input('Enter a file name:'))
```
