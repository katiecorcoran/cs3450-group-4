# Generated by Django 3.1.7 on 2021-03-21 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingapp', '0003_lot_nickname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Space',
        ),
    ]