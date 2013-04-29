# -*- coding: utf-8 -*-

from django.contrib import admin
from magazzino.models import *

for m in Scavo, Magazzino, Vano, ContestoScavo, FormaDiMateriale:
    admin.site.register(m)

class ClasseAdmin(admin.ModelAdmin):
    filter_horizontal = ['forme']

class MaterialeInline(admin.StackedInline):
    model = MaterialeInCassa
    raw_id_fields = ('classe', 'ogtd')
    autocomplete_lookup_fields = {
        'fk': ['classe', 'ogtd'],
        }
    fieldsets = [
        (None, {'fields' : ['classe', 'ogtd']}),
        (None, {'fields' : ['ogtt', 'isr']}),
        (None, {'fields' : [('orli', 'numeri_inventario_orli'),
                            ('anse', 'numeri_inventario_anse'),
                            ('pareti', 'numeri_inventario_pareti'),
                            ('fondi', 'numeri_inventario_fondi'),
                            ('piedi', 'numeri_inventario_piedi'),
                            'nme']}),
        ]
    extra = 3

class CassaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informazioni di base',
         {'fields': ['number', 'scavo', 'numscavo', ('vano', 'posizione')]}),
        ('LDC - Collocazione specifica', {'fields': ['ldct', 'ldcn', 'ldcs']}),
        ('DSC - Dati di scavo',
         {'fields': ['scan', 'dscd']}),
        ('DT - Cronologia', {'fields': ['dtzg', 'dtm']}),
        ('MA - Materiale', {'fields': [('macc', 'macq')]}),
        ('CM - Compilazione', {'fields': [('cmpd', 'cmpn'), 'fur']}),
        # collapsed fieldsets - these have default values
        ('CD - Codici', {'fields': [('lir'), ('nctr', 'nctn'), ('esc', 'ecp')],
                         'classes': ['collapse grp-collapse grp-closed']}),
        ('LC - Localizzazione geografico-amministrativa',
         {'fields': [('pvcs', 'pvcr'), ('pvcp', 'pvcc')],
          'classes': ['collapse grp-collapse grp-closed']}),
        ('TU - Condizione giuridica e vincoli',
         {'fields': ['cdgg'],
          'classes': ['collapse grp-collapse grp-closed']}),
        ('AD - Accesso ai dati',
         {'fields': [('adsp', 'adsm')],
          'classes': ['collapse grp-collapse grp-closed']}),
        ]

    inlines = [MaterialeInline]

admin.site.register(Cassa, CassaAdmin)
admin.site.register(ClasseDiMateriale, ClasseAdmin)
