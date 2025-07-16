"""sofiatribe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

def index(request):
    return render(request, "index.html")


def nachalnai(request):
    return render(request, "nachalnai.html")

urlpatterns = [
    path('', index),
    path('index/', index),
    path('events/', include('events.urls')),
    path('gallery/', include('gallery.urls')),
    path('contact-us/', include('contactus.urls')),
    path('who-we-are/', include('whoweare.urls')),
    path('bg/', nachalnai),
    path('bg/nachalnai/', nachalnai),
    path('bg/sabitia/', include('events.urls_bg')),
    path('bg/galeria/', include('gallery.urls_bg')),
    path('bg/svurjetesesnas/', include('contactus.urls_bg')),
    path('bg/koismenie/', include('whoweare.urls_bg')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
