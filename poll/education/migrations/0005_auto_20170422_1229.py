# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 12:29
from __future__ import unicode_literals

from django.db import migrations, models
import education.models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_auto_20170422_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectureday',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lectureday',
            name='code',
            field=models.CharField(default=education.models.lecture_code_handler, max_length=10, unique=True),
        ),
    ]