# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='posts',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
