"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.db import IntegrityError

from magazzino.models import *


class VanoTestCase(TestCase):

    def test_vano_unicode(self):
        vano = Vano(magazzino=Vano.ENEL, numero=3, desc='Vano di angolo')
        self.assertEqual('Magazzino ENEL - Vano 3', vano.__unicode__())


class CassaTestCase(TestCase):

    def test_natural_key_get_magazzino(self):
        vano = Vano(magazzino=Vano.ENEL, numero=3, desc='Vano di angolo')
        vano.save()
        cassa = Cassa(
            number='R45',
            nctn='00000001',
            dscd='2002-03-25',
            ldcn=vano,
            ldcs="a sinistra dell'ingresso",
            dtzg='I sec. d.C.',
            dtm='analisi dei materiali',
            macc='ceramica',
            macq='34',
            cmpd='2013-02-13',
            cmpn='Stefano Costa',
            fur='Luigi Gambaro',
            )
        cassa.save()
        self.assertEqual(Cassa.objects.get_by_natural_key('ENEL', 'R45'), cassa)

    def test_unique_together(self):
        vano = Vano(magazzino=Vano.ENEL, numero=3, desc='Vano di angolo')
        vano.save()
        cassa1 = Cassa(
            number='445',
            nctn='00000002',
            dscd='2002-03-25',
            ldcn=vano,
            ldcs="a sinistra dell'ingresso",
            dtzg='I sec. d.C.',
            dtm='analisi dei materiali',
            macc='ceramica',
            macq='34',
            cmpd='2013-02-13',
            cmpn='Stefano Costa',
            fur='Luigi Gambaro',
            )
        cassa1.save()
        cassa2 = Cassa(
            number='445',
            nctn='00000003',
            dscd='2002-03-25',
            ldcn=vano,
            ldcs="a sinistra dell'ingresso",
            dtzg='I sec. d.C.',
            dtm='analisi dei materiali',
            macc='ceramica',
            macq='34',
            cmpd='2013-02-13',
            cmpn='Stefano Costa',
            fur='Luigi Gambaro',
            )
        with self.assertRaises(IntegrityError):
            cassa2.save()


class ClasseTestCase(TestCase):

    def test_natural_key(self):
        classe = ClasseDiMateriale(
            sigla='TEST',
            classe='Classe di prova',
            famiglia='Contenitori da trasporto',
            )
        classe.save()
        self.assertEqual(ClasseDiMateriale.objects.get_by_natural_key('TEST'), classe)

class MaterialeTestCase(TestCase):

    def setUp(self):
        self.vano = Vano(magazzino=Vano.ENEL, numero=3, desc='Vano di angolo')
        self.vano.save()
        self.cassa = Cassa(
            number='R45',
            nctn='00000001',
            dscd='2002-03-25',
            ldcn=self.vano,
            ldcs="a sinistra dell'ingresso",
            dtzg='I sec. d.C.',
            dtm='analisi dei materiali',
            macc='ceramica',
            macq='34',
            cmpd='2013-02-13',
            cmpn='Stefano Costa',
            fur='Luigi Gambaro',
            )
        self.cassa.save()
        self.scavo = Scavo(
            area='TEATR',
            settore='Emiciclo est',
            scan='Saggio nel vano B (a nord delle scale)',
            scad='Saggio nel vano B (a nord delle scale)',
            luogo='Ventimiglia',
            dsch='',
            )
        self.scavo.save()
        self.contesto = ContestoScavo(scavo=self.scavo, numero_nome='Strato II')
        self.contesto.save()
        self.forma = FormaDiMateriale.objects.get_by_natural_key('Vasellame', 'Olla')
        self.classe = ClasseDiMateriale.objects.get_by_natural_key('AAFR')

    def test_frammenti_numeri_inventario(self):
        mic = MaterialeInCassa(
            cassa=self.cassa,
            contesto=self.contesto,
            macl=self.classe,
            macd=self.forma,
            )
        mic.orli = 2
        mic.numeri_inventario_orli = u'11/12'
        mic.anse = 4
        mic.numeri_inventario_anse = u'13-16'
        mic.save()

        # unfortunately, not all items are marked with a unique id
        # so the check below is not feasible
        # kept for reference

        # for f in ('orli', 'anse', 'pareti', 'fondi', 'piedi'):
        #     count = getattr(mic, f)
        #     inv_num = getattr(mic, 'numeri_inventario_'+f)
        #     if count > 0:
        #         self.assertNotEqual(inv_num, u'')
        #     if inv_num != u'':
        #         self.assertGreater(count, 0)
