from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,request,HttpResponseRedirect
from .models import Category, Product
from cart.forms import CartAddProductForm



# Create your views here.

def home(request):
    return render(request,'user/index.html')

def product_list(request, category_slug=None):
    category = None
    category = Category.objects.all()
    print(category)
    products = Product.objects.filter(available=True)
    print(products)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)


    context = {
        'category': category,
        #'categories': categories,
        'products': products
    }
    return render(request, 'index.html',{'category':category,'products':products})

def product_detail(request):
    product = get_object_or_404(Product, id=id,available=True)
    cart_product_form = CartAddProductForm()
    products = Product.objects.filter(available=True)
    print(products)
    context = {
        'products': products,
        'cart_product_form': cart_product_form
    }
    return render(request, 'user/mycart.html',{'products':products})
