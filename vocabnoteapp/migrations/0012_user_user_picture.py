# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabnoteapp', '0011_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='User_Picture',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
