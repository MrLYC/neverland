from django.db import models
from django.utils.timezone import now


class ViewRule(models.Model):
    update_at = models.DateTimeField(auto_now=True)
    visited_at = models.DateTimeField(auto_now_add=True)
    visit_count = models.IntegerField(default=0)

    target = models.CharField(max_length=128)
    path = models.CharField(
        max_length=255, null=False, blank=False,
    )
    method = models.CharField(max_length=8, choices=[
        ("GET", "GET"),
        ("POST", "POST"),
        ("PUT", "PUT"),
        ("PATCH", "PATCH"),
        ("DELETE", "DELETE"),
    ])
    token = models.CharField(
        max_length=32, default=None, blank=False, null=True,
    )
    params = models.TextField(
        max_length=1024 * 5, default=None, blank=False, null=True,
    )

    class Meta:
        unique_together = [
            ("path", "method")
        ]

    def visit(self):
        self.visit_count += 1
        self.visited_at = now()
        self.save()
