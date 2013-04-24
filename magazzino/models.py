# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import RegexValidator

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

    def __unicode__(self):
        return "%s - %s" % (self.number, self.scavo)

    class Meta:
        verbose_name_plural = "contesti"


class Magazzino(models.Model):
    '''Un magazzino.'''

    nome = models.CharField(max_length=50)
    descrizione = models.TextField()

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "magazzini"


class Vano(models.Model):
    '''Un vano all'interno di un magazzino.'''

    number = models.IntegerField('Numero del vano')
    magazzino = models.ForeignKey(Magazzino)
    desc = models.TextField('Descrizione')

    def __unicode__(self):
        return '%s %s' % (self.magazzino.__str__(), self.number)

    class Meta:
        verbose_name_plural = 'vani'


class Cassa(models.Model):
    '''Basata sul modello "Scheda di cassa".

    Fa riferimento alla scheda ICCD TMA (Tabella materiali).'''

    # informazioni di base
    number = models.CharField('Numero di cassa', max_length=50)
    scavo = models.ForeignKey(Scavo)
    numscavo = models.IntegerField(
        'Numero di cassa dello scavo',
        blank=True,
        null=True,
        help_text='Il numero di cassa nella numerazione dello scavo, se presente')
    vano = models.ForeignKey(Vano)
    posizione = models.CharField(help_text='Scaffale, colonna o altro',
                                 max_length=100)
    contenuto = models.TextField(blank=True,
                                 help_text='Descrizione estesa del contenuto')
    materiale = models.CharField(max_length=100, blank=True)

    # CD - Codici
    tsk = models.CharField('TSK',
                           help_text='Tipo scheda',
                           max_length=4,
                           default='TMA',
                           editable=False)
    LIR_CHOICES = (
        ('I', 'Inventario'),
        ('P', 'Precatalogo'),
        ('C', 'Catalogo'),
        )
    lir = models.CharField('LIR',
                           help_text='Livello ricerca',
                           max_length=5,
                           choices=LIR_CHOICES)
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
                            max_length=8,
                            unique=True,
                            validators=[RegexValidator('[0-9]'*8)])
    esc = models.CharField('ESC',
                           help_text='Ente schedatore',
                           max_length=25,
                           default='S19')
    ecp = models.CharField('ECP',
                           help_text='Ente competente',
                           max_length=25,
                           default='S19')

    # OG - Oggetto
    ## OGT - Oggetto = Cassa
    scan = models.CharField('SCAN',
                            help_text='Denominazione dello scavo',
                            max_length=100)
    dscd = models.CharField('DSCD',
                            help_text='Data in cui è stato effettuato l’intervento di scavo archeologico',
                            max_length=50)

    # LC - Localizzazione geografico-amministrativa
    ## PVC LOCALIZZAZIONE GEOGRAFICO-AMMINISTRATIVA ATTUALE
    pvcs = models.CharField('PVCS', help_text='Stato', max_length=50, default='Italia')
    pvcr = models.CharField('PVCR', help_text='Regione', max_length=25, default='Liguria')
    pvcp = models.CharField('PVCP', help_text='Provincia', max_length=3, default='IM')
    pvcc = models.CharField('PVCC', help_text='Comune', max_length=50, default='Ventimiglia')

    # LDC - Collocazione specifica
    ldct = models.CharField('LDCT',
                            help_text='Tipologia del contenitore',
                            max_length=25,
                            default='magazzino')
    ldcn = models.CharField('LDCN',
                            help_text='Denominazione magazzino',
                            max_length=50)
    ldcs = models.CharField('LDCS',
                            help_text='Specifiche: vano, sala, corridoio, colonna',
                            max_length=50)

    # DT CRONOLOGIA 
    ## DTZ CRONOLOGIA GENERICA 
    dtzg = models.CharField('DTZG',
                            help_text='Fascia cronologica di riferimento',
                            max_length=50)
    dtm = models.CharField('DTM',
                           help_text='Motivazione cronologia',
                           max_length=250)

    # MA MATERIALE
    ## MAC MATERIALE COMPONENTE 
    macc = models.CharField('MACC', help_text='Categoria', max_length=100)
    macq = models.CharField('MACQ', help_text='Quantità', max_length=100)

    # TU CONDIZIONE GIURIDICA E VINCOLI 
    ## CDG CONDIZIONE GIURIDICA 
    cdgg = models.CharField('CDGG', help_text='Indicazione generica', max_length=50)

    # AD ACCESSO AI DATI 
    ## ADS SPECIFICHE DI ACCESSO AI DATI 
    adsp = models.CharField('ADSP', help_text='Profilo di accesso', max_length=1)
    adsm = models.CharField('ADSM', help_text='Motivazione', max_length=70)

    # FTA DOCUMENTAZIONE FOTOGRAFICA
    ftax = models.CharField('FTAX', help_text='genere', max_length=50)
    ftad = models.CharField('FTAD', help_text='data', max_length=25)
    ftat = models.TextField('FTAT', help_text='note', max_length=250)

    # DRA DOCUMENTAZIONE GRAFICA
    drax = models.CharField('DRAX', help_text='genere', max_length=25)
    drat = models.CharField('DRAT', help_text='tipo', max_length=50)
    drao = models.TextField('DRAO', help_text='note', max_length=250)
    dras = models.CharField('DRAS', help_text='scala', max_length=25)
    drac = models.CharField('DRAC', help_text='collocazione', max_length=50)
    draa = models.CharField('DRAA', help_text='autore', max_length=50)
    drad = models.CharField('DRAD', help_text='data', max_length=25)

    # CM COMPILAZIONE 
    ## CMP COMPILAZIONE 
    cmpd = models.DateField('CMPD', help_text='Data')
    cmpn = models.CharField('CMPN', help_text='Nome', max_length=70)
    fur = models.CharField('FUR', help_text='Funzionario responsabile', max_length=70)

    def __unicode__(self):
        return self.number

    class Meta:
        verbose_name_plural = "casse"


