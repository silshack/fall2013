---
layout: post
author: kshaffer
categories: post
---

Below is my code for the IO exercise from class today.

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
# Accept keyboard input from user and assign
# to variable new_names.
new_names = input("Enter a list of names: ")

# Exercise: make the file name used here customizible:
# Accept keyboard input from the user and assign
# to variable filename. Then pass new variable filename
# to function add_names as second argument.
filename = input("Enter a file name: ")
add_names(new_names, filename)
```
