from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email' , 'date_sent']
    list_display_links = ['email' , 'date_sent'] 
    search_fields = ['name', 'email' , 'date_sent']