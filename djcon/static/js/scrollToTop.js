var ScrollToTop = {
    scroll: function(scrollLink) {
        var complete = false;
        $("html, body").animate(
            { scrollTop: "0" },
            300,
            'swing',
            function(){
                window.location.hash = '';
                $("#masthead .nav").slideDown();
            }
        );
    },
    bindScrollLink: function() {
        if($('#home-link').length < 1){
            $("#masthead .nav").prepend('<li style="display: none" id="home-link"><a href="/">Home</a></li>');
        }
        var scrollLink = $("#home-link");
        scrollLink.live('click', function(e){
            e.preventDefault();
            $("#masthead .nav").slideUp();
            $("body").removeClass('fixed-nav');
            ScrollToTop.scroll(scrollLink);
        });
        ScrollToTop.bindScroll(scrollLink);
    },
    bindScroll: function(scrollLink) {
        var mastheight = $("#masthead").height();
        $(window).scroll($.debounce(200, false,
            function() {
                $('#homepage section').each(function(){                    
                    var section = $(this);
                    if(section.position().top - $(window).scrollTop() <= ($(window).height() / 2)) {
                        section.addClass('selected');
                    } else {
                        section.removeClass('selected');
                    }
                });                
                if($(this).scrollTop() > mastheight){
                    $("body").addClass('fixed-nav');
                } else {
                    $("body").removeClass('fixed-nav');
                }
                var navsection = $('section.selected').last().attr('id');
                $('#masthead .nav a').removeClass('selected');
                $('#masthead .nav a[href*='+navsection+']').addClass('selected');
            })
        );
    },
    bindNavScroll: function() {
        var navheight = $("#masthead .nav").height();
        console.log(navheight);

        $(window).bind('hashchange', function(e){
            e.preventDefault();
            if(window.location.hash.length > 1){
              var target = window.location.hash.replace('page-', '');
                  $target = $(target);
              $('html, body').stop().animate({
                  'scrollTop': $target.offset().top-navheight
              }, 500, 'swing', function () {
                  console.log('hashchange animation - '+target);
              });
            } else {
                ScrollToTop.scroll('#home-link');
            }
        });
        $('#masthead .nav a[href^="/#"]').bind('click.smoothscroll',function (e) {
            e.preventDefault();
            window.location.hash = 'page-'+$(this).attr('href').replace('/#', '');
            if($(this).attr('href').length > 1){
              $("body").addClass('fixed-nav');
            }
        });
    },                
    init: function(){
        console.log('scroll init');
        this.bindNavScroll();
        this.bindScrollLink();
    }
}

