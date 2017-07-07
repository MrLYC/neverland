# coding: utf-8
from django import forms
from django.forms.fields import FileField, CharField
from django.contrib import admin

from .models import Keeper


class KeeperForm(forms.ModelForm):
    data = FileField(required=False)
    text = CharField(
        max_length=1024 * 20, required=False,
        widget=forms.Textarea,
    )

    class Meta:
        model = Keeper
        exclude = (
            "data",
        )

    def __init__(self, *args, **kwargs):
        super(KeeperForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        data = self.cleaned_data.get("data")
        if data:
            self.instance.data = data.read()
        else:
            self.instance.data = self.cleaned_data.get("text", "")

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
        ("Data", {"fields": ["text", "data", "comment"]}),
        ("Visit", {"fields": ["visit_count"]}),
    ]
    ordering = ["name", "visit_count", "visited_at"]


admin.site.register(Keeper, KeeperAdmin)
