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
