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