# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Recipient(models.Model):

    first_name = models.CharField(
        verbose_name='Имя получателя',
        help_text='Введите имя получателя',
        max_length=75,
    )
    last_name = models.CharField(
        verbose_name='Фамилия получателя',
        help_text='Введите фамилию получателя',
        max_length=100,
    )
    birthday = models.DateField(
        verbose_name='Дата рождения получателя',
        help_text='Введите дату рождеия получателя',
    )
    email = models.EmailField(
        verbose_name='Электронная почта получателя',
        help_text='Введите электронную почту получателя',
        unique=True,
    )

    def __str__(self):
        return '{}-{}'.format(self.last_name, self.first_name)

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'


@python_2_unicode_compatible
class Message(models.Model):

    name = models.CharField(
        verbose_name='Имя макета письма',
        help_text='Введите имя для макета письма',
        max_length=100,
        unique=True,
    )
    header = models.CharField(
        verbose_name='Заголовок письма',
        help_text='Введите заголовок письма',
        max_length=100,
    )
    html_template = models.FileField(
        verbose_name='html макет письма',
        help_text='Загрузите html макет пиьсма',
        upload_to='template_mail',
        validators=[
            FileExtensionValidator(allowed_extensions=['html'])
        ]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Макет письма'
        verbose_name_plural = 'Макеты писем'


@python_2_unicode_compatible
class Mail(models.Model):

    name = models.CharField(
        verbose_name='Имя рассылки',
        help_text='Введите имя для рассылки',
        max_length=150,
        unique=True,
    )
    start_time = models.DateTimeField(
        verbose_name='Дата и время начала рассылки'
    )
    message = models.ForeignKey(
        Message,
        null=True,
        on_delete=models.SET_NULL,
        related_name='mail',
        verbose_name='Макет письма'
    )
    recipients = models.ManyToManyField(
        to=Recipient,
        related_name='recipients',
        blank=True,
        verbose_name='Получатели',
    )
    sent = models.BooleanField(
        verbose_name='Статус выполнения рассылки',
        help_text='Введите cтатус выполнения рассылки',
        default=False,
    )

    def __str__(self):
        return '{}: {}'.format(self.name, self.start_time)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
