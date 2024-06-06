document.addEventListener("DOMContentLoaded", function () {
    let menuIcon = document.getElementById('menu-icon');
    let navLists = document.getElementById('nav-lists');

    menuIcon.addEventListener('click', () => {
        if (navLists.style.opacity === '1') {
            navLists.style.opacity = '0';
            navLists.style.right = '-100%';
        } else {
            navLists.style.opacity = '1';
            navLists.style.right = '0%';
        }
    });

    // Testimonial-carousel
    $(".testimonial-carousel").owlCarousel({
        loop: true,
        items: 1,
        smartSpeed: 1500,
        margin: 30,
        dots: false,
        nav: true,
        navText: ['<i class="flaticon-left-chevron"></i>','<i class="flaticon-right-chevron"></i>'],
    });

    // Testimonial-carousel-2
    var testOwl2 = $(".testimonial-carousel-2");
    testOwl2.owlCarousel({
        loop: true,
        items: 3,
        smartSpeed: 1500,
        margin: 30,
        dots: false,
        nav: false,
        responsive:{
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    });
    $(".testimonial-carousel-2-controller .carousel-prev-arrow").on("click", function () {
        testOwl2.trigger('prev.owl.carousel', [300]);
    })
    $(".testimonial-carousel-2-controller .carousel-next-arrow").on("click", function () {
        testOwl2.trigger('next.owl.carousel');
    })
    var windowTab = $(window).width();
    if(windowTab < 992) {
        $(".testimonial-carousel-2-controller").appendTo(".testimonial-carousel-2");
    }


    /**
   * Initiate glightbox
   */
    const glightbox = GLightbox({
        selector: '.glightbox'
    });

    /**
 * Animation on scroll function and init
 */
    function aos_init() {
        AOS.init({
            duration: 1000,
            easing: 'ease-in-out',
            once: true,
            mirror: false
        });
    }
    window.addEventListener('load', () => {
        aos_init();
    });

});