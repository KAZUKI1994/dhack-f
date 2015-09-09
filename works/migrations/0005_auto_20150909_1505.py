# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0004_auto_20150909_1502'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Work',
            new_name='Works',
        ),
    ]
