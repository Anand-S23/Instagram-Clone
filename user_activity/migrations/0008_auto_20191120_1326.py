# Generated by Django 2.1 on 2019-11-20 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_activity', '0007_auto_20191104_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='act_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 20, 13, 26, 1, 156153)),
        ),
    ]
