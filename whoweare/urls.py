from . import views
from django.urls import path

urlpatterns = [
    path('', views.whoweare),
    path('who-we-are', views.whoweare),
]
