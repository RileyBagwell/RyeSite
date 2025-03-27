from django.urls import path

from .templates import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("test", views.test, name="test"),
    path("about", views.about, name="about"),
    path("projects", views.projects, name="projects"),
    path("uses", views.uses, name="uses"),
    path("contact", views.contact, name="contact"),
]
