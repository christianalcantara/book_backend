# Generated by Django 3.1.2 on 2021-02-21 16:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_auto_20210221_0612"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="token",
        ),
    ]
