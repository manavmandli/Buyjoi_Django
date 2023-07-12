from django.urls import path
from . import views
from buyjoi.controller import authview, cart, wishlist, checkout, myorder

urlpatterns = [
    path('' , views.index, name='index'),
    path('home' , views.home, name='home'),
    path('contact' , views.contact , name='contact'),
    path('baby' , views.index, name='baby'),
    path('cosmetics' , views.index, name='cosmetics'),
    path('books' , views.index, name='books'),
    path('carmotorbike' , views.index, name='carmotorbike'),
    path('computers' , views.index, name='computers'),
    path('fashion' , views.index, name='fashion'),
    path('grocery' , views.index, name='grocery'),
    path('pharmacy' , views.index, name='pharmacy'),
    path('privacy' , views.privacy, name='privacy'),
    path('saree' , views.saree, name='saree'),
    path('menwear' , views.index, name='menwear'),
    path('womenwear' , views.index, name='womenwear'),
    path('kurti' , views.kurti, name='kurti'),
    path('lehenga' , views.lehenga, name='lehenga'),

    path('sitemap' , views.sitemap , name='sitemap'),
    path('search/' , views.search, name='search'),

    path('collections' , views.collections, name='collections'),
    path('collectionsview/<str:slug>' , views.collectionsview, name='collectionsview'),
    path('<str:cate_slug>/<str:prod_slug>' , views.productview, name='productview'),
    
    path('register' , authview.register, name='register'),
    path('login' , authview.loginpage,  name='loginpage'),

    path('forgot_password',authview.forgotpassword,name='forgotpassword'),
    path('otp-verify', authview.otp_verify, name='otp_verify'),
    path('new_password',authview.new_password,name='newpassword'),

    path('logout' , authview.logoutpage,   name='logoutpage'),
    path('account' , authview.account, name='account'),
    
    path('add-to-cart' , cart.addtocart, name='addtocart'),
    path('cart' , cart.viewcart , name='cart'),
    path('update-cart' , cart.updatecart , name='updatecart'),
    path('delete-cart-item' , cart.deletecartitem , name='deletecartitem'),
    path('remove_item_from_session/<int:item_id>/', cart.remove_item_from_session, name="remove_item_from_session"),
    
    path('wishlist' , wishlist.wishlistpage , name='wishlistpage'),
    path('add-to-wishlist' , wishlist.addtowishlist , name='addtowishlist'),
    path('delete-wishlist-item' , wishlist.deletewishlistitem , name='deletewishlistitem'),
    
    path('checkout' , checkout.checkoutpage, name='checkoutpage'),
    path('thankyou' , views.thankyou, name='thankyou'),
    path('placeorder' , checkout.placeorder, name='placeorder'),
    path('proceed-to-pay' , checkout.proceedtopay),
    path('myorder' , myorder.myorder, name='myorder'),
    path('<str:t_no>' , myorder.vieworder, name='vieworder'),
    path('footer' , checkout.footer, name='footer'),

               
    path('product-list' , views.productlistAjax),
     


    
]