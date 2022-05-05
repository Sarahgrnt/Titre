from django.shortcuts import render
from .forms import TitreForm
from . import models

def index(request):
    return render(request, 'Titre/formulaire.html')

def formulaire(request):
    if request.method == "POST":
        form = TitreForm(request)
        if form.is_valid():
            titre = form.save()
            return render(request,"Titre/home.html",{"Titre" : titre})
        else:
            return render(request,"Titre/formulaire.html",{"form": form})
    else :
        form = TitreForm()
        return render(request,"Titre/formulaire.html",{"form" : form})

def home(request, id):
    titre = models.Titre.objects.get(pk=id)
    return render(request,"Titre/home.html",{"titre": titre})

def all(request):
    titre = list(models.Titre.objects.all())
    return render(request,"Titre/all.html",{"titre":titre})

def traitement(request):
    lform = TitreForm(request.POST)
    if lform.is_valid():
        Titre = lform.save()
        return render(request,"Titre/home.html",{"Titre": Titre})
    else:
        return render(request,"Titre/formulaire.html",{"form": lform})