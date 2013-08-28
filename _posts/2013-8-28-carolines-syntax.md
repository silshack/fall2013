---
layout: post
author: carolinp
categories: post 
---
```javascript
$(document).ready(function() {
			
 			$('dl').toggle();
			$('h2').bind('click', function(event) {
				event.preventDefault();
				$(this).next('dl').slideToggle(500, function() {
					$('.video-bg-controls').videobackground('resize');
				});
			});
			$('body').prepend('<div class="video-background hide-on-phones hide-on-tablets"></div>');
			$('.video-background').videobackground({
				videoSource: ['http://livinggalapagos.org/media/uploads/background-video/h264/cover.m4v',
					'http://livinggalapagos.org/media/uploads/background-video/ogg/cover.ogg'], 
				controlPosition: '.video-background',
				poster: 'http://livinggalapagos.org/media/uploads/background-video/jpg/cover.jpg',
				loop: 'true',  
				resize: 'true',
				loadedCallback: function() {
					$(this).videobackground('mute', {controlPosition: '.video-background'});
				}
			});
			
			buildMenu()
		});
```
