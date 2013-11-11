---
layout: post
author: dpcolar
title: My Flaskr is almost empty
categories: post
---

Flaskr didn't pose any significant issues, for which I am grateful.  

My Ubuntu instance is a VM running on the iMac in my office.  In class and from home, I remote into the instance via ssh or VNC.
There are a number od steps to get there:  
1) connect via the VPN
2) ssh -XC to the instance
3) run flaskr in the background - (so I don't need to open another window) via 'nohup python flaskr.py &'

tonight I got an error: 
```  
socket.error: [Errno 98] Address already in use
```

Let's troubleshoot:
```
$ sudo netstat -ap | grep 5000
[sudo] password for pcolar: 
tcp        0      0 localhost:5000          *:*                     LISTEN      21798/python
```

Oops, my detached process was still running from Monday.
```
sudo kill 21798
```
the 'sudo' was not strictly needed, since the process was running under my ID.

OK, back to the assignment!

![tired of loren ipsum...](http://www.unc.edu/~pcolar/Flask_1.png)


![So I filled with the madman and the whale instead](http://www.unc.edu/~pcolar/Flask_2.png)
