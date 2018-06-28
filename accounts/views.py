from django.shortcuts import render
def log_in(request):
    return render(request,"accounts/login.html")

def sign_up(request):
    return render(request,"accounts/register.html")
