# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0011_post_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='post_categories',
            field=models.ForeignKey(default=0, to='myblog.Post'),
            preserve_default=False,
        ),
    ]
