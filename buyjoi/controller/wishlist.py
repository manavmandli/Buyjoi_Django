from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from buyjoi.models import Product, Cart, Wishlist
from django.contrib.auth.decorators import login_required

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

#manav code
def wishlistpage(request):
    wishlist = request.session.get('wishlist', {})
    if request.user.is_authenticated:
        for product_id, item in wishlist.items():
            findproduct = Product.objects.get(id=product_id)
            sessioncartitem, created = Wishlist.objects.get_or_create(product=findproduct, user=request.user)
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

def addtowishlist(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        product_check = Product.objects.get(id=prod_id)
        if product_check:
            if request.user.is_authenticated:
                if Wishlist.objects.filter(user=request.user, product_id=prod_id).exists():
                    return JsonResponse({'status': "Product already in wishlist"})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status': "Product added to wishlist"})
            else:
                # Create a session-based wishlist
                wishlist = request.session.get('wishlist', {})
                if prod_id in wishlist:
                    return JsonResponse({'status': "Product already in wishlist"})
                else:
                    wishlist[prod_id] = True
                    request.session['wishlist'] = wishlist
                    return JsonResponse({'status': "Product added to wishlist"})
        else:
            return JsonResponse({'status': "No such product found"})
    return redirect('/')


def deletewishlistitem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            
            if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                wishlistitem = Wishlist.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':"Product removed from wishlist"})
            else:
                Wishlist.objects.create(user=request.user, product_id=prod_id)
                return JsonResponse({'status':"Product not found in wishlist"})
        else:
            return JsonResponse({'status':"Login to continue"})

    return redirect('/')