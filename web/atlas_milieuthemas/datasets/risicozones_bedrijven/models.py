from django.db import models
from django.contrib.gis.db import models as geo

from datapunt_generic.generic import mixins


class LPGStation(mixins.ImportStatusMixin):
    id = models.IntegerField(primary_key=True)
    dossiernummer = models.CharField(max_length=40, null=True)
    bedrijfsnaam = models.CharField(max_length=40, null=True)
    adres = models.CharField(max_length=100, null=True)
    postcode = models.CharField(max_length=10, null=True)
    plaats = models.CharField(max_length=15, null=True)
    stadsdeel = models.CharField(max_length=10, null=True)
    oliemaatschappij = models.CharField(max_length=10, null=True)
    omzet = models.CharField(max_length=10, null=True)
    ligging = models.CharField(max_length=20, null=True)
    tank_aanwezig = models.CharField(max_length=3, null=True)
    tank_positie = models.CharField(max_length=20, null=True)
    tank_inhoud = models.CharField(max_length=10, null=True)
    vulpunt_aanwezig = models.CharField(max_length=3, null=True)
    vulmoment = models.CharField(max_length=20, null=True)
    opmerkingen = models.TextField(null=True)
    geometrie_polygon = geo.MultiPolygonField(null=True, srid=28992)
    geometrie_point = geo.PointField(null=True, srid=28992)

    objects = geo.GeoManager()


class LPGVulpunt(mixins.ImportStatusMixin):
    geo_id = models.IntegerField(null=False)
    station = models.ForeignKey(LPGStation, null=True)
    type = models.CharField(max_length=40, null=True)
    afstandseis = models.CharField(max_length=10, null=True)
    voldoet = models.CharField(max_length=3, null=True)
    geometrie_point = geo.PointField(null=True, srid=28992)
    geometrie_polygon = geo.MultiPolygonField(null=True, srid=28992)

    objects = geo.GeoManager()


class LPGAfleverzuil(mixins.ImportStatusMixin):
    stationnummer = models.IntegerField(null=True)
    geometrie_point = geo.PointField(null=True, srid=28992)
    geometrie_polygon = geo.MultiPolygonField(null=True, srid=28992)

    objects = geo.GeoManager()


class LPGTank(mixins.ImportStatusMixin):
    stationnummer = models.IntegerField(null=True)
    kleur = models.IntegerField(null=True)
    type = models.CharField(max_length=40, null=True)
    voldoet = models.CharField(max_length=3, null=True)
    afstandseis = models.CharField(max_length=10, null=True)
    geometrie = geo.MultiPolygonField(null=True, srid=28992)

    objects = geo.GeoManager()

class Bron(mixins.ImportStatusMixin):
    bron_id = models.IntegerField(null=True)
    bedrijfsnaam = models.CharField(max_length=64, null=True)
    hoeveelheid_stof = models.CharField(max_length=16, null=True)
    type_stof = models.CharField(max_length=64, null=True)
    