# Generated by Django 3.2.9 on 2021-11-03 08:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 8, 37, 40, 206415, tzinfo=utc)),
        ),
    ]
