from django.urls import path,include
from .views import home,product_list,product_detail
from . import views

urlpatterns=[
    path('',home,name='home'),
    path('product_list/', product_list, name='product_list'),
    path('product_detail/',product_detail,name='product_detail')

]