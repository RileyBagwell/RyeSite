from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    template = loader.get_template("polls/home.html")
    return render(request, 'polls/home.html')


def test(request):
    template = loader.get_template("polls/test.html")
    return render(request, "polls/test.html")


def about(request):
    template = loader.get_template("polls/about-me.html")
    return render(request, "polls/about-me.html")


def projects(request):
    template = loader.get_template("polls/projects.html")
    return render(request, "polls/projects.html")


def uses(request):
    template = loader.get_template("polls/uses.html")
    return render(request, "polls/uses.html")


def contact(request):
    template = loader.get_template("polls/contact.html")
    return render(request, "polls/contact.html")