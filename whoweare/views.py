from django.shortcuts import render

def whoweare(request):
    return render(request, 'whoweare.html')

def koismenie(request):
    return render(request, 'koismenie.html')
