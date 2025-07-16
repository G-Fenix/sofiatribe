from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message here...',
                'rows': 5
            }),
        }


class SobshtenieZaKontaktForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Въведете пълното си име'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Въведете своя имейл'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишете своето съобщение тук...',
                'rows': 5
            }),
        }
        labels = {
            'full_name': 'Пълно име',
            'email': 'Имейл',
            'message': 'Съобщение',
        }
