# -*- coding: utf-8 -*-

from django.contrib import admin
from magazzino.models import *

for m in Scavo, Vano:
    admin.site.register(m)

class ClasseAdmin(admin.ModelAdmin):
    filter_horizontal = ['forme']
    list_display = ('sigla', 'classe', 'famiglia')
    list_filter = ['famiglia']
    search_fields = ['classe']

class MaterialeInline(admin.StackedInline):
    model = MaterialeInCassa
    raw_id_fields = ('macl', 'macd')
    autocomplete_lookup_fields = {
        'fk': ['macl', 'macd'],
        }
    fieldsets = [
        (None, {'fields' : ['cassa', 'contesto']}),
        (None, {'fields' : ['macl', 'macd']}),
        (None, {'fields' : ['macp', 'macn_isr']}),
        ('Quantificazione', {'fields' : [('orli', 'numeri_inventario_orli'),
                                         ('anse', 'numeri_inventario_anse'),
                                         ('pareti', 'numeri_inventario_pareti'),
                                         ('fondi', 'numeri_inventario_fondi'),
                                         ('piedi', 'numeri_inventario_piedi'),
                                         'nme']}),
        (None, {'fields' : ['macn']}),
        ]
    extra = 3

class CassaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informazioni di base',
         {'fields': ['number', 'numscavo']}),
        ('LDC - Collocazione specifica', {'fields': ['ldct', 'ldcn', 'ldcs']}),
        ('DSC - Dati di scavo',
         {'fields': ['dscd']}),
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


class ContestoAdmin(admin.ModelAdmin):
    inlines = [MaterialeInline]

class FormaAdmin(admin.ModelAdmin):
    list_display = ('forma', 'famiglia')
    list_filter = ['famiglia']

admin.site.register(Cassa, CassaAdmin)
admin.site.register(ContestoScavo, ContestoAdmin)
admin.site.register(ClasseDiMateriale, ClasseAdmin)
admin.site.register(FormaDiMateriale, FormaAdmin)
