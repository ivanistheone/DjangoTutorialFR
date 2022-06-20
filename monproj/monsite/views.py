from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.

def hello(request):
    if "nom" in request.GET:
        nom = request.GET["nom"]
    else:
        nom = "Montréal"
    msg = "Salut " + nom + "!"
    return HttpResponse(msg)

def homepage(request):
    template = get_template("base.html")
    context = {
        "nom": "Montréal"
    }
    html = template.render(context)
    return HttpResponse(html)
