(function ($) {
    'use strict';

    var browserWindow = $(window);

    // :: 1.0 Preloader Active Code
    browserWindow.on('load', function () {
        $('.preloader').fadeOut('slow', function () {
            $(this).remove();
        });
    });

    // :: 2.0 Nav Active Code
    if ($.fn.classyNav) {
        $('#foodeNav').classyNav();
    }

    // :: 3.0 Sliders Active Code
    if ($.fn.owlCarousel) {
        var welcomeSlide = $('.hero-post-slides');
        var instaSlides = $('.instagram-slides');

        welcomeSlide.owlCarousel({
            items: 5,
            margin: 20,
            loop: true,
            nav: false,
            dots: false,
            autoplay: true,
            center: true,
            autoplayTimeout: 7000,
            smartSpeed: 1000,
            responsive: {
                0: {
                    items: 1
                },
                576: {
                    items: 2
                },
                768: {
                    items: 3
                },
                1200: {
                    items: 5
                }
            }
        });

        instaSlides.owlCarousel({
            items: 6,
            margin: 10,
            loop: true,
            nav: false,
            dots: false,
            autoplay: true,
            autoplayTimeout: 5000,
            smartSpeed: 600,
            responsive: {
                0: {
                    items: 2
                },
                480: {
                    items: 3
                },
                768: {
                    items: 4
                },
                992: {
                    items: 6
                }
            }
        });
    }

    // :: 4.0 ScrollUp Active Code
    if ($.fn.scrollUp) {
        browserWindow.scrollUp({
            scrollSpeed: 1500,
            scrollText: '<i class="fa fa-angle-up"></i>'
        });
    }

    // :: 5.0 CounterUp Active Code
    if ($.fn.counterUp) {
        $('.counter').counterUp({
            delay: 10,
            time: 2000
        });
    }

    // :: 6.0 Sticky Active Code
    if ($.fn.sticky) {
        $(".foode-main-menu").sticky({
            topSpacing: 0
        });
    }

    // :: 7.0 Tooltip Active Code
    if ($.fn.tooltip) {
        $('[data-toggle="tooltip"]').tooltip()
    }

    // :: 8.0 niceScroll Active Code
    if ($.fn.niceScroll) {
        $(".album-all-songs").niceScroll({
            background: "#fff"
        });
    }

    // :: 9.0 ScrollDown Active Code
    $("#scrollDown").on('click', function () {
        $('html, body').animate({
            scrollTop: $("#about").offset().top - 85
        }, 1500);
    });

    // :: 10.0 prevent default a click
    $('a[href="#"]').on('click', function ($) {
        $.preventDefault();
    });

    // :: 11.0 wow Active Code
    if (browserWindow.width() > 767) {
        new WOW().init();
    }

})(jQuery);