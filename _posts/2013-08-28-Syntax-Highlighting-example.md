---
layout: post
author: danielle
categories: post
---

Here is some example code of Ruby: (It was found [here](https://www.ruby-lang.org/en/))

```ruby
# Ruby knows what you
# mean, even if you
# want to do math on
# an entire Array
cities  = %w[ London
              Oslo
              Paris
              Amsterdam
              Berlin ]
visited = %w[Berlin Oslo]

puts "I still need " +
     "to visit the " +
     "following cities:",
     cities - visited
```
