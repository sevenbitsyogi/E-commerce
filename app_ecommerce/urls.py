from django.urls import path,include
from django.conf.urls import url
from .views import product_list,product_detail
from . import views

app_name='app_ecommerce'

urlpatterns=[
    # path('',home,name='home'),
    # path('product_list/', product_list, name='product_list'),
    #path('product_detail/',product_detail,name='product_detail'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^/search/$',views.search,name='search')

]

# from django.conf.urls import url
# from . import views

# app_name = 'app_ecommerce'

# urlpatterns = [
#     url(r'^$', views.product_list, name='product_list'),
#     url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
#     url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
# ]
