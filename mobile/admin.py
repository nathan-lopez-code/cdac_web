from django.contrib import admin
from .models import Information


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'titre', 'description',
        'date_de_creation', 'source',
        'image',
    ]
