# Generated by Django 2.1 on 2019-10-20 21:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_auto_20191019_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 21, 32, 6, 90047, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 21, 32, 6, 88048, tzinfo=utc)),
        ),
    ]
