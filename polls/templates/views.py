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
