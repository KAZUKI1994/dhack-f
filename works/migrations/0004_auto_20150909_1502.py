# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_auto_20150909_1339'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Works',
            new_name='Work',
        ),
    ]
