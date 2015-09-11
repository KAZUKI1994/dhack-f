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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('category', models.IntegerField(choices=[(0, '被験者バイト'), (1, '生協バイト'), (2, 'PCバイト'), (3, '授業補助'), (4, 'イベント')])),
                ('publisher', models.CharField(max_length=20)),
                ('pub_phone', models.IntegerField()),
                ('pub_mail', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('condition', models.CharField(max_length=100)),
                ('canpus', models.IntegerField(choices=[(0, '今出川'), (1, '京田辺')])),
                ('location', models.CharField(max_length=100)),
                ('work_period', models.CharField(max_length=300)),
                ('dead_line', models.DateField()),
                ('pay', models.CharField(max_length=20)),
            ],
        ),
    ]
