================
 Importing data
================

It is much easier to enter data in spreadsheet and do a bulk import::

>>> from csv import DictReader
>>> from magazzino.models import ClasseDiMateriale
>>> with open('/path/to/file.csv') as csvfile:
...     ceramreader = DictReader(csvfile)
...     for row in ceramreader:
...         cdm = ClasseDiMateriale.objects.create(**row)
... 

Check that the objects imported correctly::

>>> ClasseDiMateriale.objects.all()

.. todo:: This example does not take advantage of the ``bulk_create``
	  method available since Django 1.4.
