function handleRequest(data) {
  console.log(data);
  var screenHeight = $(window).height();
  $("div.hero").animate({
    bottom: screenHeight + "px"
  }, 500);
  $("body").css({
    height: screenHeight + "px",
  });
}

$(function() {
  var s = skrollr.init();

  $("div.text").click(function(e) {
    console.log("CLICKED");
    console.log(e);
    var url = $("input[name=url]").val();
    $.get("/query", { url: url })
      .done(handleRequest);
  });
});
