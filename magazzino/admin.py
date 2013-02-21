# -*- coding: utf-8 -*-

from django.contrib import admin
from magazzino.models import *

for m in Scavo, Magazzino, Vano, ContestoScavo, FormaDiMateriale:
    admin.site.register(m)

class ClasseAdmin(admin.ModelAdmin):
    filter_horizontal = ['forme']

class MaterialeInline(admin.TabularInline):
    model = MaterialeInCassa
    raw_id_fields = ('classe', 'ogtd')
    autocomplete_lookup_fields = {
        'fk': ['classe', 'ogtd'],
        }
    extra = 3

class CassaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informazioni di base',
         {'fields': ['number', 'scavo', ('numscavo', 'data_scavo'), ('vano', 'posizione'),
                     'contenuto', 'materiale']}),
        ('CD - Codici', {'fields': [('tsk', 'lir'), ('nctr', 'nctn'), ('esc', 'ecp')]}),
        ('OG - Oggetto', {'fields': ['scan', 'dscd']}),
        ('LC - Localizzazione geografico-amministrativa', {'fields': [('pvcs', 'pvcr'), ('pvcp', 'pvcc')]}),
        ('DT - Cronologia', {'fields': ['dtzg', 'dtm']}),
        ('MA - Materiale', {'fields': [('macc', 'macq')]}),
        ('TU - Condizione giuridica e vincoli', {'fields': ['cdgg']}),
        ('AD - Accesso ai dati', {'fields': [('adsp', 'adsm')]}),
        ('CM - Compilazione', {'fields': [('cmpd', 'cmpn'), 'fur']})
        ]

    inlines = [MaterialeInline]

admin.site.register(Cassa, CassaAdmin)
admin.site.register(ClasseDiMateriale, ClasseAdmin)
