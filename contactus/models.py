from django.db import models

class ContactMessage(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('bg', 'Bulgarian'),
    ]

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='en')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email} ({self.get_language_display()})"
    

