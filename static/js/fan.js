var initialize = function(){

var responseNum = 0;
var i =0;

$('.text').click(function(){
    $('body').append("<ul class=\"browser-mockup ipad list\"><li><span class=\"commits\">Commits incorporated</span></li><br></ul> <span class=\"gif\"></span>");
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    socket.on('my response', function(msg) {
        $('.list').append("<li class=\"task\">" + msg.data + " <img src=\"../static/Checkmark.svg\" style=\"width:1em;height:1em;\"></img></li>");
        $('.task:hidden:last').fadeIn("slow");


    $(".loading").each(function(){
        $(this).trigger("complete"+responseNum.toString());
        console.log("TRWE");

    });
        console.log(msg.data);

    });
    responseNum=responseNum+1;
    socket.on('done', function(){
        $(".gif").append("<img src=\"../static/my_gif.GIF\">");
        $(".gif").addClass("browser-mockup");
    });
});


    

}

$(document).ready(initialize);