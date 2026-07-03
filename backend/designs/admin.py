from django.contrib.admin.views import autocomplete
from django.contrib import admin
from .models import Design, Sector
from django.utils.html import format_html

class SectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class DesignAdmin(admin.ModelAdmin):
    list_display = ('name', "thumbnail", "slug", 'display_sectors')
    search_fields = ('name', "slug", "url")
    autocomplete_fields = ('sectors',)

    def thumbnail(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.thumbnail.url)
    
    def display_sectors(self, obj):
        return ", ".join([sector.name for sector in obj.sectors.all()])

    display_sectors.short_description = 'Sectors'

# Register your models here.
admin.site.register(Design, DesignAdmin)
admin.site.register(Sector, SectorAdmin)
