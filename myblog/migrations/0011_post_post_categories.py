# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_auto_20150301_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_categories',
            field=models.ForeignKey(default=0, to='myblog.Category'),
            preserve_default=False,
        ),
    ]
