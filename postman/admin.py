# coding: utf-8

from django.contrib import admin
from postman.models import EmailSettings


class EmailSettingsAdmin(admin.ModelAdmin):
    list_display = [
        "sender", "auth_user", "smtp_server",
        "visit_count", "visited_at", "update_at",
    ]
    list_filter = ["update_at", "visited_at", "smtp_server", "sender"]
    search_fields = [
        "api_key", "smtp_server", "auth_user",
        "update_at", "visited_at", "sender",
    ]
    fieldsets = [
        (None, {"fields": ["sender", "api_key", "receiver_pattern"]}),
        ("Auth", {"fields": [
            "auth_user", "auth_password", "smtp_server", "smtp_port",
        ]}),
        ("Visit", {"fields": ["visit_count"]}),
    ]
    ordering = ["smtp_server", "visit_count", "visited_at"]


admin.site.register(EmailSettings, EmailSettingsAdmin)
