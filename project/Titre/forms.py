from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class TitreForm(ModelForm):
    class Meta:
        model = models.Titre
        fields = ('titre', 'directeur', 'date_parution', 'duree','resume','acteur','genre')
        labels = {
            'titre' : _('titre'),
            'directeur' : _('directeur') ,
            'date_parution' : _('date de parution'),
            'duree' : _('durée'),
            'resume' : _('Résumé'),
            'acteur' : _('acteurs'),
            'genre' : _('genres'),
        }

class GenreForm(ModelForm):
    class Meta:
        model = models.Genre
        fields = ('genre',)
        labels = {
            'genre': _('genre'),
        }