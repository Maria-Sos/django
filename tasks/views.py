from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

class NewTasksForm(forms.Form):
    task = forms.CharField(label="New Task", 
                           widget=forms.TextInput(attrs={'style': 
                                                         'width: 600px;' 
                                                         'border-radius: 17px;'
                                                         'padding: 10px;'
                                                         'marging: 0px 0px 15px;'
                                                         'font-family: sans-serif'
                                                         'font-size: 15px;'
                                                         }))
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTasksForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
             return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTasksForm()
    })