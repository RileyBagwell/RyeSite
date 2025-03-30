from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("p3r/index.html")
    return render(request, "p3r/index.html")


def home(request):
    template = loader.get_template("p3r/home.html")
    return render(request, 'p3r/home.html')


def test(request):
    template = loader.get_template("p3r/index.html")
    return render(request, "p3r/index.html")


def about(request):
    template = loader.get_template("p3r/about-me.html")
    return render(request, "p3r/about-me.html")


def projects(request):
    template = loader.get_template("p3r/projects.html")
    return render(request, "p3r/projects.html")


def uses(request):
    template = loader.get_template("p3r/uses.html")
    return render(request, "p3r/uses.html")


def contact(request):
    template = loader.get_template("p3r/contact.html")
    return render(request, "p3r/contact.html")