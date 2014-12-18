# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='date_modified',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='list',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='list',
            old_name='date_modified',
            new_name='modified_at',
        ),
    ]
