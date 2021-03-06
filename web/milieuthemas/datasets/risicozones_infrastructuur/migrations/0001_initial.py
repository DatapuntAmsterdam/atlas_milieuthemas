# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 15:43
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Infrastructuur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('ag', 'Aardgasleiding'), ('sw', 'Spoorweg'), ('vw', 'Vaarweg'), ('wg', 'Weg')], max_length=2, null=True)),
                ('geometrie_line', django.contrib.gis.db.models.fields.MultiLineStringField(null=True, srid=28992)),
                ('geometrie_polygon', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=28992)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
