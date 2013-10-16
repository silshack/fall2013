---
layout: post
author: dpcolar
categories: post
published: True
---

* This is my solution to the List2-Sum67 problem:

``` python

def sum67(nums):
  found_6 = False
  sum = 0
  ### Traverse the array with a for loop
  for i in range(len(nums)):
    ## Make flag true when we find a '6'
    if nums[i] == 6:
      found_6 = True
      ### Continue jumps out of the line code to the next pass of the for loop
      continue
      
    ### If we have already found a '6', we are looking for a 7 before resuming summation  
    if found_6: 
      if nums[i] <> 7:
        continue
      else:
        ### A '7' is found, so we turn off the flag and resume summation at the next pass
        found_6 = False
        continue
        
    ### The code never gets here unless we are NOT between 6...7    
    sum += nums[i]
  return sum
  
```

* Post questions and I'll respond!
