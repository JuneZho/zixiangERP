# Generated by Django 2.0.6 on 2018-07-20 02:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180720_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateField(default=datetime.datetime(2018, 7, 20, 2, 3, 9, 526895, tzinfo=utc)),
        ),
    ]
