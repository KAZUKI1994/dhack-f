# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='category',
            field=models.CharField(choices=[('Hi', '被験者バイト'), ('Se', '生協バイト'), ('Pc', '赤じゃん'), ('Ho', '授業補助'), ('Ev', 'イベント')], max_length=2),
        ),
    ]
