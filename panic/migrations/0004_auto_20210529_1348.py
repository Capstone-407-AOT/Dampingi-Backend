# Generated by Django 3.0 on 2021-05-29 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panic', '0003_auto_20210529_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panic',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]