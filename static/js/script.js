$(document).ready(function(){
    $(".owl-carousel").owlCarousel({
        loop: true,          // Infinite loop
        margin: 10,         // Space between items
        nav: true,          // Show navigation arrows
        autoplay: true,     // Auto-play enabled
        autoplayTimeout: 3000, // 2 seconds per slide
        responsive:{
            0:{ items: 1 },
            600:{ items: 2 },
            1000:{ items: 5 }
        }
    });
    $( ".owl-prev").html('<i class="fa fa-chevron-left"></i>');
    $( ".owl-next").html('<i class="fa fa-chevron-right"></i>');
});
