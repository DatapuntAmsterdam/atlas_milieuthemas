from unittest import skip

from datapunt_generic.batch.test import TaskTestCase
from .. import batch, models

from datasets.themas.tests.factories import ThemaFactory


class ImportMaatgevendeToetshoogteTest(TaskTestCase):

    def task(self):
        return batch.ImportMaatgevendeToetshoogteTask()

    def test_import(self):
        self.run_task()

        imported = models.MaatgevendeToetshoogte.objects.all()
        self.assertEqual(len(imported), 20)

        klasse_min_tien = models.MaatgevendeToetshoogte.objects.filter(
            hoogte_nap_klasse=-10
        )  # <- get all objects in class -10, should be 13 in the testset
        self.assertEqual(klasse_min_tien.count(), 13)


class ImportHoogtebeperkingRadarTest(TaskTestCase):

    def task(self):
        return batch.ImportHoogtebeperkingRadarTask()

    def test_import(self):
        self.run_task()

        imported = models.HoogtebeperkingRadar.objects.all()
        self.assertEqual(len(imported), 20)

        klasse_min_tien = models.HoogtebeperkingRadar.objects.filter(
            hoogte_nap_klasse=20
        )  # <- get all objects in class -10, should be 13 in the testset
        self.assertEqual(klasse_min_tien.count(), 7)


class ImportGeluidzoneTest(TaskTestCase):
    def setUp(self):
        ThemaFactory.create(pk=2)

    def task(self):
        return batch.ImportGeluidzoneTask()

    @skip('skip because incomplete polygons')
    def test_import(self):
        self.run_task()

        imported = models.Geluidzone.objects.all()
        self.assertEqual(len(imported), 2)

        zone = models.Geluidzone.objects.get(geo_id=57)
        self.assertEqual(zone.type, '20 Ke contour')
        self.assertNotEqual(zone.geometrie, None)


class ImportVogelvrijwaringsgebiedTest(TaskTestCase):
    def setUp(self):
        ThemaFactory.create(pk=7)

    def task(self):
        return batch.ImportVogelvrijwaringsgebiedTask()

    def test_import(self):
        self.run_task()

        imported = models.Vogelvrijwaringsgebied.objects.all()
        self.assertEqual(len(imported), 1)

        gebied = models.Vogelvrijwaringsgebied.objects.get(geo_id=1)
        self.assertEqual(gebied.type, 'Vogelvrijwaringsgebied')
        self.assertNotEqual(gebied.geometrie, None)
