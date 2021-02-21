# Generated by Django 3.1.2 on 2021-02-19 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={
                "ordering": ["-created", "title"],
                "verbose_name": "Book",
                "verbose_name_plural": "Books",
            },
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(db_index=True, max_length=150, verbose_name="Title"),
        ),
    ]
