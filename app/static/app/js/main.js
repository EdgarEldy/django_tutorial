// Get products by category_id using ajax

$(function () {
    $("#category_id").on("change", function () {
        // Get the category id in the categories select menu
        category_id = $(this).val();
        // alert(category_id);
        $.get(
            "/orders/getProducts",
            {
                category_id: category_id,
            },
            function (data) {
                // Select menu must be empty before adding products
                $("#id_product").empty();
                // Add products to the select menu
                $.each(data, function (index, row) {
                    $("#id_product").append(
                        "<option value='" + row.id + "'>" + row.product_name + "</option>"
                    );
                });
            }
        );
    });
});

// Get unit price by product id
$(function () {
    $('#id_product').on('change', function () {
        id_product = $(this).val();
        // alert(id_product)
        $.get(
            '/orders/getUnitPrice',
            {
                id_product: id_product
            },
            function (data) {
                $('#unit_price').val(data);
            }
        );
    });
});

// Calculate the total
$('#id_quantity').on('keyup', function () {
    var id_qty = $(this).val();
    // alert(id_quantity)
    var unit_price = $('#unit_price').val();
    var total = id_qty * unit_price;
    $('#id_total').val(total);
});