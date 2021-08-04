$(document).ready( function() {
    // $("#about-btn").click( function(event) {
    //     console.log(123);
    //     alert("You clicked the button using jQuery!");
    // });
    $('#add_aniaml').click(function() {
        var selected_cat;
        selected_cat = $(this).attr('selected_cat');

        $.get('/rango/like_animal/', {'category_name_slug': selected_cat}, function(data) {
                $('#add_aniaml').html(data);
                // $('#like_btn').hide();
            });
    });


    $('p').hover(
        function() {
            $(this).css('color', 'red');
        },
        function() {
            $(this).css('color', 'black');
        });

    // $('#about-btn').click(function() {
    //     msgStr = $('#msg').html();
    //     msgStr = msgStr + " ooo, fancy!";
    //
    //     $('#msg').html(msgStr);
    // })


});