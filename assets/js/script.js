function updateHistory() {
  $("div#sidebar ul li").each(function(i) {
    var color = i % 2 == 0 ? "#F0F0F0" : "rgb(231, 227, 213)";
    $(this).css({
      "background-color": color,
    });
  });
}

function createCommit(commit) {
  var message = $("<span class='commit-message'>" + commit.message + "</span>");
  var hash = $("<span class='commit-hash'>" + commit.hash+ "</span>");
  var url = $("<a href='" + commit.url + "'><span class='commit-url'>See on Github</span></a>");
  var li = $("<li></li>");
  $(li).append(message);
  $(li).append($("<br />"));
  $(li).append(hash);
  $(li).append($("<br />"));
  $(li).append(url);

  var img = $("<img src='/static/screenshots/" + commit.img + "' />");
  $("div.column div.container").html(img);

  $(li).click(function() {
    var img = $("<img src='/static/screenshots/" + commit.img + "' />");
    $("div.column div.container").html(img);
  });
  return li;
}

function initializeDashboard() {
  var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

  socket.on('commit', function(msg) {
    var screenHeight = $(window).height();
    console.log("Receiving a message");
    console.log(msg);

    // $('div.ul-container ul').append("<li class=\"task\">" + msg.data + "</li>");
    $('div.ul-container ul').append(createCommit(msg));

    $("body").css({
      height: screenHeight + "px",
    });
    updateHistory();
  });

  socket.on('done', function(){
      $(".gif").append("<img src=\"../static/my_gif.GIF\">");
      $(".gif").addClass("browser-mockup");
  });

  socket.on('gif', function(msg) {
    var path = msg.url_path;
    alert(path);
  });
}

function changeScreen() {
  var screenHeight = $(window).height();
  $("div.hero").animate({
    bottom: screenHeight + "px"
  }, 500, 'swing', function() {
    $("body").css({
      height: screenHeight + "px",
    });
    $("div.footer").css({
      top: "-1000px"
    });
    $("body div.hero").css({
      display: "none",
    });
    $("div.ul-container").css({
      height: (screenHeight - 50) + "px",
    });
    updateHistory();
  });
}

function handleRequest(data) {
  changeScreen();
  initializeDashboard();
}

$(function() {
  var s = skrollr.init();

  $("div.text").click(function(e) {
    var url = $("input[name=url]").val();
    $.get("/query", { url: url })
      .done(handleRequest);
  });
});


