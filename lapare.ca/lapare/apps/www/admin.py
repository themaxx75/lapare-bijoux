from django.contrib import admin

from .models import Bijoux, Expo, Vente


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

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('image',)
        return self.readonly_fields
