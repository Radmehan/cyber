document.addEventListener("DOMContentLoaded", function () {


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