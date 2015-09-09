# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0005_auto_20150909_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='canvas',
            field=models.CharField(choices=[('IM', '今出川'), ('TN', '京田辺')], max_length=2),
        ),
    ]
