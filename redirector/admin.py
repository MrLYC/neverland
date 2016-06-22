from django.contrib import admin

from .models import UrlMapping


class UrlMappingAdmin(admin.ModelAdmin):
    list_display = [
        "alias", "raw_url", "comment", "visit_count",
        "visited_at", "update_at",
    ]
    list_filter = ["update_at", "visited_at"]
    search_fields = ["alias", "raw_url", "update_at", "visited_at"]
    fieldsets = [
        (None, {"fields": ["alias", "raw_url", "comment"]}),
        ("Visit", {"fields": ["visit_count"]}),
    ]
    ordering = ["alias", "visit_count", "visited_at"]


admin.site.register(UrlMapping, UrlMappingAdmin)
