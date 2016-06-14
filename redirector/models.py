from django.db import models
from django.utils.timezone import now


class UrlMapping(models.Model):
    update_at = models.DateTimeField(auto_now=True)

    visited_at = models.DateTimeField( auto_now_add=True)
    visit_count = models.IntegerField(default=0)

    alias = models.CharField(max_length=255, null=False, blank=False)
    raw_url = models.CharField(max_length=255, null=False, blank=False)
    comment = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return self.alias

    def visit(self):
        self.visit_count += 1
        self.visited_at = now()
        self.save()
