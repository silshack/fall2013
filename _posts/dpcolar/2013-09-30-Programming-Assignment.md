---
title: Programming Assignment - Eleventh Class
layout: post
author: dpcolar
categories: post code
---

``` python

def add_names(list_of_names, file):
  """
  Opens and adds a list of names to the end of a file, each on its own line
  """
  # We open a file in 'a' mode, for appending to it.
  names_file = open(file, 'a')

  # For each line in the list, we print that to the file.
  # This assumes one name per line.
  for name in list_of_names:
    print >> names_file, name
    print "name added: " + name

  # Close the file so the changes are visible.
  print "to file: " + file
  names_file.close()

### Main Code starts Here
new_names = input("enter new names:")

new_file = raw_input("enter the filename to append:")
add_names(new_names, new_file)

```

Results:

>>> python add_names.py <br>
enter new names:['Tim', 'Jill', 'Jeff', 'Pedro', 'Adam']<br>
enter the filename to append:names.txt<br>
name added: Tim<br>
name added: Jill<br>
name added: Jeff<br>
name added: Pedro<br>
name added: Adam<br>
to file: names.txt
