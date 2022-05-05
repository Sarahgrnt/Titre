from django.urls import path
from . import views

urlpatterns = [
    path('formulaire/',views.formulaire),
    path('home/',views.home),
    path('traitement/', views.traitement),
    path('all/',views.all),
    path('update/<int:id>/',views.update),
    path('traitementupdate/<int:id>/',views.traitementupdate),
    path('delete/<int:id>/',views.delete),
]