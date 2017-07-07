from django.db import models
from django.utils.timezone import now


CONTENT_TYPE_CHOICES = (
    ('text/plain', 'txt'),
    ('text/html', 'html'),
    ('text/css', 'css'),
    ('application/javascript', 'js'),
    ('application/json', 'json'),
    ('image/jpeg', 'jpeg'),
    ('image/x-icon', 'ico'),
    ('image/gif', 'gif'),
    ('application/xml', 'xml'),
    ('application/octet-stream', 'bin'),
    ('audio/aac', 'aac'),
    ('application/x-abiword', 'abw'),
    ('application/octet-stream', 'arc'),
    ('video/x-msvideo', 'avi'),
    ('application/vnd.amazon.ebook', 'azw'),
    ('application/x-bzip', 'bz'),
    ('application/x-bzip2', 'bz2'),
    ('application/x-csh', 'csh'),
    ('text/csv', 'csv'),
    ('application/msword', 'doc'),
    ('application/epub+zip', 'epub'),
    ('text/calendar', 'ics'),
    ('application/java-archive', 'jar'),
    ('audio/midi', 'mid'),
    ('video/mpeg', 'mpeg'),
    ('application/vnd.apple.installer+xml', 'mpkg'),
    ('application/vnd.oasis.opendocument.presentation', 'odp'),
    ('application/vnd.oasis.opendocument.spreadsheet', 'ods'),
    ('application/vnd.oasis.opendocument.text', 'odt'),
    ('audio/ogg', 'oga'),
    ('video/ogg', 'ogv'),
    ('application/ogg', 'ogx'),
    ('application/pdf', 'pdf'),
    ('application/vnd.ms-powerpoint', 'ppt'),
    ('application/x-rar-compressed', 'rar'),
    ('application/rtf', 'rtf'),
    ('application/x-sh', 'sh'),
    ('image/svg+xml', 'svg'),
    ('application/x-shockwave-flash', 'swf'),
    ('application/x-tar', 'tar'),
    ('image/tiff', 'tif'),
    ('application/x-font-ttf', 'ttf'),
    ('application/vnd.visio', 'vsd'),
    ('audio/x-wav', 'wav'),
    ('audio/webm', 'weba'),
    ('video/webm', 'webm'),
    ('image/webp', 'webp'),
    ('application/x-font-woff', 'woff'),
    ('application/xhtml+xml', 'xhtml'),
    ('application/vnd.ms-excel', 'xls'),
    ('application/vnd.mozilla.xul+xml', 'xul'),
    ('application/zip', 'zip'),
    ('video/3gpp', '3gp'),
    ('video/3gpp2', '3g2'),
    ('application/x-7z-compressed', '7z')
)


class Keeper(models.Model):
    update_at = models.DateTimeField(auto_now=True)

    visited_at = models.DateTimeField(auto_now_add=True)
    visit_count = models.IntegerField(default=0)

    name = models.CharField(
        max_length=255, null=False, blank=False, unique=True,
    )
    c_type = models.CharField(
        max_length=255, null=True, blank=True, choices=CONTENT_TYPE_CHOICES,
    )
    data = models.BinaryField(max_length=1024 * 20, null=True, blank=True)
    read_token = models.CharField(max_length=16, null=True, blank=True)
    write_token = models.CharField(max_length=16, null=True, blank=True)
    charset = models.CharField(
        max_length=16, null=True, blank=True, default="utf-8",
    )
    reason = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    comment = models.CharField(max_length=32, null=True, blank=True)

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

    def visit(self):
        self.visit_count += 1
        self.visited_at = now()
        self.save()
