# Generated by Django 2.1.2 on 2018-11-13 04:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='banner pictures')),
                ('url', models.URLField(verbose_name='url to visit')),
                ('index', models.IntegerField(default=100)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
            },
        ),
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='verification code')),
                ('email', models.EmailField(max_length=50, verbose_name='email address')),
                ('send_type', models.CharField(choices=[('reg', 'register'), ('for', 'forget')], max_length=5)),
                ('send_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'verification code',
                'verbose_name_plural': 'verification codes',
            },
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], default='f', max_length=2),
        ),
    ]
