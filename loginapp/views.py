from django.shortcuts import render,redirect
from django.http import HttpResponse,request,HttpResponseRedirect
from .forms import SignUpForm,LoginForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.core.mail import EmailMessage



# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        username = request.POST.get('username')
        print(username)
        email = request.POST.get('email')
        print(email)
        password1 = request.POST.get('password1')
        print(password1)
        password2 = request.POST.get('password2')
        print(password2)
        if form.is_valid():
            print(form.is_valid())
            user = form.save(commit=False)
            user.is_active = False
            
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('accounts/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
        else:
            print("form not valid")
    else:
       form = SignUpForm()
    return render(request, 'register7.html', {'form': form})



def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Your account has been activate successfully')
    else:
        return HttpResponse('Activation link is invalid!')


def user_login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/login")
                else:
                    return HttpResponse("You're account is disabled.")
            else:
                print("invalid login details " + username + " " + password)
                return render(request,'login7.html')
        else:
            return render(request,'login7.html')


def password_reset(request):
    return render(request,"forget7.html")
   