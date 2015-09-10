# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0006_auto_20150909_1510'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AlterField(
            model_name='works',
            name='money_kind',
            field=models.CharField(max_length=20),
        ),
    ]
