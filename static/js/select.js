$(function() {
    $(".menu ul").css({display: "none"}); // Opera Fix
    $(".menu li").hover(function(){
        $(this).find('ul:first').css({visibility: "visible",display: "none"}).slideDown("normal");
            },function(){
        $(this).find('ul:first').css({visibility: "hidden"});
    });
});
