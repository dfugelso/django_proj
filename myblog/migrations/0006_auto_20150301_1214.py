# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_auto_20150301_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='posts',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
