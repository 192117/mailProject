# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import MailForm, MessageForm, RecipientForm


class RecipientView(FormView):

    template_name = 'mail/recipient.html'
    form_class = RecipientForm
    success_url = reverse_lazy('recipient_url')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())


class MessageView(FormView):

    template_name = 'mail/message.html'
    form_class = MessageForm
    success_url = reverse_lazy('message_url')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())


class MailView(FormView):

    template_name = 'mail/mail.html'
    form_class = MailForm
    success_url = reverse_lazy('mail_url')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())
