$(document).ready(function () {

  // $('.addToCartBtn').click(function (e) {
  //   e.preventDefault();

  //   var product_id = $(this).closest('.product_data').find('.prod_id').val();
  //   var product_qty = $(this).closest('.product_data').find('.qty_input').val();
  //   var token = $('input[name=csrfmiddlewaretoken]').val();
  //   $.ajax({
  //     method: "POST",
  //     url: "/add-to-cart",
  //     data: {
  //       'product_id': product_id,
  //       'product_qty': product_qty,
  //       csrfmiddlewaretoken: token,
  //     },
  //     success: function (response) {
  //       console.log(response);
  //       alertify.success(response.status);
  //     },
  //   });
  // });



    $('.addToCartBtn').click(function (e) {
      e.preventDefault();
  
      var product_id = $(this).closest('.product_data').find('.prod_id').val();
      var product_qty = $(this).closest('.product_data').find('.qty_input').val();
      var token = $('input[name=csrfmiddlewaretoken]').val();
  
      $.ajax({
        method: "POST",
        url: "/add-to-cart",
        data: {
          'product_id': product_id,
          'product_qty': product_qty,
          csrfmiddlewaretoken: token,
        },
        success: function (response) {
          console.log(response);
          alertify.success(response.status);
        },
      });
    });




  $('.addToWishlist').click(function (e) {
    e.preventDefault();

    var product_id = $(this).closest('.product_data').find('.prod_id').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
      method: "POST",
      url: "/add-to-wishlist",
      data: {
        'product_id': product_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        alertify.success(response.status);
      },
    });
  });


  // $('.changeQuantity').click(function (e) {
  //   e.preventDefault();

  //   var product_id = $(this).closest('.product_data').find('.prod_id').val();
  //   var product_qty = $(this).closest('.product_data').find('.qty_input').val();
  //   var token = $('input[name=csrfmiddlewaretoken]').val();
  //   $.ajax({
  //     method: "POST",
  //     url: "/update-cart",
  //     data: {
  //       'product_id': product_id,
  //       'product_qty': product_qty,
  //       csrfmiddlewaretoken: token,
  //     },
  //     success: function (response) {
  //     },
  //   });
  // });

   $('.qty_input').each(function() {
    var quantityInput = $(this);
    var product_id = quantityInput.data('product-id');
    var cart_quantity = '{{ cart_quantity|get_item:item.id|stringformat:"d" }}';
    quantityInput.val(cart_quantity);
  });

  // Handle quantity change
  $('.changeQuantity').click(function(e) {
    e.preventDefault();
    var action = $(this).data('action');
    var quantityInput = $(this).parent().find('.qty_input');
    var product_id = quantityInput.data('product-id');
    var product_qty = parseInt(quantityInput.val());
    var token = $('input[name=csrfmiddlewaretoken]').val();

    if (action === 'decrement') {
      product_qty = Math.max(0, product_qty - 1);
    } else if (action === 'increment') {
      product_qty += 1;
    }

    quantityInput.val(product_qty);

    // Update the quantity in the server using AJAX
    $.ajax({
      method: "POST",
      url: "/update-cart",
      data: {
        'product_id': product_id,
        'product_qty': product_qty,
        'csrfmiddlewaretoken': token
      },
      success: function(response) {
        // Handle success response if needed
      },
      error: function(xhr, textStatus, error) {
        console.log(xhr.statusText);
        console.log(textStatus);
        console.log(error);
      }
    });
  });
  $('.deletecartitemBtn').click(function (e) {
    e.preventDefault();

    var product_id = $(this).closest('.product_data').find('.prod_id').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();
    
    $.ajax({
      method: "POST",
      url: "/delete-cart-item",
      data: {
        'product_id': product_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        alertify.success(response.status)

      },
    });
  });
  
  $('.deletewishlistbtn').click(function (e) {
    e.preventDefault();

    var product_id = $(this).closest('.product_data').find('.prod_id').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();
    
    $.ajax({
      method: "POST",
      url: "/delete-wishlist-item",
      data: {
        'product_id': product_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        alertify.success(response.status)

      },
    });
  });
});
