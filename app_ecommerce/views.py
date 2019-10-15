from django.shortcuts import render
from django.http import HttpResponse,request,HttpResponseRedirect


# Create your views here.

def home(request):
    return render(request,'user/index.html')