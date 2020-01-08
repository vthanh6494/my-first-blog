$(document).ready(function() {
    $(window).load(function(){
        var socialIcons = $('.social-icons').offset().top;
        $(this).scroll(function () {
            if ($(window).scrollTop() >= socialIcons) {
                $('.social-icons').addClass("fixed-icons-bar");
                $('.container').addClass("plus-margin-top");
            } else {
                $('.social-icons').removeClass("fixed-icons-bar");
                $('.container').removeClass("plus-margin-top");
            }
        });
    });
});