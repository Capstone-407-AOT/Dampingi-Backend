# Generated by Django 3.0 on 2021-05-26 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='cur_lat',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='cur_lng',
            new_name='lng',
        ),
    ]
