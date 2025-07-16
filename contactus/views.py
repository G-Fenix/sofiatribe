from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm, SobshtenieZaKontaktForm

def contactus(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.language = 'en'  # ✅ İngilizce olduğunu kaydet
            obj.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contactus')
    else:
        form = ContactMessageForm()
    return render(request, 'contactus.html', {'form': form})

def svurjetesesnas(request):
    if request.method == 'POST':
        form = SobshtenieZaKontaktForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.language = 'bg'  # ✅ Bulgarca olduğunu kaydet
            obj.save()
            messages.success(request, "Săobshtenieto vi be izprateno uspeshno!")
            return redirect('svurjetesesnas')
    else:
        form = SobshtenieZaKontaktForm()
    return render(request, 'svurjetesesnas.html', {'form': form})
