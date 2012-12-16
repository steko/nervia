========================
 Resetting the database
========================

``manage.py sqlclear`` is not enough when using GeoDjango. One needs
to clear the geometry columns::

  spatialite> select DiscardGeometryColumn('magazzino_cassa', 'mpoly');
  1

