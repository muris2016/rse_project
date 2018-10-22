$(document).ready(function(){
  $('div div a').click(function(){
    $('div a').removeClass("active");
    $(this).addClass("active");
});
});