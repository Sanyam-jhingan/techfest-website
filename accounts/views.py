from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import student
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
def log_in(request):
    return render(request,"accounts/login.html")

def sign_up(request):
    if request.method=="POST":
        form=student(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            pasword=form.cleaned_data["Password1"]

            user=User.objects.create_user(username=username,password=pasword)
            messages.success(request, 'account created')
            return HttpResponseRedirect(reverse("account:login"))
    else:
        form=student()

        return render(request,"accounts/register.html",{'form':form})
