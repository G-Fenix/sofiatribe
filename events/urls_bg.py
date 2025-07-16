from . import views
from django.urls import path

urlpatterns = [
    path('minalisabitiap', views.minalisabitiap),
    path('predstoiashtisabitiau', views.predstoiashtisabitiau),
]
