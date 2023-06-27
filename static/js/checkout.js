$(document).ready(function () {
    
    $('.payWithRazorpay').click(function (e) { 
        e.preventDefault();
        
        var fname = $("[name='fname']").val();
        var lname = $("[name='lname']").val();
        var phone = $("[name='phone']").val();
        var pincode = $("[name='pincode']").val();
        var flat = $("[name='flat']").val();
        var area = $("[name='area']").val();
        var landmark = $("[name='landmark']").val();
        var city = $("[name='city']").val();
        var state = $("[name='state']").val();
        var token = $("[name='csrfmiddlewaretoken']").val();

        if(fname == "" || lname == "" || phone == "" || pincode == "" || flat == "" || area == "" || landmark == "" || city == "" || state == "" )
        {
            swal("Please fill all the details");
            return false;
        }

        else
        {

            $.ajax({
                method: "GET",
                url: "/proceed-to-pay",
                success: function (response) {
                    var options = {
                        "key": "rzp_live_XImGyqdu2cMBu3", // Enter the Key ID generated from the Dashboard
                        "amount": response.total_price * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "Buyjoi Ecommerce Platform",
                        "description": "Thank you for purchasing.",
                        "image": "http://buyjoi.com/static/img/buyjoilogoweb.jpg ",
                        // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (responseb){
                            alert(responseb.razorpay_payment_id);                            
                            data = {
                                "fname": fname,
                                "lname": lname,
                                "phone": phone,
                                "pincode": pincode,
                                "flat": flat,
                                "area": area,
                                "landmark": landmark,
                                "city": city,
                                "state": state,
                                "payment_mode": "Paid by Razorpay",
                                "payment_id": responseb.razorpay_payment_id,
                                csrfmiddlewaretoken: token
                            }
                            $.ajax({
                                method: "POST",
                                url: "/placeorder",
                                data: data,
                                success: function (responsec) {
                                    swal("Congratulations!", responsec.status )
                                    .then((value) => {
                                        window.location.href = '/myorder'
                                    });

                                }
                            });
                        },

                        "prefill": {
                            "name": fname,
                            "email": email,
                            "contact": phone,
                        },
                        
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();
            
                }
            });


    
        }

    });

});