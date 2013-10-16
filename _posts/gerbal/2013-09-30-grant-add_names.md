---
title: Grant completes add_names.py
layout: post
author: gmclendon
categories: post
---  

here's my code:  

```python 
import re

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
def new_names():
    """
    gets a long string, splits it into a list on non alpha-numeric characters
    """
    names = raw_input("What are the names? ")
    split_names = re.split('[\W_]+',names)
    return split_names

# Exercise: make the file name used here customizible:
file_name = raw_input("What is the file name? ")

add_names(new_names(), file_name)  
```  

Added a little bit of functionality. 
