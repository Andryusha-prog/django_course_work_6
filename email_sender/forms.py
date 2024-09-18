

from django.forms import ModelForm

from email_sender.models import Client, Mailing, Message, Attempt


class ClientFormCreate(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class ClientFormUpdate(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MessageFormCreate(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class MessageFormUpdate(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class MailingFormCreate(ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'


class MailingFormUpdate(ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'


class AttemptForm(ModelForm):
    class Meta:
        model = Attempt
        fields ='__all__'

