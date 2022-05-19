from django.shortcuts import render
from .forms import TitreForm
from .forms import GenreForm
from . import models
from django.http import HttpResponseRedirect


def main(request):
    return render(request,'Titre/main.html')

def details(request, id):
    titre = models.Titre.objects.get(pk=id)
    form = TitreForm(titre.get_dico())
    return render(request,"Titre/detail.html",{"form":form,"id":id})

def formulaire(request):
    if request.method == "POST":
        form = TitreForm(request)
        if form.is_valid():
            titre = form.save()
            return render(request,"all/home.html",{"Titre" : titre})
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

def triegenre(request):
    genre = list(models.Genre.objects.all())
    return render(request,"Titre/triegenre.html",{"genre":genre})


def forms(request):
    if request.method == "POST":
        form = GenreForm(request)
        if form.is_valid():
            genre = form.save()
            return render(request,"Titre/main.html",{"genre" : genre})
        else:
            return render(request,"Titre/genre.html",{"form": form})
    else :
        form = GenreForm()
        return render(request,"Titre/genre.html",{"form" : form})


def idk(request):
    lform = GenreForm(request.POST)
    if lform.is_valid():
        genre = lform.save()
        return render(request,"Titre/triegenre.html",{"Genre": genre})
    else:
        return render(request,"Titre/genre.html",{"form": lform})


def upgenre(request, id):
    genre = models.Genre.objects.get(pk=id)
    form = GenreForm(genre.get_dic())
    return render(request,"Titre/upgenre.html",{"form":form,"id":id})


def traitementupdategenre(request, id):
    lform = GenreForm(request.POST)
    if lform.is_valid():
        Genre = lform.save(commit=False)
        Genre.id = id;
        Genre.save()
        return HttpResponseRedirect("/Titre/all")
    else:
        return render(request, "Titre/upgenre.html", {"form": lform, "id": id})


def supp(request, id):
    models.Genre.objects.get(pk=id).delete()
    return HttpResponseRedirect("/Titre/allgenre")

def allgenre(request):
    genre = list(models.Genre.objects.all())
    return render(request,"Titre/allgenre.html",{"genre":genre})
