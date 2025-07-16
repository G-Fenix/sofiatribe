from django.shortcuts import render

def photo(request):
    return render(request, 'photo.html')

def video(request):
    return render(request, 'video.html')

def foto(request):
    return render(request, 'foto.html')

def galeria(request):
    return render(request, 'galeria.html')