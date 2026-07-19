from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('liberar/', views.liberar_bebida, name='liberar_bebida'),
]