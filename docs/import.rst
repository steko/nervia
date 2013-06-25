================
 Importing data
================

It is much easier to enter data in spreadsheet and do a bulk import::

  >>> from csv import DictReader
  >>> from magazzino.models import FormaDiMateriale
  >>> csvpath = '/path/to/file.csv'
  >>> with open(csvpath) as csvfile:
  ...   ceramreader = DictReader(csvfile)
  ...   data = [FormaDiMateriale(**row) for row in ceramreader]
  ...   FormaDiMateriale.objects.bulk_create(data)
  ... 

Check that the objects imported correctly::

>>> FormaDiMateriale.objects.all()

Foreign keys
============

Bulk creation with foreign keys::

  >>> from magazzino.models import *
  >>> data = [Vano(number=1, magazzino=Magazzino.objects.get(pk=1), desc='Vano 1'),
              Vano(number=2, magazzino=Magazzino.objects.get(pk=1), desc='Vano 2')]
  >>> Vano.objects.bulk_create(data)
  [<Vano: ENEL 1>, <Vano: ENEL 2>]

Bulk creation with natural keys::

  >>> Cassa.objects.get_by_natural_key(magazzino="Gas", numero="415")
  <Cassa: Gas 415>

with another model::

  >>> ClasseDiMateriale.objects.get_by_natural_key('COMLO')
  <ClasseDiMateriale: COMLO>

This can be used to prepare an object from a CSV record::

  >>> ins
  {'anse': 0,
  'cassa': <Cassa: Gas 415>,
  'classe': <ClasseDiMateriale: VNA>,
  'fondi': 0,
  'nme': 1,
  'numeri_inventario_orli': '5622',
  'ogtd': <FormaDiMateriale: Patera>,
  'orli': 1,
  'pareti': 0,
  'piedi': 0}

