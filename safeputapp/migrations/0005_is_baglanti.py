# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-18 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('safeputapp', '0004_auto_20190618_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='is',
            name='baglanti',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Ba\u011flant\u0131'),
            preserve_default=False,
        ),
    ]
