

function preloader() {
      $(() => {

          setInterval(() => {
          let p = $('.preloader');

          p.css('opacity', 0);
          setInterval(
              () => p.remove(),
              parseInt(p.css('--duration')) * 500
          );
          }, 500);

      });
    }
preloader();



var navigation = $('#nav-main').okayNav();









