from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.

def hello(request):
    msg = "Salut Montréal!"
    return HttpResponse(msg)

def homepage(request):
    template = get_template("base.html")
    html = template.render()
    return HttpResponse(html)
