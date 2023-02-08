from django.conf.urls import url

from .views import MailView, MessageView, RecipientView

urlpatterns = [
    url(r'^recipient/', RecipientView.as_view(), name='recipient_url'),
    url(r'^message/', MessageView.as_view(), name='message_url'),
    url(r'^mail/', MailView.as_view(), name='mail_url'),
]
