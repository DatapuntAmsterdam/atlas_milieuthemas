from django.db import models
from django.contrib.gis.db import models as geo

from datapunt_generic.generic import mixins
from datasets.themas.models import Thema
from django.db.models import Manager as GeoManager

class Veiligheidsafstand(mixins.ModelViewFieldsMixin, mixins.ImportStatusMixin):
    geo_id = models.IntegerField(null=False)
    type = models.CharField(max_length=100, null=True)
    thema = models.ForeignKey(Thema, null=True, on_delete=models.CASCADE)
    locatie = models.CharField(max_length=100, null=True)
    geometrie_multipolygon = geo.MultiPolygonField(null=True, srid=28992)
    geometrie_point = geo.PointField(null=True, srid=28992)

    objects = GeoManager()

    geo_view_exclude = ['date_modified', 'thema']
    geo_view_include = ['thema_id']
