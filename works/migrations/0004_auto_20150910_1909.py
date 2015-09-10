# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_auto_20150910_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='canvas',
            field=models.IntegerField(choices=[(0, '今出川'), (1, '京田辺')]),
        ),
        migrations.AlterField(
            model_name='works',
            name='category',
            field=models.IntegerField(choices=[(0, '被験者バイト'), (1, '生協バイト'), (2, 'PCバイト'), (3, '授業補助'), (4, 'イベント')]),
        ),
    ]
