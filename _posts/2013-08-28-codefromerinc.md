---
layout: post
author: erincarter
title: Some code from Erin C.
---


<p>Click the button to get a time-based greeting.</p>

<button onclick="myFunction()">Try it</button>

<p id="demo"></p>

'''javascript
<script>
function myFunction()
{
var x="";
var time=new Date().getHours();
if (time<20)
  {
  x="Good day";
  }
else
  {
  x="Good evening";
  }
document.getElementById("demo").innerHTML=x;
}
</script>'''
