# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-31 11:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20170731_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emplovee',
            name='user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='start',
        ),
        migrations.DeleteModel(
            name='Emplovee',
        ),
    ]