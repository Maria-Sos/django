import datetime
from django.shortcuts import render

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "newYear/index.html", {
        "newyear": now.month == 1 and now.date == 1
    })