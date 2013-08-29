---
layout: post
author: gmclendon
categories: howto
title: How to get Jekyll running locally on Ubuntu (and other things to do after setting up VirtualBox)
---

#####DIsclaimer: this worked for me, I hope it works for you I've tested it in a limited fashion on a local VM, but that's it.  


## Virtual Box Extras  
So, you have Ubuntu installed on your brand new VirtualBox and are trying to figure out what to do next.  
The very first thing to do is install VirtualBox Guest utilities that let you do fun things like scroll.

There are two sets of extras and extensions to install, one provided by VirtualBox and another maintained by the community.  
* Download [VirtualBox Extension Pack](http://download.virtualbox.org/virtualbox/4.2.16/Oracle_VM_VirtualBox_Extension_Pack-4.2.16-86992.vbox-extpack) double click the file and VirtualBox will mount it as a CD.
 	*  'Devices>Install Guest Additions' in your running Ubuntu instance will launch an installer
	*  If an installer fails to launch or doesn't run to completion the following will install the additions manually
		* in the terminal (ctrl+alt+t)  
```bash  
cd /media/$USER  
cd VBOX {pres tab to complete}  
sudo ./VBoxLinuxAdditions.run  
```  
		* restart your VirtualBox
* Install the community maintained VirtualBox Guest additions:
	* in the terminal (ctril+alt+t)  
```bash  
sudo apt-get install virtualbox-guest-utils virtualbox-guest-x11    
```  


##Setting up a Jekyll instance  
Ubuntu has an outdated version of Jekyll in its repositories, don't install it. It has a whole host of issues and fails to build most jekyll pages.  
Instead we are going to install Ruby and the Jekyll gem   
```bash
sudo apt-get install ruby1.9.1 ruby1.9.1-dev make build-essential  
export PATH=$PATH:/var/lib/gems/1.9.1  
sudo gem install jekyll  
```  

Now you have jekyll setup, To make it realy useful we need git working too, but that I still don't quite understand.
