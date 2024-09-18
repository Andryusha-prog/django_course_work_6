import datetime

from email_sender.models import Client, Mailing, Message
from email_sender.services import send_send


def send_func(*args, **kwargs):
    today = datetime.datetime.now()  # получение текущей даты-времени

    if len(kwargs) == 0:
        list_mail = Mailing.objects.values('pk', 'status', 'message', 'client', 'periodic', 'date_start', 'date_end')
    else:
        list_mail = Mailing.objects.values('pk', 'status', 'message', 'client', 'periodic', 'date_start',
                                           'date_end').filter(pk=kwargs['mailing_pk'], message=kwargs['message_pk'])

    for mail in list_mail:
        if mail['status'] != 'stop':
            if args[0] == mail['periodic'] or args[0] == 'go_mail':
                if mail['date_start'].strftime('%Y-%m-%d %H:%M') <= today.strftime('%Y-%m-%d %H:%M') <= mail[
                    'date_end'].strftime('%Y-%m-%d %H:%M'):
                    send_send(
                        Message.objects.values('topic_mail').get(pk=mail['message'])['topic_mail'],
                        Message.objects.values('bode_mail').get(pk=mail['message'])['bode_mail'],
                        Client.objects.values('email').get(pk=mail['client'])['email'],
                        Mailing.objects.get(pk=mail['pk'])
                    )
                else:
                    tek_zap = Mailing.objects.get(pk=mail['pk'])
                    tek_zap.status = Mailing.STATUS_MAILING[2][0]
                    tek_zap.save()

                if mail['status'] == 'create':
                    tek_zap = Mailing.objects.get(pk=mail['pk'])
                    tek_zap.status = Mailing.STATUS_MAILING[1][0]
                    tek_zap.save()
