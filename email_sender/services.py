import datetime
import smtplib

from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from email_sender.models import Mailing, Attempt


def send_send(topic, body, email, mailing):
    today = datetime.datetime.now()
    try:
        server_response = send_mail(
            subject=topic,
            message=body,
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False
        )
        status = Attempt.STATUS_ATTEMPT[0][0]
        Attempt.objects.create(mailing=mailing, last_date=today, answer=server_response, status=status)
    except smtplib.SMTPException as e:
        status = Attempt.STATUS_ATTEMPT[1][0]
        Attempt.objects.create(mailing=mailing, last_date=today, answer=e, status=status)