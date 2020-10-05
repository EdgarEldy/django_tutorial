$(function () {
    $('#category_id').on('change', function () {
        var category_id = $(this).val();
        //alert(category_id);
        $.get('/orders/getProducts',
            {
                category_id: category_id
            },
            function (data) {
                $('#id_product').html(data);
            });
    });
});