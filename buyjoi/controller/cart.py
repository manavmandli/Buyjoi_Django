from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from buyjoi.models import Product, Cart
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore



# def addtocart(request):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             prod_id = int(request.POST.get('product_id'))
#             product_check = Product.objects.get(id=prod_id)

#             if (product_check):
#                 if (Cart.objects.filter(user=request.user.id, product_id=prod_id)):
#                     return JsonResponse({'status': "Product Already in Cart"})
#                 else:
#                     prod_qty = int(request.POST.get('product_qty'))

#                     if product_check.quantity >= prod_qty:
#                         Cart.objects.create(
#                             user=request.user, product_id=prod_id, product_qty=prod_qty)
#                         return JsonResponse({'status': "Product added successfully"})
#                     else:
#                         return JsonResponse({'status': "Only " + str(product_check.quantity) + " quantity available"})

#             else:
#                 return JsonResponse({'status': "No such product found"})
#         else:
#             return JsonResponse({'status': "Login to Continue"})

#     return redirect("/")



# @login_required(login_url='loginpage')
# def viewcart(request):
#     if request.user.is_authenticated:
#         cart = Cart.objects.filter(user=request.user)
#         context = {
#             'cart': cart
#         }
#         return render(request, "cart.html", context)
#     else:
#         messages.error(
#             request, "Kindly login to access this section, Thank you.")
#         return redirect("/")

def addtocart(request):
    if request.method == 'POST':
        session = SessionStore(request.session.session_key)
        if not session.exists(session.session_key):
            session.create()

        prod_id = int(request.POST.get('product_id'))
        product_check = Product.objects.filter(id=prod_id).first()

        if product_check:
            cart_products = session.get('cart_products', {})
            if str(prod_id) in cart_products:
                return JsonResponse({'status':"Product Already in Cart"})
            else:
                prod_qty = int(request.POST.get('product_qty'))

                if product_check.quantity >= prod_qty:
                    cart_products[str(prod_id)] = prod_qty
                    session['cart_products'] = cart_products
                    session.save()
                    return JsonResponse({'status': "Product added successfully"})
                else:
                    return JsonResponse({'status': "Only " + str(product_check.quantity) + " quantity available"})
        else:
            return JsonResponse({'status': "No such product found"})
    return redirect("/")

def viewcart(request):
    session = SessionStore(request.session.session_key)
    cart_products = session.get('cart_products', {})
    cart_items = Product.objects.filter(id__in=cart_products.keys())

    # Create a dictionary to store product IDs and their corresponding quantities
    cart_quantity = {}
    for item in cart_items:
        cart_quantity[item.id] = cart_products[str(item.id)]

    context = {
        'cart': cart_items,
        'cart_quantity': cart_quantity
    }
    return render(request, "cart.html", context)
   
# def updatecart(request):
#     if request.method == 'POST':
#         prod_id = int(request.POST.get('product_id'))
#         if (Cart.objects.filter(user=request.user, product_id=prod_id)):
#             prod_qty = int(request.POST.get('product_qty'))
#             cart = Cart.objects.get(product_id=prod_id, user=request.user)
#             cart.product_qty = prod_qty
#             cart.save()
#             return JsonResponse({'status': "Updated Successfully"})
#     return redirect('/')

def updatecart(request):
    if request.method == 'POST':
        session = SessionStore(request.session.session_key)
        cart_products = session.get('cart_products', {})
        
        prod_id = int(request.POST.get('product_id'))
        prod_qty = int(request.POST.get('product_qty'))
        
        if str(prod_id) in cart_products:
            cart_products[str(prod_id)] = prod_qty
            session['cart_products'] = cart_products
            session.save()
            
            return JsonResponse({'status': "Updated Successfully"})
        
    return redirect('/')

# def deletecartitem(request):
#     if request.method == 'POST':
#         prod_id = int(request.POST.get('product_id'))
#         if(Cart.objects.filter(user=request.user, product_id=prod_id)):
#             cartitem = Cart.objects.get(product_id=prod_id, user=request.user)
#             cartitem.delete()
#         return JsonResponse({'status:"Deleted Successfully"'})
#     return redirect('/')

def deletecartitem(request):
    if request.method == 'POST':
        session = SessionStore(request.session.session_key)
        cart_products = session.get('cart_products', {})
        
        prod_id = int(request.POST.get('product_id'))
        
        if str(prod_id) in cart_products:
            del cart_products[str(prod_id)]
            session['cart_products'] = cart_products
            session.save()
            
            return JsonResponse({'status': "Deleted Successfully"})
        
    return redirect('/')