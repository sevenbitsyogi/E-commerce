from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,request,HttpResponseRedirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic import TemplateView, ListView



# Create your views here.


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

def product_detail(request,id,slug):
    product = get_object_or_404(Product, id=id, slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'mycart.html', context)

class search_results(ListView):
    model = Product
    template_name = 'search_results.html'
    queryset = Product.objects.filter(name__icontains='Boston')
