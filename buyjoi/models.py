from datetime import datetime
from distutils.command.upload import upload
from email.mime import image
from unicodedata import category
from django.db import models
from django.forms import ImageField
import os
import datetime
from django.contrib.auth.models import User

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('upload/', filename)


class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=False, blank=True)
    round_image = models.ImageField(upload_to=get_file_path, null=False, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default 1=hidden")
    trending = models.BooleanField(default=False, help_text="0=default 1=trending")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=750, null=False, blank=False)
    meta_description = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=1150, null=False, blank=True)
    name = models.CharField(max_length=1150, null=False, blank=True)
    product_image1 = models.ImageField(upload_to=get_file_path, null=False, blank=True)
    product_image2 = models.ImageField(upload_to=get_file_path, null=False, blank=True)
    product_image3 = models.ImageField(upload_to=get_file_path, null=False, blank=True)
    small_description = models.TextField(max_length=1500, null=False, blank=True)
    quantity = models.IntegerField(null=False, blank=True)
    description = models.TextField(max_length=12500, null=False, blank=True)
    original_price = models.FloatField(null=False, blank=True)
    selling_price = models.FloatField(null=False, blank=True)
    rating_number = models.CharField(max_length=1150, null=False, blank=True)
    status = models.BooleanField(default=False, help_text="0=default 1=hidden")
    trending = models.BooleanField(default=False, help_text="0=default 1=trending")
    homepage = models.BooleanField(default=False, help_text="0=default 1=trending")
    tag = models.CharField(max_length=1150, null=False, blank=True)
    meta_title = models.CharField(max_length=1150, null=False, blank=True)
    meta_keywords = models.CharField(max_length=1750, null=False, blank=True)
    meta_description = models.TextField(max_length=12500, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class HomeProduct(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=1150, null=False, blank=True)
    name = models.CharField(max_length=1150, null=False, blank=True)
    product_image1 = models.ImageField(upload_to=get_file_path, null=False, blank=True)
    product_image2 = models.ImageField(upload_to=get_file_path, null=False, blank=True)
    product_image3 = models.ImageField(upload_to=get_file_path, null=False, blank=True)
    small_description = models.TextField(max_length=1500, null=False, blank=True)
    quantity = models.IntegerField(null=False, blank=True)
    description = models.TextField(max_length=12500, null=False, blank=True)
    original_price = models.FloatField(null=False, blank=True)
    selling_price = models.FloatField(null=False, blank=True)
    rating_number = models.CharField(max_length=1150, null=False , blank=True)
    status = models.BooleanField(default=False, help_text="0=default 1=hidden")
    trending = models.BooleanField(default=False, help_text="0=default 1=trending")
    homepage = models.BooleanField(default=False, help_text="0=default 1=trending")
    tag = models.CharField(max_length=1150, null=False, blank=True)
    meta_title = models.CharField(max_length=1150, null=False, blank=True)
    meta_keywords = models.CharField(max_length=1750, null=False, blank=True)
    meta_description = models.TextField(max_length=12500, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
 
 

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=1150, null=False)
    lname = models.CharField(max_length=1150, null=True)
    phone = models.CharField(max_length=1150, null=False)
    pincode = models.CharField(max_length=1150, null=False)
    flat = models.CharField(max_length=1150, null=False)
    area = models.CharField(max_length=1150, null=False)
    landmark = models.CharField(max_length=1150, null=False)
    city = models.CharField(max_length=1150, null=False)
    state = models.CharField(max_length=1150, null=False)
    country = models.CharField(max_length=1150, null=False)
    addresstype = models.CharField(max_length=1150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=250, null=True)
    orderstatuses = (
        ('Pending','Pending'),
        ('Out For Shipping', 'Out For Shipping'),
        ('Completed','Completed'),
    )
    status = models.CharField(max_length=150, choices=orderstatuses, default='Pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	price = models.FloatField(null=False)
	quantity = models.IntegerField(null=False)

	def __str__(self):
		return '{} {}'.format(self.order.id, self.order.tracking_no)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=1150, null=False)
    lname = models.CharField(max_length=1150, null=True)
    phone = models.CharField(max_length=1150, null=False)
    pincode = models.CharField(max_length=1150, null=False)
    flat = models.CharField(max_length=1150, null=False)
    area = models.CharField(max_length=1150, null=False)
    landmark = models.CharField(max_length=1150, null=False)
    city = models.CharField(max_length=1150, null=False)
    state = models.CharField(max_length=1150, null=False)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
         return self.user.username
     
     
     
     
class ExcelFileUpload(models.Model):
	excel_file_upload = models.FileField(upload_to="excel")


class EmailSubcription(models.Model):
    emailtosubscribe = models.CharField(max_length=1150, null=True)



class contactform(models.Model):
    personname = models.CharField(max_length=1150, null=True)
    personemail = models.CharField(max_length=1150, null=True)
    personmessage = models.TextField(max_length=12500, null=False, blank=True)
