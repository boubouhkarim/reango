# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-05 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170616_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='vote_count',
            field=models.IntegerField(default=0),
        ),
    ]