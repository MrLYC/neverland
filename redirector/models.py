from django.db import models


class UrlMapping(models.Model):
    update_at = models.DateTimeField(auto_now=True)
    alias = models.CharField(max_length=255, null=False, blank=False)
    raw_url = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.alias
