# Generated by Django 3.1.7 on 2021-04-14 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingapp', '0013_reservation_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='space_type',
            field=models.CharField(default='Standard', max_length=10),
        ),
    ]