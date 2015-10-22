from django.contrib import admin
from .models import Expo, Vente, Bijoux


@admin.register(Expo)
class ExpoAdmin(admin.ModelAdmin):
    pass


@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    pass


@admin.register(Bijoux)
class BijouxAdmin(admin.ModelAdmin):
    exclude = ('processed', 'processed_path')
    readonly_fields = ('image_tag',)
