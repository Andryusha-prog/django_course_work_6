from django.contrib import admin

from email_sender.models import Client, Mailing, Message

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("email", "name")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("topic_mail",)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("date_start", "periodic", "status", "date_end", "message")
