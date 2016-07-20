# coding: utf-8

from django.views import generic
from django import forms
from django.http import HttpResponseForbidden, HttpResponse

from postman.models import EmailSettings

from ycyc.tools.email_tools import EMail


class MailInfoForm(forms.Form):
    api_key = forms.CharField(
        min_length=1, max_length=32,
        label=u"api key",
    )

    receiver = forms.CharField(
        min_length=5, max_length=256,
        label=u"email receivers",
    )
    subject = forms.CharField(
        max_length=256,
        label=u"email subject",
    )
    content = forms.CharField(
        max_length=100 * 1024,
        label=u"email content",
    )


class MailToView(generic.View):

    def post(self, request, sender):
        form = MailInfoForm(request.POST)

        if not form.is_valid():
            return HttpResponseForbidden("form valid failed")

        data = form.clean()
        api_key = data.get("api_key")
        if not api_key:
            return HttpResponse("authenticate failed", status=401)

        email_settings = EmailSettings.objects.filter(
            sender=sender, api_key=api_key,
        ).first()
        if not email_settings:
            return HttpResponse("authenticate failed", status=401)

        receivers = [
            i.strip()
            for i in data.get("receiver", "").split(",")
            if i.strip()
        ]
        if not receivers:
            return HttpResponseForbidden("receiver can not be empty")

        email = EMail(
            server=email_settings.smtp_server,
            sender=email_settings.sender or email_settings.auth_user,
            receiver=receivers, subtype=EMail.SubType.HTML,
            subject=data.get("subject"), content=data.get("content"),
        )

        try:
            email.send(
                user=email_settings.auth_user,
                passwd=email_settings.auth_password,
            )
        except Exception as err:
            return HttpResponseForbidden(str(err))
        return HttpResponse("ok")
