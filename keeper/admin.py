from django.contrib import admin

from .models import Keeper


class KeeperAdmin(admin.ModelAdmin):
    list_display = [
        "name", "c_type", "visit_count", "visited_at", "update_at",
    ]
    list_filter = ["update_at", "visited_at"]
    search_fields = ["name", "c_type", "update_at", "visited_at"]
    fieldsets = [
        (None, {"fields": [
            "name", "c_type", "read_token","write_token",
            "charset", "reason", "status",
        ]}),
        ("Data", {"fields": ["data"]}),
        ("Visit", {"fields": ["visit_count"]}),
    ]
    ordering = [ "-visit_count", "-visited_at"]


admin.site.register(Keeper, KeeperAdmin)