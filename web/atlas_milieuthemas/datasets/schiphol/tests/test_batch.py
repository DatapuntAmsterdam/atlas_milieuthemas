from unittest import skip

from datapunt_generic.batch.test import TaskTestCase
from .. import batch, models

from datasets.themas.tests.factories import ThemaFactory

NAP = 'diva/milieuthemas'


class ImportHoogtebeperkendeVlakkenTest(TaskTestCase):
    def setUp(self):
        ThemaFactory.create(pk=6)

    def task(self):
        return batch.ImportHoogtebeperkendeVlakkenTask(NAP)

    def test_import(self):
        self.run_task()

        imported = models.HoogtebeperkendeVlakken.objects.all()
        self.assertEqual(len(imported), 20)

        vlak = models.HoogtebeperkendeVlakken.objects.get(geo_id=16)
        self.assertEqual(vlak.bouwhoogte, '1.5-2.0')
        self.assertEqual(vlak.geometrie_point, None)
        self.assertEqual(vlak.geometrie_line, None)
        self.assertNotEqual(vlak.geometrie_polygon, None)


class ImportGeluidzoneTest(TaskTestCase):
    def setUp(self):
        ThemaFactory.create(pk=2)

    def task(self):
        return batch.ImportGeluidzoneTask(NAP)

    @skip('skip because incomplete polygons')
    def test_import(self):
        self.run_task()

        imported = models.Geluidzone.objects.all()
        self.assertEqual(len(imported), 2)

        zone = models.Geluidzone.objects.get(geo_id=57)
        self.assertEqual(zone.type, '20 Ke contour')
        self.assertNotEqual(zone.geometrie, None)
