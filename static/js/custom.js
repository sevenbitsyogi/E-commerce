(function($) {
  "use strict"; // Start of use strict
          
	$('.new-products-area').slick({
		arrows: false,
		infinite: true,
		slidesToShow: 6,
		slidesToScroll: 1,
		prevArrow: '<img class="slick-prev custom-slick-nav" src="images/left-icon.png">',
		nextArrow: '<img class="slick-next custom-slick-nav" src="images/right-icon.png">',
		responsive: [{
			breakpoint: 1024,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 3,
			}
		}, {
			breakpoint: 600,
			settings: {
				slidesToShow: 2,
				slidesToScroll: 2
			}
		}, {
			breakpoint: 575,
			settings: {
				slidesToShow: 2,
				slidesToScroll: 1
			}
		}]
	});

	// <!-- slick-slider -->

		$('#shop-category-section .main-cate-slider').slick({
			arrows: true,
			infinite: true,
			slidesToShow: 5,
			slidesToScroll: 1,
			prevArrow: '<img class="slick-prev custom-slick-nav" src="images/left-icon.png">',
			nextArrow: '<img class="slick-next custom-slick-nav" src="images/right-icon.png">',
			responsive: [{
				breakpoint: 1024,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 3,
				}
			}, {
				breakpoint: 600,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 2
				}
			}, {
				breakpoint: 575,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1
				}
			}]
		});


	// <!-- select2 -->     
	if($('.category-btn').length){
		$('.category-btn').select2({
			minimumResultsForSearch: -1,
			placeholder: "Select Category",
		});
	}
	// <!-- slick-slider -->

	// plus-minus-btn
		$(document).on('click', '.value-control', function() {
		var action = $(this).attr('data-action')
		var target = $(this).attr('data-target')
		var value = parseFloat($('[id="' + target + '"]').val());
		if (action == "plus") {
			value++;
		}
		if (action == "minus") {
			value--;
		}
		$('[id="' + target + '"]').val(value)
	});
	
})(jQuery); // End of use strict