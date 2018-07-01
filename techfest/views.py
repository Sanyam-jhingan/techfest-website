from django.shortcuts import render
from events.models import event


def home(request):
    events=event.objects.all()
    print(events[0].image)
    print(events)
    return render(request,"home.html",{"events":events})
def about(request):
    return render(request,"about.html")
def privacy(request):
    return render(request,"privacy.html")
