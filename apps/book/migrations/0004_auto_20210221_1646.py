# Generated by Django 3.1.2 on 2021-02-21 16:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0003_book_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(
                related_name="books", to="book.Author", verbose_name="Authors"
            ),
        ),
    ]
