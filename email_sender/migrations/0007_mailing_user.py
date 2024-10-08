# Generated by Django 4.2.2 on 2024-09-21 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("email_sender", "0006_alter_attempt_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailing",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь-Владелец",
            ),
        ),
    ]
