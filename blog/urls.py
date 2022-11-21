from django.urls import path
from . import views

urlpatterns = [
    path('animal/<str:id_animal>/', views.animal_detail, name='animal_detail'),
    path('Tic/', views.Tic, name='Tic'),
    path('Pocahontas/', views.Pocahontas, name='Pocahontas'),
    path('Totora/', views.Totora, name='Totora'),
    path('Patrick/', views.Patrick, name='Patrick'),
    path('Tac/', views.Tac, name='Tac'),
    path('', views.animaux, name='Animaux'),
]