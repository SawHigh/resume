# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='condition',
            field=models.CharField(max_length=10, null=True, choices=[(b'mobile', b'mobile'), (b'desktop', b'desktop'), (b'both', b'both')]),
        ),
    ]
