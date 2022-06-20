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
    template = get_template("homepage.html")
    context = {
        "nomcompagnie": "Minireference Co.",
        "pitch": "Nous utilisons Python, Git et LaTeX pour créer des livres compacts sur les maths, les sciences, et l'informatique",
    }
    html = template.render(context)
    return HttpResponse(html)
