$(document).ready(function() {
    $('#like_btn').click(function() {
        var animalIdVar;
        animalIdVar = $(this).attr('data-animalid');

        $.get('/rango/like_animal/', {'animal_id': animalIdVar}, function(data) {
                $('#like_count').html(data);
                $('#like_btn').hide();
            });

        // $.get('/rango/like/', {category_id: catid}, function(data){
        //     $('#like_count').html(data);
        //     $('#likes').hide();
        // });
    });

    // $('#search-input').keyup(function() {
    //     var query;
    //     query = $(this).val();
    //
    //     $.get('/rango/<slug:category_name_slug>/suggest', {'suggestion': query},
    //           function(data) {
    //               $('#categories-listing').html(data);
    //           });
    // });

    // $('.rango-page-add').click(function() {
    //     var categoryid = $(this).attr('data-categoryid');
    //     var title = $(this).attr('data-title');
    //     var url = $(this).attr('data-url');
    //     var clickedButton = $(this);
    //
    //     $.get('/rango/search_add_page/',
    //           {'category_id': categoryid, 'title': title, 'url': url},
    //           function(data) {
    //               $('#page-listing').html(data);
    //               clickedButton.hide();
    //           })
    // });
});