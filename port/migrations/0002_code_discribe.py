# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='discribe',
            field=models.TextField(null=True),
        ),
    ]
