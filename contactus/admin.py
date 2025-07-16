from django.contrib import admin
from .models import ContactMessage
import csv
from django.http import HttpResponse

def export_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=ContactMessages.csv'
    writer = csv.writer(response)
    writer.writerow(field_names)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response
export_as_csv.short_description = "Export selected messages to CSV"

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'language', 'created_at')
    list_filter = ('language', 'created_at')  
    search_fields = ('full_name', 'email', 'message')
    actions = [export_as_csv]

