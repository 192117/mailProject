import datetime

from django.core.mail import get_connection, send_mail
from django.template.loader import get_template

from mail.models import Mail
from mailProject.settings import (EMAIL_HOST, EMAIL_HOST_PASSWORD,
                                  EMAIL_HOST_USER, EMAIL_PORT, EMAIL_USE_SSL)

from .celeryapp import app


@app.task
def task_send_mail():
    now = datetime.datetime.now()
    mails = Mail.objects.filter(sent=False).filter(start_time__lte=now)
    for mail in mails:
        recipients = list(mail.recipients.values())
        for recipient in recipients:
            connection = get_connection(host=EMAIL_HOST, port=EMAIL_PORT,
                                        username=EMAIL_HOST_USER, password=EMAIL_HOST_PASSWORD,
                                        use_ssl=EMAIL_USE_SSL, )
            context = {
                'first_name': recipient['first_name'],
                'last_name': recipient['last_name'],
                'birthday': recipient['birthday'],
            }
            send_mail(mail.message.header, 'blabla', EMAIL_HOST_USER, (recipient['email'],),
                      connection=connection, html_message=get_template(mail.message.html_template).render(context)
                      )
        mail.sent = True
        mail.save()
