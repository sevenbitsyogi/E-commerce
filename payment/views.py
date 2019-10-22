from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order


#from .models import Product, Order, LineItem
#from .forms import CartForm, CheckoutForm

# Create your views here.
@csrf_exempt
def payment_done(request):
    return render(request, 'payment/payment_done.html')
 
 
@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/payment_cancelled.html')


def process_payment(request):
    order = request.session.get('order.id')
    print(order)
    order = get_object_or_404(Order, id=order)
    host = request.get_host()
 
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % Decimal(order.get_total_cost()).quantize(Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'INR',
        'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,redirect('/payment_done')),                                           
        'cancel_return': 'http://{}{}'.format(host,redirect('/payment_cancelled')),                                              
    }
 
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process_payment.html', {'order': order, 'form': form})

