/********************************************************
 *
 * Custom Javascript code for Enkel Bootstrap theme
 * Written by Themelize.me (http://themelize.me)
 *
 *******************************************************/
$(document).ready(function() {

  //flexslider
  $('.flexslider').each(function(i) {
    var currentFlexslider = $(this).attr('id', 'flexslider-'+ i);

    var sliderSettings =  {
      id: 'flexslider-'+ i,
      animation: $(this).data('transition'),
      selector: ".slides > .slide",
      controlNav: true,
      smoothHeight: true,
      start: function(slider) {
        //animate in first slide
        currentFlexslider.find('.slide').eq(1).addClass('animate-in');
      },
      before: function(slider) {
        //pause, animate out currentSlide, play
        currentFlexslider.find('.slide').eq(slider.currentSlide + 1).addClass('animate-out');
      },
      after: function(slider) {
        //remove animate-in & animate-out classes
        currentFlexslider.find('.slide').removeClass('animate-out animate-in');
        currentFlexslider.find('.slide').eq(slider.animatingTo + 1).addClass('animate-in');
      }
    };

    var sliderNav = $(this).data('slidernav');
    if (sliderNav != 'auto') {
      sliderSettings = $.extend({}, sliderSettings, {
        manualControls: sliderNav +' li a',
        controlsContainer: '.flexslider-wrapper'
      });
    }

    $(this).flexslider(sliderSettings);
  });

  //flexslider carousels
  $('.flexslider-carousel').each(function() {
    var carouselSettings =  {
      animation: "slide",
      animationLoop: false,
      selector: ".items > .item",
      itemWidth: $(this).data('item-width'),
      itemMargin: $(this).data('item-margin'),
      move: 1,
      controlNav: typeof $(this).data('item-controls-on') != 'undefined' ? true : false,
      slideshow: false
    };
    $(this).flexslider(carouselSettings);
  });

});