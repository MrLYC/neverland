from django.db import models


class Keeper(models.Model):
    update_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    content_type = models.CharField(
        max_length=255, choices=(
            ('application/json', 'application/json'),
            ('text/html', 'text/html'),
            ('text/plain', 'text/plain'),
            ('application/octet-stream', 'application/octet-stream'),
        )
    )
    data = models.CharField(max_length=5120)
    token = models.CharField(max_length=16, null=True, blank=True)
    charset = models.CharField(max_length=16, null=True, blank=True)
    reason = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
