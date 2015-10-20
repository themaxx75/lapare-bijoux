/*!
 * Start Bootstrap - Creative Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

(function($) {
    "use strict"; // Start of use strict

    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 50)
        }, 1250, 'easeInOutExpo');
        event.preventDefault();
    });

    // Highlight the top nav as scrolling occurs
    $('body').scrollspy({
        target: '.navbar-fixed-top',
        offset: 51
    })

    // Closes the Responsive Menu on Menu Item Click
    $('.navbar-collapse ul li a').click(function() {
        $('.navbar-toggle:visible').click();
    });

    // Fit Text Plugin for Main Header
    $("h1").fitText(
        1.2, {
            minFontSize: '35px',
            maxFontSize: '65px'
        }
    );

    // Offset for Main Navigation
    $('#mainNav').affix({
        offset: {
            top: 100
        }
    })

    // Initialize WOW.js Scrolling Animations
    new WOW().init();

})(jQuery); // End of use strict

//function carouselNormalization() {
//var items = $('#carousel-example-generic .item'), //grab all slides
//    heights = [], //create empty array to store height values
//    tallest; //create variable to make note of the tallest slide
//
//if (items.length) {
//    function normalizeHeights() {
//        items.each(function() { //add heights to array
//            heights.push($(this).height());
//        });
//        tallest = Math.max.apply(null, heights); //cache largest value
//        items.each(function() {
//            $(this).css('min-height',tallest + 'px');
//        });
//    };
//    normalizeHeights();
//
//    $(window).on('resize orientationchange', function () {
//        tallest = 0, heights.length = 0; //reset vars
//        items.each(function() {
//            $(this).css('min-height','0'); //reset min-height
//        });
//        normalizeHeights(); //run it again
//    });
//}
//}
//    $('document').ready(function() {
//  carouselNormalization();
//});
