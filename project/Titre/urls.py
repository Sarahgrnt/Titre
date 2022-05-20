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
    path('',views.main),
    path('detail/<int:id>/', views.details),
    path('forms/',views.forms),
    path('upgenre/<int:id>/',views.upgenre),
    path('idk/',views.idk),
    path('supp/<int:id>/',views.supp),
    path('traitementupdategenre/<int:id>/',views.traitementupdategenre),
    path('genre/',views.forms),
    path('triegenre/', views.triegenre),
    path('allgenre/',views.allgenre),
    path('main/',views.main),
]