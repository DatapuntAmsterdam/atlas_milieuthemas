# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bommenkaart', '0003_fix_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bominslag',
            name='intekening',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gevrijwaardgebied',
            name='intekening',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='verdachtgebied',
            name='subtype',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
