# Generated by Django 3.2 on 2023-06-21 19:46

from django.db import migrations


def link_apartments_and_owners(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    Owner = apps.get_model("property", "Owner")
    for flat in Flat.objects.all().iterator():
        owner = Owner.objects.get_or_create(
            fullname=flat.owner, phonenumber=flat.owners_phonenumber
        )[0]
        owner.flats.set([flat])
    for owner in Owner.objects.all().iterator():
        flat = Flat.objects.get_or_create(
            owner=owner.fullname, owners_phonenumber=owner.phonenumber
        )[0]
        flat.owners.set([owner])


def link_apartments_and_owners_backward(apps, schema_editor):
    Owner = apps.get_model("property", "Owner")
    Flat = apps.get_model("property", "Flat")
    Owner.objects.all().update(flats=None)
    Flat.objects.all().update(owners=None)


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0010_auto_20230624_2351"),
    ]

    operations = [
        migrations.RunPython(
            link_apartments_and_owners, link_apartments_and_owners_backward
        )
    ]
