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
    pass
