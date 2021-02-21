# Generated by Django 3.1.2 on 2021-02-21 04:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("book", "0002_auto_20210219_2129"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Fee",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "days",
                    models.PositiveSmallIntegerField(
                        unique=True,
                        validators=[
                            django.core.validators.MaxValueValidator(31),
                            django.core.validators.MinValueValidator(1),
                        ],
                        verbose_name="Days",
                    ),
                ),
                (
                    "late_fee",
                    models.FloatField(
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(0.1),
                        ],
                        verbose_name="late fee",
                    ),
                ),
                (
                    "interest",
                    models.FloatField(
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(0.1),
                        ],
                        verbose_name="Interest",
                    ),
                ),
            ],
            options={
                "verbose_name": "Fee",
                "verbose_name_plural": "Fees",
                "ordering": ["days"],
            },
        ),
        migrations.CreateModel(
            name="Rent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rental_date",
                    models.DateTimeField(auto_now_add=True, verbose_name="Rental date"),
                ),
                (
                    "return_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Return date"
                    ),
                ),
                (
                    "late_fee_value",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="late fee",
                    ),
                ),
                (
                    "interest_value",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="Interest",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="Amount value",
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="rents",
                        to="book.book",
                        verbose_name="Book",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="rents",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Rent",
                "verbose_name_plural": "Rents",
            },
        ),
        migrations.CreateModel(
            name="Catalog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=9, verbose_name="Rental price"
                    ),
                ),
                (
                    "book",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="catalogs",
                        to="book.book",
                        verbose_name="Book",
                    ),
                ),
            ],
            options={
                "verbose_name": "Catalog",
                "verbose_name_plural": "Catalogs",
            },
        ),
    ]
