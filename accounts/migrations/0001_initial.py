# Generated by Django 2.1 on 2019-07-20 23:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=300, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be alphanumeric or contain numbers.', regex='^[a-zA-Z0-9]*$')])),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('name', models.CharField(max_length=300, verbose_name='Full Name')),
                ('bio', models.TextField(blank=True, max_length=255, null=True, verbose_name='Bio')),
                ('picture', models.ImageField(blank=True, default='/profile_pic/default.jpg', upload_to='profile_pic', verbose_name='Profile Picture')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
