from django.shortcuts import render
from .forms import TitreForm
from . import models
from django.http import HttpResponseRedirect


def main(request):
    return render(request, 'Titre/main.html')

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



def update(request, id):
    titre = models.Titre.objects.get(pk=id)
    form = TitreForm(titre.get_dico())
    return render(request,"Titre/update.html",{"form":form,"id":id})


def traitementupdate(request, id):
    lform = TitreForm(request.POST)
    if lform.is_valid():
        Titre = lform.save(commit=False)
        Titre.id = id;
        Titre.save()
        return HttpResponseRedirect("/Titre/all")
    else:
        return render(request, "Titre/update.html", {"form": lform, "id": id})


def delete(request, id):
    models.Titre.objects.get(pk=id).delete()
    return HttpResponseRedirect("/Titre/all")
