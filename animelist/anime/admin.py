from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Anime

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('name', 'producer', 'release_date', 'image_preview')
    fields = ('name', 'description', 'producer', 'release_date', 'image')
    readonly_fields = ('image_preview',)
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "(No image)"

    image_preview.short_description = "Image Preview"

