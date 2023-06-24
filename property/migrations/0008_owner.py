# Generated by Django 3.2 on 2023-06-20 23:46

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0007_auto_20230621_0242"),
    ]

    operations = [
        migrations.CreateModel(
            name="Owner",
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
                    "fullname",
                    models.CharField(
                        max_length=200, verbose_name="ФИО владельца"
                    ),
                ),
                (
                    "phonenumber",
                    models.CharField(
                        max_length=20, verbose_name="Номер владельца"
                    ),
                ),
                (
                    "pure_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=20,
                        null=True,
                        region=None,
                        verbose_name="Стандартизированный номер владельца",
                    ),
                ),
                (
                    "flats",
                    models.ManyToManyField(
                        blank=True,
                        related_name="owners",
                        to="property.Flat",
                        verbose_name="Квартиры в собственности",
                    ),
                ),
            ],
        ),
    ]
