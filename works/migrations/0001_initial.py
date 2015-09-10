# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=20)),
                ('pub_phone', models.IntegerField()),
                ('pub_mail', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('condition', models.CharField(max_length=100)),
                ('canvas', models.CharField(max_length=2, choices=[('IM', '今出川'), ('TN', '京田辺')])),
                ('location', models.CharField(max_length=100)),
                ('work_period', models.DateField()),
                ('dead_line', models.DateField()),
                ('can_time', models.DateField()),
                ('pay', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=2, choices=[('Hi', '被験者バイト'), ('Se', '生協バイト'), ('Pc', 'PCバイト'), ('Ho', '補助バイト')])),
            ],
        ),
    ]
