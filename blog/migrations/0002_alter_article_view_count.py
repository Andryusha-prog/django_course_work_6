# Generated by Django 4.2.2 on 2024-09-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="view_count",
            field=models.IntegerField(default=0, verbose_name="Количество просмотров"),
        ),
    ]
