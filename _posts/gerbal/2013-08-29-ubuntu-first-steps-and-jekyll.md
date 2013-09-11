---
layout: post
author: gmclendon
categories: howto
title: Post install Ubuntu tips & Jekyll setup 
published: false
---

Disclaimer: this worked for me, I hope it works for you. I've only tested it in a limited fashion. Please comment if you have issues or fixes. I'm also a terrible technical writer, so feel free to tell me what I messed up.

##Virtual Box Extras  
So, you have Ubuntu installed on your brand new VirtualBox and are trying to figure out what to do next.  
The very first thing to do is install VirtualBox Guest utilities that let you do fun things like scroll.

There are two sets of extras and extensions to install, one provided by VirtualBox and another maintained by the community.  
* Download [VirtualBox Extension Pack](http://download.virtualbox.org/virtualbox/4.2.16/Oracle_VM_VirtualBox_Extension_Pack-4.2.16-86992.vbox-extpack) double click the file and VirtualBox will mount it as a CD.
 	*  Go to ['Devices>Install Guest Additions'](http://i.imgur.com/qOezy1M.png) in your running VirtualBox menu instance will launch an installer 
	*  If an installer fails to launch or doesn't run to completion the following will install the additions manually
		* in the terminal (ctrl+alt+t)  

```bash  
cd /media/$USER  
cd VBOX {pres tab to complete}  
sudo ./VBoxLinuxAdditions.run  
```

		* restart your VirtualBox
* Installing the Ubuntu VirtualBox Guest additions:
	* in the terminal (ctrl+alt+t)  

```bash  
sudo apt-get install virtualbox-guest-utils  
```    


##Setting up a Jekyll instance  (courtesy of [Michael Chelen](http://michaelchelen.net/articles/install-jekyll-ubuntu-12-10.html))
Ubuntu has an outdated version of Jekyll in its repositories, don't install it. It has a whole host of issues and fails to build most jekyll pages.  
Instead we are going to install jekyll through ruby, this works better.

In the terminal (ctrl+alt+t):
```bash
sudo apt-get install ruby1.9.1 ruby1.9.1-dev make build-essential  
sudo gem install jekyll  
```  

If when you try to run Jekyll you are told 'Command not found' you will need to add Ruby Gems to your $PATH (places linux looks for system wide-commands)  
	In the terminal:
```bash
export PATH=$PATH:/var/lib/gems/1.9.1/bin
```
