// Getting products by category_id
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

//Getting unit price by product id
$(function () {
    $('#id_product').on('change', function () {
        var id_product = $(this).val();
        $.get('/orders/getUnitPrice',
            {
                id_product: id_product
            },
            function (data) {
                $('#unit_price').val(data);
            });
    });
});

// Getting total
$(function () {
    $('#id_qty').on('change', function () {
       var price = $('#unit_price').val();
       var qty = $(this).val();
       total = price * qty;
       $('#id_total').val(total);
    });
 });