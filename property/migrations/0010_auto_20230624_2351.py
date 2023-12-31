# Generated by Django 3.2 on 2023-06-24 20:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0009_auto_20230621_0247"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flat",
            name="description",
            field=models.TextField(
                null=True, verbose_name="Текст объявления"
            ),
        ),
        migrations.AlterField(
            model_name="flat",
            name="owner",
            field=models.CharField(
                db_index=True, max_length=200, verbose_name="ФИО владельца"
            ),
        ),
        migrations.AlterField(
            model_name="owner",
            name="fullname",
            field=models.CharField(
                db_index=True, max_length=200, verbose_name="ФИО владельца"
            ),
        ),
    ]
