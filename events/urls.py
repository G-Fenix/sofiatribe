from . import views
from django.urls import path

urlpatterns = [
    path('past-events', views.pastevents),
    path('upcoming-events', views.upcomingevents),
]
