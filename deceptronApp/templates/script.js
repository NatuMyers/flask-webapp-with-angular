$(function() {
    $('#button').click(function(){
	var data = {text: $('#input').val()};
	$.ajax({
	    url: '/',
            type: 'POST',
	    contentType: 'application/json; charset=utf-8',
	    data: JSON.stringify(data),
            success: function(response) {
		$("#result").html(response);
		$("#input").val('');
            }
	});
    });
});
