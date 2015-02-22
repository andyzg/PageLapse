function handleRequest(data) {
  console.log(data);
  var screenHeight = $(window).height();
  $("div.hero").animate({
    bottom: screenHeight + "px"
  }, 500, 'swing');
  $("body").css({
    height: screenHeight + "px",
  });
  $("div.footer").css({
    height: "-1000px"
  });
}

$(function() {
  var s = skrollr.init();

  $("div.text").click(function(e) {
    var url = $("input[name=url]").val();
    $.get("/query", { url: url })
      .done(handleRequest);
  });
});
