from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from buyjoi.models import Product, Cart, Order, OrderItem
from django.contrib.auth.decorators import login_required


@login_required(login_url='loginpage')
def myorder(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request, "myorder.html", context)


def vieworder(request, t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = { 'order' : order, 'orderitems' : orderitems }
    return render(request, "vieworder.html", context)