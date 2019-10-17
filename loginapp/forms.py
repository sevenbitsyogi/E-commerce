from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class SignUpForm(UserCreationForm):
   email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
   class Meta:
       model = User
       fields = ('username', 'email', 'password1', 'password2')


class LoginForm(UserCreationForm):
    username = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',required = True)
    class Meta:
        model = User
        fields = ('username','password')

    # def clean(self):

    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #     user=authenticate(username=username,password=password)
    #     if not user:
    #         raise forms.ValidationError("This user does not exist")

class PasswordResetRequestForm(UserCreationForm):
   email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')