# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-09-21 20:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0004_evaluation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='podcast',
            old_name='podcast_title',
            new_name='material_title',
        ),
    ]
