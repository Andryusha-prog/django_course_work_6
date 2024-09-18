from django.core.management import BaseCommand

from email_sender.cron import send_func
from email_sender.models import Mailing, Message, Client
from email_sender.services import send_send


class Command(BaseCommand):
    def handle(self, *args, **options):
        list_mail = Mailing.objects.values('pk', 'status', 'message', 'client', 'periodic', 'date_start', 'date_end')

        for mail in list_mail:
            if mail['status'] != 'stop':
                send_send(
                    Message.objects.values('topic_mail').get(pk=mail['message'])['topic_mail'],
                    Message.objects.values('bode_mail').get(pk=mail['message'])['bode_mail'],
                    Client.objects.values('email').get(pk=mail['client'])['email'],
                    Mailing.objects.get(pk=mail['pk'])
                )
                if mail['status'] == 'create':
                    tek_zap = Mailing.objects.get(pk=mail['pk'])
                    tek_zap.status = Mailing.STATUS_MAILING[1][0]
                    tek_zap.save()
