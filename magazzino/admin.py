from django.contrib import admin
from magazzino.models import *

for m in Scavo, Magazzino, Vano, Contesto:
    admin.site.register(m)

class CassaAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Informazioni di base',
         {'fields': ['number', ('scavo', 'numscavo', 'data_scavo'), ('vano', 'posizione'),
                     'contenuto', 'materiale', 'mpoly']}),
        ('CD - Codici', {'fields': ['tsk', 'lir', ('nctr', 'nctn'), ('esc', 'ecp')]}),
        ('OG - Oggetto', {'fields': ['scan', 'dscd']}),
        ('LC - Localizzazione geografico-amministrativa', {'fields': [('pvcs', 'pvcr', 'pvcp', 'pvcc')]}),
        ('DT - Cronologia', {'fields': ['dtzg', 'dtm']}),
        ('MA - Materiale', {'fields': [('macc', 'macq')]}),
        ('TU - Condizione giuridica e vincoli', {'fields': ['cdgg']}),
        ('AD - Accesso ai dati', {'fields': [('adsp', 'adsm')]}),
        ('CM - Compilazione', {'fields': [('cmpd', 'cmpn'), 'fur']})
        ]

admin.site.register(Cassa, CassaAdmin)
