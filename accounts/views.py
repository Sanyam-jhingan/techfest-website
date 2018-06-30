from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import student
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
def log_in(request):

        if request.method=="POST":
            print(request.POST)
            u=request.POST.get("username")
            p=request.POST.get("password")
            user=authenticate(request,username=u,password=p)
            if user is not None:
                login(request,user)
                messages.success(request, ' Welcome to TechFest '+ u )
                return HttpResponseRedirect(reverse('home'))
        return render(request,'accounts/login.html')


def sign_up(request):
    if request.method=="POST":
        form=student(request.POST)

        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["Password1"]
            email=form.cleaned_data["email"]

            user=User.objects.create_user(username=username,password=password,email=email)
            messages.success(request,'account created')
        
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        form=student()

        return render(request,"accounts/register.html",{'form':form})
