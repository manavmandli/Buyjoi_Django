from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from buyjoi.models import Product, Cart
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404, redirect
from django.db.models import F, Sum



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



# manav code 
def addtocart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        product_check = Product.objects.filter(id=prod_id).first()
        print(product_check)
        if product_check:
            if request.user.is_authenticated:
                if Cart.objects.filter(user=request.user, product_id=prod_id).exists():
                    return JsonResponse({'status': "Product Already in Cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(
                            user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': "Product added successfully"})
                    else:
                        return JsonResponse({'status': "Only " + str(product_check.quantity) + " quantity available"})
            else:
                cart = request.session.get('cart', {})

                if prod_id in cart:
                    return JsonResponse({'status': "Product Already in Cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >= prod_qty:
                        cart[prod_id] = {
                            'product_id': prod_id,
                            'product_qty': prod_qty,
                        }
                        request.session['cart'] = cart
                        return JsonResponse({'status': "Product added successfully"})
                    else:
                        return JsonResponse({'status': "Only " + str(product_check.quantity) + " quantity available"})

        else:
            return JsonResponse({'status': "No such product found"})

    return redirect("/")





#manav code 
def viewcart(request):
    cart = request.session.get('cart', {}).values()
    total_quantity = sum(item['product_qty'] for item in cart)
    if request.user.is_authenticated:
        for item in cart:
            product_id = item['product_id']
            quantity = item['product_qty']
            findproduct = Product.objects.get(id=product_id)
            sessioncartitem, created = Cart.objects.get_or_create(product_id=findproduct.id, product_qty=quantity, user=request.user)
        request.session.pop('cart', None)
        cart_item=0
        cart = Cart.objects.filter(user=request.user)
        total_price = cart.aggregate(total_price=Sum(F('product__selling_price') * F('product_qty')))['total_price']
        for i in cart:
            cart_item=cart_item+1
        context = {
            'cart_item':cart_item,
            'cart': cart,
            'total_price': total_price,
        }
        return render(request, "cart.html", context)
    else:
        products = []
        for item in cart:
            product_id = item['product_id']
            quantity = item['product_qty']
            findproduct = Product.objects.get(id=product_id)
            products.append(findproduct)
        context = {
            'cart': products,
        }
        return render(request, "sessioncart.html", context)


def minus_cart(request, product_id):
    cp = Cart.objects.get(user=request.user, product_id=product_id)
    if cp.product_qty == 1:
        cp.delete()
    else:
        cp.product_qty -= 1
        cp.save()
        messages.success(request, 'Quantity updated successfully.')
    return redirect('cart')  


def plus_cart(request, product_id):
    cp = Cart.objects.get(user=request.user, product_id=product_id)
    if cp:
        cp.product_qty += 1
        cp.save()
        messages.success(request, 'Quantity updated successfully.')
    else:
        messages.error(request, 'Cart item not found.')
    return redirect('cart')

def deletecartitem(request, product_id):
    cart_item = get_object_or_404(Cart, user=request.user, product_id=product_id)

    if cart_item:
        cart_item.delete()
        messages.success(request, 'Cart item deleted successfully.')
    else:
        messages.error(request, 'Cart item not found.')
    return redirect('cart')

def remove_item_from_session(request, item_id):
    cart = request.session.get('cart', {}).values()
    if 'cart' in request.session:
        if item_id in cart:
            print("----",cart[item_id])
            del cart[item_id]
            request.session['cart'] = cart
            request.session.modified = True
            request.session.save()
            return JsonResponse({'status': 'Deleted Successfully'})
    return redirect('/')