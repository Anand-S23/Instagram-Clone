# Generated by Django 2.1 on 2019-10-20 00:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_auto_20191019_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 0, 5, 53, 102367, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 0, 5, 53, 99369, tzinfo=utc)),
        ),
    ]