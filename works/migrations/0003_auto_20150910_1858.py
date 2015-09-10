# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_auto_20150910_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='category',
            field=models.CharField(max_length=2, choices=[('Hi', '被験者バイト'), ('Se', '生協バイト'), ('Pc', 'PCバイト'), ('Ho', '授業補助'), ('Ev', 'イベント')]),
        ),
    ]
