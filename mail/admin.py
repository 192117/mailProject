# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Mail, Message, Recipient

admin.site.register(Message)
admin.site.register(Recipient)
admin.site.register(Mail)
