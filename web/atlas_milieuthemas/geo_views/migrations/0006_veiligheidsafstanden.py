# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 08:15
# Python
from __future__ import unicode_literals
# Packages
from django.db import migrations
# Project
from geo_views import migrate


class Migration(migrations.Migration):

    dependencies = [
        ('geo_views', '0005_bodeminformatie'),
        ('veiligheidsafstanden', '0001_initial'),
    ]

    operations = [
        migrate.ManageView(
            view_name="geo_veiligheidsafstanden_point_layer",
            sql="""SELECT id, type, locatie, geometrie_point as geometrie
                    FROM veiligheidsafstanden_veiligheidsafstand
                    WHERE geometrie_point IS NOT NULL"""
        ),
        migrate.ManageView(
            view_name="geo_veiligheidsafstanden_polygon_layer",
            sql="""SELECT id, type, locatie, geometrie_multipolygon as geometrie
                    FROM veiligheidsafstanden_veiligheidsafstand
                    WHERE geometrie_multipolygon IS NOT NULL"""
        ),
    ]
