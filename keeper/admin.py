# coding: utf-8
from django.forms import ModelForm, FileField
from django.contrib import admin

from .models import Keeper


class KeeperForm(ModelForm):
    file_data = FileField(required=False)

    class Meta:
        model = Keeper
        exclude = ()

    def save(self, *args, **kwargs):
        file_data = self.cleaned_data.get("file_data")
        if file_data:
            self.instance.data = file_data.read()

        return super(KeeperForm, self).save(*args, **kwargs)


class KeeperAdmin(admin.ModelAdmin):
    form = KeeperForm
    list_display = [
        "name", "comment", "c_type", "visit_count", "visited_at", "update_at",
    ]
    list_filter = ["update_at", "visited_at"]
    search_fields = ["name", "c_type", "update_at", "visited_at"]
    fieldsets = [
        (None, {"fields": [
            "name", "c_type", "read_token", "write_token",
            "charset", "reason", "status",
        ]}),
        ("Data", {"fields": ["data", "file_data", "comment"]}),
        ("Visit", {"fields": ["visit_count"]}),
    ]
    ordering = ["name", "visit_count", "visited_at"]


admin.site.register(Keeper, KeeperAdmin)
