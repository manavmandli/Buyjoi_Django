from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from buyjoi.models import Product, Cart, Order, OrderItem, Profile, EmailSubcription
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import random
from django.http import JsonResponse

@login_required(login_url='loginpage')
def checkoutpage(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)

        cartitems = Cart.objects.filter(user=request.user)
        total_price = 0
        for item in cartitems:
            total_price = total_price + item.product.selling_price * item.product_qty
            
        userprofile = Profile.objects.filter(user=request.user).first()

        context = {'cartitems': cartitems, 'total_price':total_price, 'userprofile':userprofile}
        return render(request, "checkout.html", context)
    
    
@login_required(login_url='loginpage')
def placeorder(request):
    if request.method == 'POST':
        
        currentuser = User.objects.filter(id=request.user.id).first()
        
        if not currentuser.first_name :
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()
        
        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.phone = request.POST.get('phone')
            userprofile.pincode = request.POST.get('pincode')
            userprofile.flat = request.POST.get('flat')
            userprofile.area = request.POST.get('area')
            userprofile.landmark = request.POST.get('landmark')
            userprofile.city = request.POST.get('city')
            userprofile.state = request.POST.get('state')
            userprofile.save()
            
            
        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.phone = request.POST.get('phone')
        neworder.pincode = request.POST.get('pincode')
        neworder.flat = request.POST.get('flat')
        neworder.area = request.POST.get('area')
        neworder.landmark = request.POST.get('landmark')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')        
        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_id')
        
        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty            
            
        neworder.total_price = cart_total_price
        trackno = 'buyjoi'+str(random.randint(1111111,9999999))   
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = 'buyjoi'+str(random.randint(1111111,9999999))

        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty

            )
            
            # to decrease product quantity from available stock
            
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()

        # to make clear the cart
        Cart.objects.filter(user=request.user).delete()
        
        messages.success(request, "Your order has been placed successfuly!")
        
        payMode = request.POST.get('payment_mode')
        if (payMode == "Paid by Razorpay"):
            return JsonResponse({'status':"Your order has been placed successfuly!"})
                
    return redirect('/')



@login_required(login_url='loginpage')
def proceedtopay(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart:
        total_price = total_price + item.product.selling_price * item.product_qty
    return JsonResponse({
        'total_price' : total_price
    })
    
    
    
def footer(request):
    if request.method == 'POST':
        emailhome = request.POST.get['email']
        data = EmailSubcription( emailtosubscribe=emailhome )
        data.save()
    return render(request, 'footer.html')
