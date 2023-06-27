from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from buyjoi.models import Product, Cart
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session



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



# def addtocart(request):
#     if request.method == 'POST':
#         prod_id = int(request.POST.get('product_id'))
#         product_check = Product.objects.get(id=prod_id)

#         if (product_check):
#             # Check if cart exists in the session, create one if not
#             if 'cart' not in request.session:
#                 request.session['cart'] = {}

#             cart = request.session['cart']

#             # Check if the product is already in the cart
#             if str(prod_id) in cart:
#                 return JsonResponse({'status': "Product Already in Cart"})

#             prod_qty = int(request.POST.get('product_qty'))

#             if product_check.quantity >= prod_qty:
#                 # Add the product to the cart in the session
#                 cart[str(prod_id)] = prod_qty
#                 request.session.modified = True
#                 return JsonResponse({'status': "Product added successfully"})
#             else:
#                 return JsonResponse({'status': "Only " + str(product_check.quantity) + " quantity available"})

#         else:
#             return JsonResponse({'status': "No such product found"})

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


# def viewcart(request):
#     if 'cart' in request.session:
#         cart = Cart('cart')
#         return render(request, 'cart.html', {'cart': cart.items})  # Assuming 'items' is the list of items in the cart
#     else:
#         messages.error(request, "You don't have any product in your cart.")
#         return render(request, 'cart.html')

class Cart:
    def _init_(self, cart_id):
        self.cart_id = cart_id
        self.items = []  # Initialize the items attribute as an empty list

    # Other methods and properties of the Cart class...

# def viewcart(request):
#     if 'cart' in request.session:
#         cart = Cart('cart')
#         return render(request, 'cart.html', {'cart': cart.items})
#     else:
#         messages.error(request, "You don't have any product in your cart.")
#         return render(request, 'cart.html')

#manav code 
def addtocart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        product_check = Product.objects.get(id=prod_id)

        if product_check:
            # Check if cart exists in the session, create one if not
            if 'cart' not in request.session:
                request.session['cart'] = {}

            cart = request.session['cart']

            # Check if the product is already in the cart
            if str(prod_id) in cart:
                return JsonResponse({'status': 'Product Already in Cart'})

            prod_qty = int(request.POST.get('product_qty'))

            if product_check.quantity >= prod_qty:
                # Add the product to the cart in the session
                cart[str(prod_id)] = prod_qty
                request.session.modified = True
                return JsonResponse({'status': 'Product added successfully'})
            else:
                return JsonResponse({'status': f'Only {product_check.quantity} quantity available'})

        else:
            return JsonResponse({'status': 'No such product found'})

    return redirect('/')


def viewcart(request):
    if 'cart' in request.session:
        cart = request.session['cart']
        product_ids = cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart_items = []

        for product in products:
            cart_item = {
                'product': product,
                'quantity': cart[str(product.id)],
            }
            cart_items.append(cart_item)

        return render(request, 'cart.html', {'cart_items': cart_items})
    else:
        messages.error(request, "You don't have any products in your cart.")
        return render(request, 'cart.html')

   
def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status': "Updated Successfully"})
    return redirect('/')


def deletecartitem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cartitem = Cart.objects.get(product_id=prod_id, user=request.user)
            cartitem.delete()
        return JsonResponse({'status:"Deleted Successfully"'})
    return redirect('/')