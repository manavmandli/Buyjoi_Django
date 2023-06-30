from django.contrib import admin
from .models import Category, Order, OrderItem, Product, Cart, Profile, EmailSubcription, contactform
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    search_fields=('name',)


admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
admin.site.register(Product, ProductAdmin)
admin.site.register(EmailSubcription)
admin.site.register(contactform)






