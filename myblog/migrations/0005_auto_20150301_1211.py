# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_post_post_categories'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='Categories',
        ),
    ]
