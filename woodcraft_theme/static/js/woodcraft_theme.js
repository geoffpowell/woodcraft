
//hides main navigation dividers when nav item is active or dropdown is hovered over.Without this the divider lines will poke out a little bit.
$(document).ready(function(){
	$(".navbar-nav > li.active").addClass("hide-divider");
	var last_nav_item = $(".navbar-nav > li").last().addClass("last");
	$(".navbar-nav > li").hover(function(){
		if($(this).hasClass("dropdown") 
			&& !($(this).hasClass("last")) 
			&& !($(this).hasClass("active"))) {
			$(this).toggleClass("hide-divider");
		}
	});
	$(last_nav_item).addClass("hide-divider");

	$("#search_link").click(function(){
		$("#search_container").fadeIn().css('display','inline-block');
		$(this).hide();
	});

	$("#search_link_nav").click(function(){
		$("#search_container_nav").fadeToggle();
	});


});

