from . import views
from django.urls import path

urlpatterns = [
    path('', views.contactus, name='contactus'),
    path('contact-us/', views.contactus, name='contactus'),
    path('svurjetesesnas/', views.svurjetesesnas, name='svurjetesesnas'),
]
