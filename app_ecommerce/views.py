from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,request,HttpResponseRedirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q


# Create your views here.


def product_list(request, category_slug=None):
    category = None
    category = Category.objects.all()
    #print(category)
    products = Product.objects.filter(available=True)
    #print(products)
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
    return render(request, 'mycart.html', context,{'product':product})

# def search(request):
#     if request.method=='GET':
#         template_name = 'index.html'
#         print("FDS")
#         model = Product

#         def get_queryset(self):
#             query = self.request.POST.get('Product')
#             print(query)
#             if query:
#                 product = Product.objects.filter(Q(name__icontains=Product))
#                 print(product)
#             else:
#                 products = self.model.objects.none()
#                 print("aa")
#             return render(request, 'index.html',{'products':products})
#         return render(request, 'index.html',{'products':products})

def search(request): 
   
    
    model=Product
    model=Category

    if request.method =='GET':
        product = request.GET.get('Product')
        category = request.GET.get('Category')
        
        products = Product.objects.filter(Q(name__icontains=product)|Q(category__name__icontains=product))
        # categories = Category.objects.filter(name__icontains=category)
        # print(products)
        return render(request, 'index.html',{'products':products })
    return render(request, 'index.html',{'products':products })

  
