$(function(){

	var
	  winW = $(window).width(),
		winH = $(window).height(),
		nav = $('#mainnav ul a'),
		curPos = $(this).scrollTop();

	if (winW > 800){
		var headerH =0;
	}
	else{
		var headerH =70;
	}

	$(nav).on('click', function(){
  	var $el = $(this),
		id = $el.attr('href');
 		$('html, body').animate({
   		scrollTop: $(id).offset().top - headerH
 		}, 500);
		if (winW < 800){
			$('#menuWrap').next().slideToggle();
			$('#menuButton').removeClass('close');
		}
 		return false;
	});

	$('.panel').hide();
	$('#menuWrap').toggle(function(){
		$(this).next().slideToggle();
		$('#menuButton').toggleClass('close');
	},
	function(){
		$(this).next().slideToggle();
		$('#menuButton').removeClass('close');
	});

	$('.slider').slick({
		arrows: true,
		slidesToShow:1,
		autoplay: true,
		autoplaySpeed: 4000,
		centerMode: true,
		centerPadding:'100px',
		focusOnPadding: true,
		pauseOnHover: false,
	});
});
