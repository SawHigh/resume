# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0008_profile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='link',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.AddField(
            model_name='contact',
            name='icon',
            field=models.ImageField(default=1, max_length=20, upload_to=b'contact'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=1024, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usercontact',
            name='contact',
            field=models.ForeignKey(to='resume.Contact'),
        ),
        migrations.AddField(
            model_name='usercontact',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
