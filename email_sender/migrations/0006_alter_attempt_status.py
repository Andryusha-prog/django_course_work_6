# Generated by Django 4.2.2 on 2024-09-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("email_sender", "0005_remove_mailing_attempt_attempt_mailing"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attempt",
            name="status",
            field=models.CharField(max_length=150, verbose_name="статус рассылки"),
        ),
    ]
