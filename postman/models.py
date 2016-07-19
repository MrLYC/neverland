# coding: utf-8

import uuid

from django.db import models


class EmailSettings(models.Model):
    update_at = models.DateTimeField(auto_now=True)
    visited_at = models.DateTimeField(auto_now_add=True)

    visit_count = models.IntegerField(default=0)
    api_key = models.CharField(
        max_length=32, default=None, null=False, db_index=True, blank=True
    )
    receiver_pattern = models.CharField(max_length=128, blank=True, default="")
    auth_user = models.CharField(max_length=64, blank=True, default="")
    auth_password = models.CharField(max_length=64, blank=True, default="")
    sender = models.CharField(max_length=64, null=True, unique=True)

    smtp_server = models.CharField(max_length=64)
    smtp_port = models.IntegerField(default=465)

    def save(self, *args, **kwargs):
        if not self.api_key:
            uuid_key = uuid.uuid4()
            self.api_key = uuid_key.hex
        return super(EmailSettings, self).save(*args, **kwargs)

    def visit(self):
        self.visit_count += 1
        self.save()
