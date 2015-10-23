from django.contrib import admin

from .models import UrlMapping


class UrlMappingAdmin(admin.ModelAdmin):
    fields = ['alias', 'raw_url']
    list_display = ['alias', 'raw_url', 'update_at']
    list_filter = ['update_at']
    search_fields = ['alias', 'raw_url', 'update_at']
    

admin.site.register(UrlMapping, UrlMappingAdmin)
