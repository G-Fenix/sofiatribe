from django.shortcuts import render

def upcomingevents(request):
    return render(request, 'upcomingevents.html')

def pastevents(request):
    return render(request, 'pastevents.html')

def minalisabitiap(request):
    return render(request, 'minalisabitiap.html')

def predstoiashtisabitiau(request):
    return render(request, 'predstoiashtisabitiau.html')