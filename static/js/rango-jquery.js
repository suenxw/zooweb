$(document).ready( function() {

    $('#add_aniaml').click(function() {
        var selected_cat;
        selected_cat = $(this).attr('selected_cat');

        $.get('/rango/like_animal/', {'category_name_slug': selected_cat}, function(data) {
                $('#add_aniaml').html(data);
            });
    });


    $('p').hover(
        function() {
            $(this).css('color', 'red');
        },
        function() {
            $(this).css('color', 'black');
        });




});