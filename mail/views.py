# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import MailForm, MessageForm, RecipientForm


def get_resipient(request):
    if request.method == 'POST':
        form = RecipientForm(request.POST)
        if form.is_valid():
            return render(request, 'success.html')
    else:
        form = RecipientForm()
    return render(request, 'mail/recipient.html', {'form': form})


def get_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            return render(request, 'success.html')
    else:
        form = MessageForm()
    return render(request, 'mail/message.html', {'form': form})


def get_mail(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            return render(request, 'success.html')
    else:
        form = MailForm()
    return render(request, 'mail/mail.html', {'form': form})
