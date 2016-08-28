from django.contrib import admin
from django import forms

from .models import ViewRule
from .register import Targets


class ViewRuleForm(forms.ModelForm):
    target = forms.ChoiceField()

    class Meta:
        model = ViewRule
        fields = [
            "target", "path", "method",
            "token", "params",
            "visit_count",
        ]

    def __init__(self, *args, **kwargs):
        super(ViewRuleForm, self).__init__(*args, **kwargs)
        self.fields["token"].required = False
        self.fields["params"].required = False
        self.fields['target'].choices = [
            (k, i.description)
            for k, i in Targets.items()
        ]


class ViewRuleAdmin(admin.ModelAdmin):
    form = ViewRuleForm
    list_display = [
        "path", "target", "method", "visit_count", "visited_at", "update_at",
    ]
    list_filter = ["path", "target", "method", "update_at", "visited_at"]
    search_fields = ["path", "target", "method", "update_at", "visited_at"]
    fieldsets = [
        (None, {"fields": [
            "target", "path", "method", "token", "params",
        ]}),
        ("Visit", {"fields": ["visit_count"]}),
    ]
    ordering = ["path", "target", "update_at"]

admin.site.register(ViewRule, ViewRuleAdmin)
