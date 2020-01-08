$(document).ready(function() {
    $(window).load(function(){
        var socialIcons = $('.social-icons').offset().top;
        var htmlAdded1  = '<div class="wrap-logo"><a class="added-info" href="/"><img src="/static/images/python-logo.png" alt="python-logo"></img></a><p>Anhcun blog</p></div>';
        var htmltAdded2 = '<div class="social-icons"><a class="cv-icon" href="/resume"><img src="/static/images/cv-icon.png" alt="icon-CV"></a><a href="https://www.facebook.com/akiko.vo94"><i class="fab fa-facebook-f"></i></a><a href="https://www.instagram.com/honganhftu01677/"><i class="fab fa-instagram"></i></a><a href="https://github.com/vthanh6494?tab=repositories"><i class="fab fa-github"></i></a></div>';
        $(this).scroll(function () {
            if ($(window).scrollTop() >= socialIcons) {
                $('.show-sp').addClass("fixed-icons-bar");
                $('.show-sp').html(htmlAdded1+htmltAdded2);
                $('.container').addClass("plus-margin-top");
            } else {
                $('.show-sp').removeClass("fixed-icons-bar");
                $('.container').removeClass("plus-margin-top");
                $('.show-sp').html(htmltAdded2);
            }
        });
    });
});