from django.urls import path
from django.contrib.auth import views as auth_views

from .views import user_login,signup,password_reset

urlpatterns=[
    #path('',login,name='login'),
    path('signup/',signup,name='signup'),
    path('login/',user_login,name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = "forget7.html",email_template_name = 'registrations/password_reset_email.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = "registrations/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "registrations/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = "registrations/password_reset_complete.html"), name='password_reset_complete'),
]