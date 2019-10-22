from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from . import views

app_name='payment'

urlpatterns=[
    url(r'^payment/', include('paypal.standard.ipn.urls')),
    url(r'^process_payment/$', views.process_payment, name='process_payment'),
    url(r'^payment_done/$', views.payment_done, name='payment_done'),
    url('payment_cancelled/', views.payment_canceled, name='payment_cancelled'),

]