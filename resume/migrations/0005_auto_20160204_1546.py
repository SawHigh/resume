# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_project_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Introduction',
        ),
        migrations.AddField(
            model_name='profile',
            name='introducion',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
