from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import user_login,signup,password_reset,activate_account

app_name='loginapp'

urlpatterns=[
    #path('',login,name='login'),
    url('signup/',signup,name='signup'),
    url(r'^login/$',user_login,name='login'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name = "forget7.html",email_template_name = 'registrations/password_reset_email.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = "registrations/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "registrations/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = "registrations/password_reset_complete.html"), name='password_reset_complete'),
    url(r'^activate_account/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',activate_account, name='activate_account'),
]