from django.urls import path

from . import views

app_name = "newYear"
urlpatterns = [
    path("", views.index, name="index")
]