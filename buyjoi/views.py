from email import message
from telnetlib import STATUS
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Product, Category, EmailSubcription, contactform
from django.core.paginator import Paginator
from django.http import JsonResponse




# Create your views here.
def index(request):
    if request.method == 'POST':
        emailhome = request.POST['email']
        dataemail = EmailSubcription( emailtosubscribe=emailhome )
        dataemail.save()
    homesaree = Product.objects.filter(category__name='saree' , homepage=1)[:44]
    homekurti = Product.objects.filter(category__name='Kurti' , homepage=1)[:12]
    homelehenga = Product.objects.filter(category__name='Lehenga' , homepage=1)[:8]
    data = {
        'homesaree':  homesaree,  'homekurti':  homekurti,  'homelehenga':  homelehenga 
    }
    return render(request, "index.html" , data)



def home(request):
    products = Product.objects.filter(category__name='home' , status=0)
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    productsfinal = paginator.get_page(page_number)
    totalpage = productsfinal.paginator.num_pages
    data={
        'productsdata': productsfinal,
        'totalpagelist': [n+1 for n in range(totalpage)]
    }
    return render(request, "homeappliance.html" , data)

def baby(request):
    products = Product.objects.filter(category__name='baby' , status=0)
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    productsfinal = paginator.get_page(page_number)
    totalpage = productsfinal.paginator.num_pages
    data={
        'productsdata': productsfinal,
        'totalpagelist': [n+1 for n in range(totalpage)]
    }
    return render(request, "baby.html" , data)

def cosmetics(request):
    products = Product.objects.filter(category__name='cosmetics' , status=0)
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    productsfinal = paginator.get_page(page_number)
    totalpage = productsfinal.paginator.num_pages
    data={
        'productsdata': productsfinal,
        'totalpagelist': [n+1 for n in range(totalpage)]
    }
    return render(request, "cosmeticsbeauty.html" , data)

def books(request):
    products = Product.objects.filter(category__name='books' , status=0)
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    productsfinal = paginator.get_page(page_number)
    totalpage = productsfinal.paginator.num_pages
    data={
        'productsdata': productsfinal,
        'totalpagelist': [n+1 for n in range(totalpage)]
    }
    return render(request, "books.html" , data)

def carmotorbike(request):
    products = Product.objects.filter(category__name='carmotorbike' , status=0)
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    productsfinal = paginator.get_page(page_number)
    totalpage = productsfinal.paginator.num_pages
    data={
        'productsdata': productsfinal,
        'totalpagelist': [n+1 for n in range(totalpage)]
    }
    return render(request, "carmotorbike.html" , data)

def kurti(request):
    products = Product.objects.filter(category__name='Kurti' , status=0)
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    productsfinal = paginator.get_page(page_number)
    totalpage = productsfinal.paginator.num_pages
    data={
        'productsdata': productsfinal,
        'totalpagelist': [n+1 for n in range(totalpage)]
    }
    return render(request, "kurti.html" , data)

def lehenga(request):
    products = Product.objects.filter(category__name='Lehenga' , status=0)
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    productsfinal = paginator.get_page(page_number)
    totalpage = productsfinal.paginator.num_pages
    data={
        'productsdata': productsfinal,
        'totalpagelist': [n+1 for n in range(totalpage)]
    }
    return render(request, "lehenga.html" , data)

def computers(request):
    products = Product.objects.filter(category__name='computers' , status=0)
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    productsfinal = paginator.get_page(page_number)
    totalpage = productsfinal.paginator.num_pages
    data={
        'productsdata': productsfinal,
        'totalpagelist': [n+1 for n in range(totalpage)]
    }
    return render(request, "computers.html" , data)

def fashion(request):
    products = Product.objects.filter(category__name='fashion' , status=0)
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    productsfinal = paginator.get_page(page_number)
    totalpage = productsfinal.paginator.num_pages
    data={
        'productsdata': productsfinal,
        'totalpagelist': [n+1 for n in range(totalpage)]
    }
    return render(request, "fashion.html" , data)

def grocery(request):
    products = Product.objects.filter( category__name='grocery' , status=0)
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    productsfinal = paginator.get_page(page_number)
    totalpage = productsfinal.paginator.num_pages
    data={
        'productsdata': productsfinal,
        'totalpagelist': [n+1 for n in range(totalpage)]
    }
    return render(request, "grocery.html" , data)



def pharmacy(request):
    products = Product.objects.filter( category__name='pharmacy' , status=0)
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    productsfinal = paginator.get_page(page_number)
    totalpage = productsfinal.paginator.num_pages
    data={
        'productsdata': productsfinal,
        'totalpagelist': [n+1 for n in range(totalpage)]
    }
    return render(request, "pharmacy.html" , data)

def privacy(request):
    return render(request, "privacy.html")

def saree(request):
    products = Product.objects.filter(category__name='saree' , status=0)
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    productsfinal = paginator.get_page(page_number)
    totalpage = productsfinal.paginator.num_pages
    data={
        'productsdata': productsfinal,
        'totalpagelist': [n+1 for n in range(totalpage)]
    }
    return render(request, "saree.html" , data)
             
def menwear(request):
    return render(request, "menwear.html")

def womenwear(request):
    return render(request, "womenwear.html")

def thankyou(request):
    return render(request, "thankyou.html")

def collections(request):
    category = Category.objects.filter(status=0)
    context = { 'category':category }
    return render(request , "collections.html" , context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        category_image = Category.objects.filter(slug=slug)
        context = {'products': products, 'category_name':category_name, 'category_image':category_image}
        return render(request, "products/index.html" , context)
    else:
        messages.warning(request, "No such category found")
        return redirect("index")
    
    
def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
         
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            
            context = {
                'products':products
            }
    else:
        messages.error(request, "No such category found")
        return redirect("index")
    
    
    return render(request, "productview.html" ,  context )


def productlistAjax(request):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    productsList = list(products)

    return JsonResponse(productsList, safe=False)




    # Product Search

def search(request):
    query = request.GET.get('query')
    if query != None:
        products = Product.objects.filter(name__icontains=query , status=0)
        data={
        'searchdata': products }

    else:
        return redirect("index")
        
    return render(request, 'search.html' , data)


def sitemap(request):
    return render(request, "sitemap.xml")

def contact(request):
    if request.method == 'POST':
        personname = request.POST['name']
        personemail = request.POST['email']
        personmessage = request.POST['message']
        contactdetails = contactform( personname = personname , personemail = personemail , personmessage = personmessage )
        contactdetails.save()
    return render(request, "contact.html")


