from django.conf.urls import url

from .views import get_resipient, get_mail, get_message

urlpatterns = [
    url(r'^recipient/', get_resipient, name='recipient_url'),
    url(r'^message/', get_message, name='message_url'),
    url(r'^mail/', get_mail, name='mail_url'),
]
