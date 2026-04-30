from django.urls import path
from app_recepcao import views

urlpatterns = [
    path('', views.index, name='index'),
    path('salvar/', views.salvar, name='salvar'), # O name='salvar' é o que o HTML procura
    path('sucesso/', views.sucesso, name='sucesso'),
]