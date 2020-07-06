/* Please ❤ this if you like it! */


(function($) { "use strict";
	$(function() {
		var header = $(".start-style");
		$(window).scroll(function() {    
			var scroll = $(window).scrollTop();
			if (scroll >= 10) {
				header.removeClass('start-style').addClass("scroll-on");
			} else {
				header.removeClass("scroll-on").addClass('start-style');
			}
		});
	});		
				
	//*HA AAQUIB IT TOOK 7 GOD DAMN MONTHS BUT I FIXED THE DROPDOWNS 
	
	
  })(jQuery);

