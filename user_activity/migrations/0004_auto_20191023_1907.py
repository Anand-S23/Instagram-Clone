# Generated by Django 2.1 on 2019-10-23 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_activity', '0003_auto_20191020_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='act_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 23, 19, 7, 5, 306861)),
        ),
    ]