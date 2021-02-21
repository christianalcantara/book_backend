# Generated by Django 3.1.2 on 2021-02-21 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0002_auto_20210219_2129"),
        ("rent", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catalog",
            name="book",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="catalog",
                to="book.book",
                verbose_name="Book",
            ),
        ),
    ]