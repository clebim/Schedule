from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/<int:id>', views.store, name='store'),
    path('busca/', views.busca, name='busca'),
] 
