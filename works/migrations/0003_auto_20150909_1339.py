# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_auto_20150909_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
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
                ('canvas', models.CharField(max_length=1, choices=[('IM', '今出川'), ('TN', '京田辺')])),
                ('location', models.CharField(max_length=100)),
                ('work_start', models.DateField()),
                ('work_finish', models.DateField()),
                ('money_kind', models.CharField(max_length=1, choices=[('T', '時給'), ('K', '固定（一回)')])),
                ('money_amount', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
    ]
