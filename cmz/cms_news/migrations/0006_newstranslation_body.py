# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-23 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_news', '0005_remove_newstranslation_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstranslation',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
