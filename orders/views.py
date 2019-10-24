from django.shortcuts import render,redirect
from django.urls import reverse
#from .tasks import order_created
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.
def order_create(request):
    cart=Cart(request)
    if request.method=='POST':
        form=OrderCreateForm(request.POST)
        if form.is_valid():
            order=form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            #order_created.delay(order.id)
            request.session['order.id']=order.id
            return redirect('/payment/process_payment')
        return render(request,'/payment/payment_done.html')
        #return render(request,'orders/order/created.html',{'order':order})
    else:
        form=OrderCreateForm()
    return render(request,'orders/order/create.html',{'form':form,'cart':cart})