class FormaDiMateriale(models.Model):
    '''Una forma di oggetto.

    Corrisponde al campo OGTD della scheda TMA.'''

    famiglia = models.CharField(max_length=100)
    forma = models.CharField('OGTD',
                             help_text='Forma',
                             max_length=100)

    def __unicode__(self):
        return self.forma

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "forma__icontains", 'famiglia__icontains')

    class Meta:
        verbose_name_plural = 'forme di materiale'
        ordering = ['pk']
        unique_together = ('famiglia', 'forma')


class ClasseDiMateriale(models.Model):
    '''Classi di materiale.

    Corrisponde al campo CLS della scheda TMA.'''

    classe = models.CharField('CLS',
                              help_text='Classe',
                              max_length=100)
    sigla = models.CharField(max_length=12, help_text='Sigla della classe', unique=True)
    famiglia = models.CharField(max_length=50, blank=True)
    forme = models.ManyToManyField(FormaDiMateriale, blank=True)

    def __unicode__(self):
        cls_str = self.sigla
        if self.famiglia:
            cls_str += '%s - ' % (self.famiglia)
        cls_str += self.classe
        return cls_str

    @staticmethod
    def autocomplete_search_fields():
        return ('id__iexact', 'classe__icontains', 'famiglia__icontains')

    class Meta:
        verbose_name_plural = "classi di materiale"
        ordering = ['pk']
        unique_together = ('classe', 'famiglia')


class MaterialeInCassa(models.Model):
    '''Singoli materiali in una cassa.'''

    cassa = models.ForeignKey(Cassa)
    classe = models.ForeignKey(ClasseDiMateriale, verbose_name='CLS - Classe')
    isr = models.CharField('ISR - Iscrizioni', max_length=100, blank=True)
    ogtd = models.ForeignKey(FormaDiMateriale,  verbose_name='OGTD - Forma')
    ogtt = models.CharField('OGTT - Tipologia',
                            max_length=200,
                            help_text='Tipologia, es “Lamboglia 9” o “Dressel 23”',
                            blank=True)

    # conteggi

    help_text_inv = '''Numeri singoli separati da barre es. 123/124/125
oppure intervalli di numeri separati da trattino es. 123-126'''

    orli = models.IntegerField()
    numeri_inventario_orli = models.CharField(max_length=500,
                                              help_text=help_text_inv)

    anse = models.IntegerField()
    numeri_inventario_anse = models.CharField(max_length=500,
                                              help_text=help_text_inv)

    fondi = models.IntegerField()
    numeri_inventario_fondi = models.CharField(max_length=500,
                                               help_text=help_text_inv)

    piedi = models.IntegerField()
    numeri_inventario_piedi = models.CharField(max_length=500,
                                               help_text=help_text_inv)

    pareti = models.IntegerField()
    numeri_inventario_pareti = models.CharField(max_length=500,
                                                 help_text=help_text_inv)

    nme = models.IntegerField('NME', help_text='Numero minimo di esemplari')

    # inventario

    def __unicode__(self):
        return '%s in %s' % (self.classe, self.cassa)

    class Meta:
        verbose_name_plural = "materiali in cassa"
