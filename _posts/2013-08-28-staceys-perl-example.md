---
title: Hester Prynne's Daughter was creepy
layout: post
author: smantooth
categories: post
---

```perl
$count = 0;
while (<stdin>) {
    @w = split;
    $count++;
    for ($i=0; $i<=$#w; $i++) {
	$s[$i] += $w[$i];
    }
}

for ($i=0; $i<=$#w; $i++) {
    print $s[$i]/$count, "\t";
}

print "\n";
```
