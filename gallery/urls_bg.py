from . import views
from django.urls import path

urlpatterns = [
    path('foto', views.foto),
    path('galeria', views.galeria),
]

