$(".mm-cat-level-1 .cat-level-title").after("<span class='mob_menu'></span>")
$(".mm-mega-menu .mob_menu").click(function(){$(this).parent('li').toggleClass("open-mob-menu");$(this).toggleClass("mob-menu-open");});
$(".navbar-top-collapse .dropdown > .dropdown-toggle").after("<span class='mob_menu' data-toggle='dropdown' aria-expanded='false'></span>")
$(".navbar-top-collapse .dropdown .mob_menu").click(function(){});$('.counter-portfolio').counterUp({delay:20,time:1000});
$(document).on('mouseenter','header li.mm-mega-menu',function(){
    if($(this).find(".mm-maga-main.mm-mega-cat-level").length>0){
        var $first_tab=$(this).find(".mm-category-level .mm-cat-level-1:eq(0)");
        $first_tab.find(".cat-level-title").addClass("active-li");
        $first_tab.find(".mm-cat-level-2").addClass("menu-active");
    }
});
$(document).on('mouseenter','.mm-cat-level-1',function(){
    var $first_div=$(this).find('.cat-level-title');
    $first_div.addClass("active-li");
    $(this).find('.mm-cat-level-2').addClass("menu-active");
});
$(document).on('mouseleave','.mm-cat-level-1',function(){
    var $first_div=$(this).find('.cat-level-title');
    $first_div.removeClass("active-li");
    $(this).find('.mm-cat-level-2').removeClass("menu-active");
});


jQuery(document).ready(function($){
    // Hide Loader
    $(".hilia-loader").hide();

    $("header .search_open").on("click",function(event){
        $(".h-search").toggleClass("hm-search-open");
        event.stopPropagation();
    });
    $(".h-search").on("click",function(event){event.stopPropagation();});
    $(document).on("click",function(event){$(".h-search").removeClass("hm-search-open");});
    $("header .mobile_toggle_menu").click(function(){$('body').toggleClass("mob-main-nav-open");});
    $(".mm-cat-level-1 .cat-level-title").after("<span class='mob_menu'></span>")
    $(".mm-mega-menu .mob_menu").click(function(){
        $(this).parent('li').toggleClass("open-mob-menu");
        $(this).toggleClass("mob-menu-open");
    });
    $(".navbar-top-collapse .dropdown > .dropdown-toggle").after("<span class='mob_menu' data-toggle='dropdown' aria-expanded='false'></span>")
    $(".navbar-top-collapse .dropdown .mob_menu").click(function(){});
    $('.counter-portfolio').counterUp({delay:20,time:1000});
    $('.counter-blog-template').counterUp({delay:20,time:1000});
    $('.counter-shortcut').counterUp({delay:20,time:1000});
    $('.counter-like').counterUp({delay:20,time:1000});
    $("img.sub-images").click(function(ev){
        ev.preventDefault();ev.stopPropagation();
        $('.product_detail_img').attr('src',this.src)
        ;$('.product_detail_img').parent().parent().attr('src',this.src);
    });
});



