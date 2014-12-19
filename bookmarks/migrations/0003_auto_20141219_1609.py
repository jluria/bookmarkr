# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_auto_20141217_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='links',
            field=models.ManyToManyField(help_text='Select existing links to add to the list:', to='bookmarks.Link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=50, help_text='Name Your List:'),
            preserve_default=True,
        ),
    ]
