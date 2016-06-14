from django.db import models


class Keeper(models.Model):
    update_at = models.DateTimeField(auto_now=True)
    name = models.CharField(
        max_length=255, null=False, blank=False, unique=True,
    )
    c_type = models.CharField(
        max_length=255, null=True, blank=True, choices=(
            ('application/json', 'application/json'),
            ('text/html', 'text/html'),
            ('text/plain', 'text/plain'),
            ('application/octet-stream', 'application/octet-stream'),
        )
    )

    data = models.TextField(max_length=1024 * 20, null=True, blank=True)
    read_token = models.CharField(max_length=16, null=True, blank=True)
    write_token = models.CharField(max_length=16, null=True, blank=True)
    charset = models.CharField(
        max_length=16, null=True, blank=True, default="utf-8",
    )
    reason = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)

    @property
    def content_type(self):
        content_type = self.c_type
        if not content_type:
            return content_type

        if self.charset:
            content_type = "%s; charset=%s" % (content_type, self.charset)
        return content_type

    def __str__(self):
        return self.name

    def save(self):
        if self.charset and isinstance(self.data, bytes):
            try:
                self.data = self.data.decode(self.charset)
            except UnicodeDecodeError:
                pass
        return super(Keeper, self).save()
