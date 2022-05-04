from django.db import models

class Titre(models.Model):
    titre = models.CharField(max_length=100)
    directeur = models.CharField(max_length=100)
    date_parution = models.DateField(blank=True, null=True)
    duree = models.IntegerField(blank=False)
    resume = models.TextField(null=True, blank=True)
    acteur= models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def __str__(self):
        chaine=f" Le nom du titre est {self.nom} parue en {self.date_parution}  par dirigé{self.directeur}"
        return chaine
