from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from buyjoi.models import Product, Cart, Wishlist
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

# @login_required(login_url='loginpage')
# def wishlistpage(request):
# 	wishlistitem = Wishlist.objects.filter(user=request.user)
# 	context = {'wishlistitem':wishlistitem}
# 	return render(request, 'wishlist.html', context)

# def addtowishlist(request):
# 	if request.method == 'POST':
# 		if request.user.is_authenticated:
# 			prod_id = int(request.POST.get('product_id'))
# 			product_check = Product.objects.get(id=prod_id)
# 			if(product_check):
# 				if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
# 					return JsonResponse({'status':"Product already in wishlist"})
# 				else:
# 					Wishlist.objects.create(user=request.user, product_id=prod_id)
# 					return JsonResponse({'status':"Product added to wishlist"})
# 			else:
# 				return JsonResponse({'status':"No such product found"})
# 		else:
# 			return JsonResponse({'status':"Login to continue"})
# 	return redirect('/')

# manav code
def wishlistpage(request):
    wishlist = request.session.get('wishlist', {})
    if request.user.is_authenticated:
        for product_id, item in wishlist.items():
            findproduct = Product.objects.get(id=product_id)
            sessioncartitem, created = Wishlist.objects.get_or_create(product=findproduct, user=request.user)
        request.session.pop('wishlist', None)
        wishlist = Wishlist.objects.filter(user=request.user)
        context = {'wishlistitem': wishlist}
        return render(request, "wishlist.html", context)
    else:
        product_ids = list(wishlist.keys())
        products = Product.objects.filter(id__in=product_ids)
        context = {
            'wishlist': products
        }
        return render(request, "sessionwishlist.html", context)

def addtowishlist(request, product_id):
    prod_id = int(product_id)
    product_check = Product.objects.filter(id=prod_id)
    if product_check:
        if request.user.is_authenticated:
            if Wishlist.objects.filter(user=request.user, product=prod_id).exists():
                messages.error(request, 'Product is already in your wishlist.')
            else:
                Wishlist.objects.create(user=request.user, product=prod_id)
                messages.success(request, 'Product added to your wishlist.')
        else:
            # Create a session-based wishlist
            wishlist = request.session.get('wishlist', {})
            if prod_id in wishlist:
                messages.error(request, 'Product is already in your wishlist.')
            else:
                prod_qty = 1  # Assuming a default quantity of 1 for session-based wishlist
                wishlist[prod_id] = {
                    'product_id': prod_id,
                }
                request.session['wishlist'] = wishlist
                messages.success(request, 'Product added to your wishlist.')
            # next_page = request.GET.get('next')
            # product = Product.objects.get(id=product_id)
            # next_page =reverse('productview', args=[product.category.slug, product.slug])
            # add_to_wishlist_url = reverse('addtowishlist', args=[prod_id]) + '?next=' + next_page
            # if next_page:
            #     return redirect(next_page)
    else:
        messages.error(request, 'No such product found.')
    return redirect('wishlistpage')

def deletewishlistitem(request, item_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(Wishlist, user=request.user, product_id=item_id)
        cart_item.delete()
        messages.success(request, 'Wishlist item deleted successfully.')
    else:
        session_cart = request.session.get('wishlist', {})
        if str(item_id) in session_cart:
            del session_cart[str(item_id)]
            request.session['wishlist'] = session_cart
            messages.success(request, 'wishlist item deleted successfully.')
        else:
            messages.error(request, 'wishlist item not found.')

    return redirect('wishlistpage')


