from django.shortcuts import render, redirect
from django.http import HttpResponse

from Module.models import enquiry_table
from Module.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    if request.method == "POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('subject')
        d=request.POST.get('message')
        enquiry=enquiry_table(name=a,email=b,subject=c,message=d)
        enquiry.save()

        messages.success(request,'Enquiry Form Submitted Succesfully..')
    return render(request,'index.html')