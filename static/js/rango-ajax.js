$(document).ready(function() {
    $('#like_btn').click(function() {
        var animalIdVar;
        animalIdVar = $(this).attr('data-animalid');

        $.get('/rango/like_animal/', {'animal_id': animalIdVar}, function(data) {
                $('#like_count').html(data);
                $('#like_btn').hide();
            });

    });
});