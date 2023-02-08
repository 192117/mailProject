import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailProject.settings')

app = Celery('mail')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.task_serializer = 'pickle'
app.conf.accept_content = ['application/json', 'application/x-python-serialize']

app.conf.beat_schedule = {
    'task_send_mail': {
        'task': 'mail.tasks.task_send_mail',
        'schedule': crontab(),
    },
}
