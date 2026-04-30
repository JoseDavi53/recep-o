from django.urls import path
from app_recepcao import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sorteio/', views.sorteio, name='sorteio'),
    path('sucesso/', views.sucesso, name='sucesso'),
    # ESTA É A LINHA QUE ESTÁ FALTANDO:
    path('salvar/', views.salvar, name='salvar'), 
]