# -*- coding: utf-8 -*-

from django.contrib.gis.db import models

# Create your models here.


class Scavo(models.Model):
    '''Scavo archeologico.

    Probabilmente da ricondurre a una scheda ICCD SAS.'''

    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=50, blank=True)
    luogo = models.CharField('Località', max_length=100)
    descrizione = models.TextField()

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "scavi"


class ContestoScavo(models.Model):
    '''Unità stratigrafica, strato, livello o altro.

    Un qualunque tipo di indicazione sulla provenienza del materiale
    di scavo, in forma sintetica'''

    number = models.CharField(max_length=50)
    scavo = models.ForeignKey(Scavo)

    def __str__(self):
        return "%s - %s" % (self.number, self.scavo)

    class Meta:
        verbose_name_plural = "contesti"


class Magazzino(models.Model):
    '''Un magazzino.'''

    nome = models.CharField(max_length=50)
    descrizione = models.TextField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "magazzini"


class Vano(models.Model):
    '''Un vano all'interno di un magazzino.'''

    number = models.IntegerField('Numero del vano')
    magazzino = models.ForeignKey(Magazzino)
    desc = models.TextField('Descrizione')

    def __str__(self):
        return '%s %s' % (self.magazzino.__str__(), self.number)

    class Meta:
        verbose_name_plural = 'vani'


class Cassa(models.Model):
    '''Basata sul modello "Scheda di cassa".

    Fa riferimento alla scheda ICCD TMA (Tabella materiali).'''

    # informazioni di base
    number = models.CharField('Numero di cassa', max_length=50)
    scavo = models.ForeignKey(Scavo, blank=True)
    numscavo = models.IntegerField('Numero di cassa dello scavo', blank=True, help_text='Il numero di cassa nella numerazione dello scavo, se presente')
    vano = models.ForeignKey(Vano)
    posizione = models.CharField(help_text='Scaffale, colonna o altro',
                                 max_length=100)
    contenuto = models.TextField(blank=True, help_text='Descrizione estesa del contenuto')
    #contesto = models.ManyToManyField(Contesto, blank=True)
    materiale = models.CharField(max_length=100, blank=True)

    # posizione
    mpoly = models.PointField()
    objects = models.GeoManager()

    # dati di scavo
    data_scavo = models.CharField(max_length=20, blank=True, help_text='Data dello scavo in formato AAAA-MM-GG')

    # CD - Codici
    tsk = models.CharField('TSK', help_text='Tipo scheda', max_length=100)
    lir = models.CharField('LIR', help_text='Livello ricerca', max_length=100)
    ## NCT - Codice univoco
    NCTR_CODICI = (
        # codici ICCD
        ('01', 'Piemonte'),
        ('02', "Valle d'Aosta"),
        ('03', 'Lombardia'),
        ('04', 'Trentino-Alto Adige'),
        ('05', 'Veneto'),
        ('06', 'Friuli-Venezia Giulia'),
        ('07', 'Liguria'),
        ('08', 'Emilia-Romagna'),
        ('09', 'Toscana'),
        ('10', 'Umbria'),
        ('11', 'Marche'),
        ('12', 'Lazio'),
        ('13', 'Abruzzo'),
        ('14', 'Molise'),
        ('15', 'Campania'),
        ('16', 'Puglia'),
        ('17', 'Basilicata'),
        ('18', 'Calabria'),
        ('19', 'Sicilia'),
        ('20', 'Sardegna'),
        )
    nctr = models.CharField('NCTR',
                            help_text='Codice regione',
                            max_length=2,
                            choices=NCTR_CODICI)
    nctn = models.CharField('NCTN',
                            help_text='Numero catalogo generale',
                            max_length=30,
                            unique=True)
    esc = models.CharField('ESC', help_text='Ente schedatore', max_length=100) 
    ecp = models.CharField('ECP', help_text='Ente competente', max_length=100)

    # OG - Oggetto
    ## OGT - Oggetto = Cassa
    scan = models.CharField('SCAN', help_text='Area', max_length=100)
    # elenco delle US
    dscd = models.CharField('DSCD', max_length=200)
    # elenco dei numeri di inventario

    # LC - Localizzazione geografico-amministrativa
    ## PVC LOCALIZZAZIONE GEOGRAFICO-AMMINISTRATIVA ATTUALE
    pvcs = models.CharField('PVCS', help_text='Stato', max_length=50, default='Italia')
    pvcr = models.CharField('PVCR', help_text='Regione', max_length=30)
    pvcp = models.CharField('PVCP', help_text='Provincia', max_length=30) 
    pvcc = models.CharField('PVCC', help_text='Comune', max_length=100) 

    # DT CRONOLOGIA 
    ## DTZ CRONOLOGIA GENERICA 
    dtzg = models.CharField('DTZG',
                            help_text='Fascia cronologica di riferimento',
                            max_length=100)
    dtm = models.CharField('DTM',
                           help_text='Motivazione cronologia',
                           max_length=200)

    # MA MATERIALE
    ## MAC MATERIALE COMPONENTE 
    macc = models.CharField('MACC', help_text='Categoria', max_length=100)
    macq = models.CharField('MACQ', help_text='Quantità', max_length=100)

    # TU CONDIZIONE GIURIDICA E VINCOLI 
    ## CDG CONDIZIONE GIURIDICA 
    cdgg = models.CharField('CDGG', help_text='Indicazione generica', max_length=100)

    # AD ACCESSO AI DATI 
    ## ADS SPECIFICHE DI ACCESSO AI DATI 
    adsp = models.CharField('ADSP', help_text='Profilo di accesso', max_length=100)
    adsm = models.CharField('ADSM', help_text='Motivazione', max_length=100)

    # FTA DOCUMENTAZIONE FOTOGRAFICA
    # FTAX', help_text='genere
    # FTAD - data
    # FTAT - note

    # DRA DOCUMENTAZIONE GRAFICA
    # DRAX - genere
    # DRAT - tipo
    # DRAO - note
    # DRAS - scala
    # DRAC - collocazione
    # DRAA - autore
    # DRAD - data

    # CM COMPILAZIONE 
    ## CMP COMPILAZIONE 
    cmpd = models.DateField('CMPD', help_text='Data')
    cmpn = models.CharField('CMPN', help_text='Nome', max_length=100)
    fur = models.CharField('FUR', help_text='Funzionario responsabile', max_length=100)

    def __unicode__(self):
        return self.number

    class Meta:
        verbose_name_plural = "casse"


class ClasseMateriale(models.Model):
    '''Classi di materiale.'''

    classe = models.CharField('CLS', help_text='Classe', max_length=100)
    famiglia = models.CharField(max_length=50, blank=True)


class Materiale(models.Model):
    pass
