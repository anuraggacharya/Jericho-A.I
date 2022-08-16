$( document ).ready(function() {
    console.log( "ready!" );
});
$("#sayHello").click(function(){
    $.ajax({
        type: "POST",
        url: "/sayHello",
        data: JSON.stringify({'name':'gayatri'}),
        contentType: 'application/json',
        success: function(data){
           console.log("done")
        }
      });
})
$(".ledButton").click(function(){
    command=$(this).data('command')
    console.log(command)
    $.ajax({
        type: "POST",
        url: "/controlLed",
        data: JSON.stringify({"command":command}),
        contentType: 'application/json',
        success: function(data){
           console.log("done")
        }
      });
})