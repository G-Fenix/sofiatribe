from . import views
from django.urls import path

urlpatterns = [
    path('photo', views.photo),
    path('video', views.video),
]

