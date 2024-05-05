$('#red_header').click(function () {
  const cls = $('header').attr('class')
  if (cls === 'red') { 
    $('header').toggleClass('red green')
   } else if (cls === 'green') {
     $('header').toggleClass('green red')
  }
});
