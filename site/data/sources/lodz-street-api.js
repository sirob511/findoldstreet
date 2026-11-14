
jQuery('.test').on('click', function(){
	alert('OK');
});

jQuery(window).scroll(function () {
	if (jQuery(document).scrollTop() >= 1 ) {
		jQuery('body').addClass('scrolled');
	} else {
		jQuery('body').removeClass('scrolled');
	}
});

jQuery(".vc_tta-tab > a").on("click", function(e) {
	e.preventDefault();
	let getID = $(this).attr('href')
	jQuery("div").hide();
	jQuery(getID).show();
	history.pushState(null, null, getID.replace('#', ''))

});

if( jQuery('#main_slider').length ) {


	let slides = jQuery('.carousel-inner .carousel-item');

	if (jQuery('.carousel-inner .carousel-item').length > 1) {

		jQuery('.carousel-indicators button').on('click', function () {
			selectImg(this.className);
			clearInterval(interval);
			timer()
		});

		let interval;
		let timer = function () {
			interval = setInterval(function () {
				moveImg();
			}, 6000);
		};

		timer();

		function selectImg(className) {


			let q = className;
			q--;

			let oCurPhoto = jQuery('.carousel-inner .carousel-item.active');
			let oNxtPhoto = jQuery('.carousel-inner .carousel-item').eq(q);

			if( oNxtPhoto[0].length ){
				return;
			}

			jQuery('.carousel-indicators button.active').removeClass('active');

			jQuery('.carousel-indicators button.' + className).addClass('active');

			oCurPhoto.addClass('previous').animate({opacity: 0}, 500,
				function () {
					oCurPhoto.removeClass('active');
				});


			oNxtPhoto.css({opacity: 0.8}).addClass('active').animate({opacity: 1.0}, 1000,
				function () {
					oCurPhoto.removeClass('previous');
				});
		}

		function moveImg() {

			let oCurDot = jQuery('.carousel-indicators button.active').removeClass('active');
			let oCurPhoto = jQuery('.carousel-inner .carousel-item.active');
			let oNxtPhoto = oCurPhoto.next();
			let oNxtDot = oCurDot.next();

			if (oNxtPhoto.length == 0) {
				oNxtPhoto = jQuery('.carousel-inner .carousel-item:first');
				oNxtDot = jQuery('.carousel-indicators button:first');
			}

			oNxtDot.addClass('active');

			oCurPhoto.addClass('previous').animate({opacity: 0}, 500,
				function () {
					oCurPhoto.removeClass('active');
				});

			oNxtPhoto.css({opacity: 0.8}).addClass('active').animate({opacity: 1.0}, 1000,
				function () {
					oCurPhoto.removeClass('previous');
				});
		}
	}
}

jQuery('.open_menu').on('click', function (){
	jQuery('body').toggleClass('stop_scroll');
	jQuery(this).toggleClass('close_menu');
	jQuery('ul.main_menu').toggle(100);
	jQuery('.sidebar').toggle(100);
});

jQuery('ul.main_menu li.menu-item-has-children').on('click', function (){
	jQuery(this).toggleClass('opened_li');
	jQuery(this).find('ul').toggle(100);
})

jQuery('.marquee').marquee({
	duration: 30000,
	gap: 50,
	delayBeforeStart: 0,
	direction: 'left',
	duplicated: true,
	pauseOnHover: true,
	startVisible: true
});

jQuery(document).on('click', '.cookie_info button', function (){
	jQuery('.cookie_info').fadeOut(100);
	setCookie('accept_cookies', 1);
});

function setCookie(cname, cvalue, exdays) {
	const d = new Date();
	d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
	let expires = "expires="+d.toUTCString();
	document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}


jQuery('.collapseomatic:not(.colomat-close)').on('click', function (){

	let parent = jQuery(this).parent();

	if( parent.hasClass('accordion') ){

		jQuery(this).addClass('opened');

		parent.find('.collapseomatic:not(.opened)').removeClass('colomat-close colomat-visited');
		parent.find('.collapseomatic:not(.opened)').next().fadeOut(10);

		parent.find('.collapseomatic').removeClass('opened');
	}

});
