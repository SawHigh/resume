# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0012_auto_20160215_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='end',
            new_name='end_date',
        ),
    ]
