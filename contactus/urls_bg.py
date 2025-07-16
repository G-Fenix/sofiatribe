from . import views
from django.urls import path

urlpatterns = [
    path('', views.svurjetesesnas, name='contactus'),
    path('svurjetesesnas/', views.svurjetesesnas, name='svurjetesesnas'),
]
