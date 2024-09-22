

from django.forms import ModelForm

from email_sender.models import Client, Mailing, Message, Attempt


class ClientFormCreate(ModelForm):
    class Meta:
        model = Client
        exclude = ('user',)


class ClientFormUpdate(ModelForm):
    class Meta:
        model = Client
        exclude = ('user',)


class MessageFormCreate(ModelForm):
    class Meta:
        model = Message
        exclude = ('user',)


class MessageFormUpdate(ModelForm):
    class Meta:
        model = Message
        exclude = ('user',)


class MailingFormCreate(ModelForm):
    class Meta:
        model = Mailing
        exclude = ('user',)


class MailingFormUpdate(ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'


class AttemptForm(ModelForm):
    class Meta:
        model = Attempt
        fields ='__all__'


class ManagerMailingDetailForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ('status',)
