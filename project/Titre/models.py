from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        chaine=f"{self.genre}"
        return chaine

    def dico(self):
        dic={"genre":self.genre}
        return dic


class Titre(models.Model):
    titre = models.CharField(max_length=100)
    directeur = models.CharField(max_length=100)
    date_parution = models.DateField(blank=True, null=True)
    duree = models.IntegerField(blank=False)
    resume = models.TextField(null=True, blank=True)
    acteur = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


    def __str__(self):
        chaine=f" Le nom du titre est {self.titre} parue en {self.date_parution}  par dirigé {self.directeur}"
        return chaine

    def get_dico(self):
        dico= {"titre" : self.titre, "directeur":self.directeur, "date_parution":self.date_parution, "duree":self.duree, "resume":self.resume, "acteur":self.acteur, "genre":self.genre}
        return dico

