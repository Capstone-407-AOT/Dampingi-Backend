# Generated by Django 3.0 on 2021-05-25 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jwtauth', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmergencyContact',
            new_name='Emergency',
        ),
    ]