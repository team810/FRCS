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
		
	//Animation
	
	$(document).ready(function() {
		$('body.hero-anime').removeClass('hero-anime');
	});

	//Menu On Hover
		
	$('body').on('mouseenter mouseleave','.nav-item',function(e){
			if ($(window).width() > 750) {
				var _d=$(e.target).closest('.nav-item');_d.addClass('show');
				setTimeout(function(){
				_d[_d.is(':hover')?'addClass':'removeClass']('show');
				},1);
			}
	});	
	
	
  })(jQuery);

  window.onload = async function changeComp(){
    var value = $("#teamNumber option:selected").text();      
    $(document).ready(function () {
    $.get("https://www.thebluealliance.com/api/v3/events/2020/simple",{"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data) {
    var jObject = (data);
    for(var i = 0; i<300; i++){
    var comp = jObject[i];
    teamsR.forEach(function(name){
    var option = "<option value='" + name + "'>" + name + "</option>"
    document.getElementById('teamNumber').innerHTML += option;
    });
};
});
});
}

