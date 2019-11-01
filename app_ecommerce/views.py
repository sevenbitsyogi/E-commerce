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

  
# def search(request):
#     model=Product
#     if request.method =='GET':
#         query= request.GET.get('q')

#         if query is not None:
#             #lookups= Q(name__icontains=query) | Q(category__icontains=query)
#             results=Product.objects.filter(Q(name__icontains=query))
#             return render(request, 'index.html',{'results':results })
#         return render(request, 'index.html',{'results':results })
#         return render(request, 'index.html',{'products':products })

    
# class SearchView(ListView):
#     template_name = 'user/index.html'
#     paginate_by = 20
#     count = 0
    
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['count'] = self.count or 0
#         context['query'] = self.request.GET.get('q')
#         return context

#     def get_queryset(self):
#         request = self.request
#         query = request.GET.get('q', None)
        
#         if query is not None:
#             product_results = Product.objects.search(query)
            
#             # combine querysets 
#             # queryset_chain = chain(
#             #         blog_results,
#             #         lesson_results,
#             #         profile_results
#             # )        
#             qs = sorted(product_results, 
#                         key=lambda instance: instance.pk, 
#                         reverse=True)
#             self.count = len(qs) # since qs is actually a list
#             return qs
#         return Post.objects.none() 