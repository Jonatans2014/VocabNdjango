# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabnoteapp', '0007_auto_20171127_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Classification', models.CharField(max_length=100)),
                ('Word', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['Classification'],
            },
        ),
        migrations.RenameModel(
            old_name='Album',
            new_name='User',
        ),
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='album_name',
            new_name='User_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='artist',
            new_name='gender',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
        migrations.AddField(
            model_name='word',
            name='User',
            field=models.ManyToManyField(to='vocabnoteapp.User'),
        ),
        migrations.AlterUniqueTogether(
            name='word',
            unique_together=set([('Classification', 'Word')]),
        ),
    ]
