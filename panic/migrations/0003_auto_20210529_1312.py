# Generated by Django 3.0 on 2021-05-29 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panic', '0002_auto_20210526_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panic',
            name='cur_lat',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='panic',
            name='cur_lng',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
