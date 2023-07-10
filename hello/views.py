from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def greed(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

def helloname(request, name):
    return render(request, "hello/helloname.html", {
        "name": name.capitalize()
    })
