import datetime

from django import forms

from mail.models import Mail, Message, Recipient


class RecipientForm(forms.ModelForm):

    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'first_name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'last_name'}))
    birthday = forms.DateField(label='', widget=forms.TextInput(attrs={'placeholder': 'birthday'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'email'}))

    class Meta:
        model = Recipient
        fields = ('first_name', 'last_name', 'birthday', 'email')


class MessageForm(forms.ModelForm):

    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'name'}))
    header = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'header'}))
    message = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'message'}))
    html_template = forms.FileField(label='', widget=forms.FileInput(attrs={'placeholder': 'html_template'}))

    class Meta:
        model = Message
        fields = ('name', 'header', 'message', 'html_template')


class MailForm(forms.ModelForm):

    try:
        choices = Recipient.objects.values_list('id', 'email')

        name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'name'}))
        start_time = forms.DateTimeField(label='', widget=forms.DateTimeInput(attrs={'placeholder': 'start_time'}),
                                         initial=format(datetime.date.today(), '%Y-%m-%d %H:%M'))
        message = forms.ModelChoiceField(queryset=Message.objects.all())
        recipients = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)
    except Exception:
        choices = []

        name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'name'}))
        start_time = forms.DateTimeField(label='', widget=forms.DateTimeInput(attrs={'placeholder': 'start_time'}),
                                         initial=format(datetime.date.today(), '%Y-%m-%d %H:%M'))
        message = forms.ModelChoiceField(queryset=Message.objects.all())
        recipients = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Mail
        fields = ('name', 'start_time', 'message', 'recipients',)
