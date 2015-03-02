# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_category_post_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='post_categories',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_categories',
        ),
    ]
