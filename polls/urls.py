from django.urls import path

from .templates import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("test", views.test, name="test")
]
