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


  $('.changeQuantity').click(function (e) {
    e.preventDefault();

    var product_id = $(this).closest('.product_data').find('.prod_id').val();
    var product_qty = $(this).closest('.product_data').find('.qty_input').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
      method: "POST",
      url: "/update-cart",
      data: {
        'product_id': product_id,
        'product_qty': product_qty,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
      },
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
