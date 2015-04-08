# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cassa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=50, verbose_name=b'Numero di cassa')),
                ('numscavo', models.IntegerField(help_text=b'Il numero di cassa nella numerazione dello scavo, se presente', null=True, verbose_name=b'Numero di cassa dello scavo', blank=True)),
                ('tsk', models.CharField(default=b'TMA', help_text=b'Tipo scheda', max_length=4, editable=False, verbose_name=b'TSK')),
                ('lir', models.CharField(default=b'I', help_text=b'Livello ricerca', max_length=5, verbose_name=b'LIR', choices=[(b'I', b'Inventario'), (b'P', b'Precatalogo'), (b'C', b'Catalogo')])),
                ('nctr', models.CharField(default=b'07', help_text=b'Codice regione', max_length=2, verbose_name=b'NCTR', choices=[(b'01', b'Piemonte'), (b'02', b"Valle d'Aosta"), (b'03', b'Lombardia'), (b'04', b'Trentino-Alto Adige'), (b'05', b'Veneto'), (b'06', b'Friuli-Venezia Giulia'), (b'07', b'Liguria'), (b'08', b'Emilia-Romagna'), (b'09', b'Toscana'), (b'10', b'Umbria'), (b'11', b'Marche'), (b'12', b'Lazio'), (b'13', b'Abruzzo'), (b'14', b'Molise'), (b'15', b'Campania'), (b'16', b'Puglia'), (b'17', b'Basilicata'), (b'18', b'Calabria'), (b'19', b'Sicilia'), (b'20', b'Sardegna')])),
                ('nctn', models.CharField(default=b'00000000', max_length=8, validators=[django.core.validators.RegexValidator(b'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')], help_text=b'Numero catalogo generale', unique=True, verbose_name=b'NCTN')),
                ('esc', models.CharField(default=b'S19', help_text=b'Ente schedatore', max_length=25, verbose_name=b'ESC')),
                ('ecp', models.CharField(default=b'S19', help_text=b'Ente competente', max_length=25, verbose_name=b'ECP')),
                ('dscd', models.CharField(help_text=b'\nData in cui \xc3\xa8 stato effettuato l\xe2\x80\x99intervento di scavo archeologico,\nnel formato AAAA/MM/GG. Esempi: 2002/03/25, 2004/00/00, 2005/07/21-2005/10/12.', max_length=50, verbose_name=b'DSCD', validators=[django.core.validators.RegexValidator(b'[0-9][0-9][0-9][0-9]/[0-1][0-9]/[0-3][0-9]')])),
                ('pvcs', models.CharField(default=b'Italia', help_text=b'Stato', max_length=50, verbose_name=b'PVCS')),
                ('pvcr', models.CharField(default=b'Liguria', help_text=b'Regione', max_length=25, verbose_name=b'PVCR')),
                ('pvcp', models.CharField(default=b'IM', help_text=b'Provincia', max_length=3, verbose_name=b'PVCP')),
                ('pvcc', models.CharField(default=b'Ventimiglia', help_text=b'Comune', max_length=50, verbose_name=b'PVCC')),
                ('ldct', models.CharField(default=b'magazzino', help_text=b'Tipologia del contenitore', max_length=25, verbose_name=b'LDCT')),
                ('ldcs', models.CharField(help_text=b'Specifiche: corridoio, colonna', max_length=50, verbose_name=b'LDCS')),
                ('dtzg', models.CharField(help_text=b'Fascia cronologica di riferimento', max_length=50, verbose_name=b'DTZG')),
                ('dtm', models.CharField(help_text=b'Motivazione cronologia', max_length=250, verbose_name=b'DTM', choices=[(b'analisi dei materiali', b'analisi dei materiali'), (b'analisi chimico-fisica', b'analisi chimico-fisica'), (b'analisi stilistica', b'analisi stilistica'), (b'bibliografia', b'bibliografia'), (b'bollo', b'bollo'), (b'contesto', b'contesto'), (b'data', b'data'), (b'dati epigrafici', b'dati epigrafici'), (b'documentazione', b'documentazione'), (b'tradizione orale', b'tradizione orale'), (b'NR (recupero pregresso)', b'NR (recupero pregresso)')])),
                ('macc', models.CharField(help_text=b'Categoria: es. ceramica oppure ceramica/vetro/metallo', max_length=100, verbose_name=b'MACC')),
                ('macq', models.CharField(help_text=b'Quantit\xc3\xa0', max_length=100, verbose_name=b'MACQ')),
                ('cdgg', models.CharField(default=b'propriet\xc3\xa0 Stato', help_text=b'Condizione giuridica - Indicazione generica', max_length=50, verbose_name=b'CDGG')),
                ('adsp', models.CharField(default=b'1', help_text=b'Profilo di accesso', max_length=1, verbose_name=b'ADSP', choices=[(b'1', b'intera scheda visibile'), (b'2', b'limitazione per privacy e tutela')])),
                ('adsm', models.CharField(default=b'dati liberamente accessibili', help_text=b'Motivazione', max_length=70, verbose_name=b'ADSM')),
                ('ftax', models.CharField(help_text=b'genere', max_length=50, verbose_name=b'FTAX')),
                ('ftad', models.CharField(help_text=b'data', max_length=25, verbose_name=b'FTAD')),
                ('ftat', models.TextField(help_text=b'note', max_length=250, verbose_name=b'FTAT')),
                ('drax', models.CharField(help_text=b'genere', max_length=25, verbose_name=b'DRAX')),
                ('drat', models.CharField(help_text=b'tipo', max_length=50, verbose_name=b'DRAT')),
                ('drao', models.TextField(help_text=b'note', max_length=250, verbose_name=b'DRAO')),
                ('dras', models.CharField(help_text=b'scala', max_length=25, verbose_name=b'DRAS')),
                ('drac', models.CharField(help_text=b'collocazione', max_length=50, verbose_name=b'DRAC')),
                ('draa', models.CharField(help_text=b'autore', max_length=50, verbose_name=b'DRAA')),
                ('drad', models.CharField(help_text=b'data', max_length=25, verbose_name=b'DRAD')),
                ('cmpd', models.DateField(help_text=b'Data', verbose_name=b'CMPD')),
                ('cmpn', models.CharField(help_text=b'Nome', max_length=70, verbose_name=b'CMPN')),
                ('fur', models.CharField(help_text=b'Funzionario responsabile', max_length=70, verbose_name=b'FUR')),
            ],
            options={
                'verbose_name_plural': 'casse',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClasseDiMateriale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('classe', models.CharField(help_text=b'Classe - MACL', max_length=100)),
                ('sigla', models.CharField(help_text=b'Sigla della classe', unique=True, max_length=12)),
                ('famiglia', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'classi di materiale',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContestoScavo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_nome', models.CharField(help_text=b'Es. \xe2\x80\x9cUS 551\xe2\x80\x9d, \xe2\x80\x9cStrato II, parodos est, 3\xc2\xb0 taglio\xe2\x80\x9d.', max_length=50, verbose_name=b'Numero o nome')),
            ],
            options={
                'verbose_name_plural': 'contesti di scavo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormaDiMateriale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('famiglia', models.CharField(max_length=100)),
                ('forma', models.CharField(help_text=b'Forma', max_length=100, verbose_name=b'OGTD')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'forme di materiale',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MaterialeInCassa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('macp', models.CharField(help_text=b'Tipologia, es \xe2\x80\x9cLamboglia 9\xe2\x80\x9d o \xe2\x80\x9cDressel 23\xe2\x80\x9d', max_length=200, verbose_name=b'MACP- Tipologia', blank=True)),
                ('macn_isr', models.CharField(max_length=100, verbose_name=b'ISR - Iscrizioni', blank=True)),
                ('macn', models.CharField(max_length=100, verbose_name=b'MACN - Annotazioni', blank=True)),
                ('orli', models.IntegerField(default=0)),
                ('numeri_inventario_orli', models.CharField(help_text=b'Numeri singoli separati da barre es. 123/124/125\noppure intervalli di numeri separati da trattino es. 123-126', max_length=500)),
                ('anse', models.IntegerField(default=0)),
                ('numeri_inventario_anse', models.CharField(help_text=b'Numeri singoli separati da barre es. 123/124/125\noppure intervalli di numeri separati da trattino es. 123-126', max_length=500)),
                ('fondi', models.IntegerField(default=0)),
                ('numeri_inventario_fondi', models.CharField(help_text=b'Numeri singoli separati da barre es. 123/124/125\noppure intervalli di numeri separati da trattino es. 123-126', max_length=500)),
                ('piedi', models.IntegerField(default=0)),
                ('numeri_inventario_piedi', models.CharField(help_text=b'Numeri singoli separati da barre es. 123/124/125\noppure intervalli di numeri separati da trattino es. 123-126', max_length=500)),
                ('pareti', models.IntegerField(default=0)),
                ('numeri_inventario_pareti', models.CharField(help_text=b'Numeri singoli separati da barre es. 123/124/125\noppure intervalli di numeri separati da trattino es. 123-126', max_length=500)),
                ('nme', models.IntegerField(default=1, help_text=b'Numero minimo di esemplari', verbose_name=b'NME')),
                ('cassa', models.ForeignKey(to='magazzino.Cassa')),
                ('contesto', models.ForeignKey(to='magazzino.ContestoScavo')),
                ('macd', models.ForeignKey(verbose_name=b'MACD - Forma', to='magazzino.FormaDiMateriale')),
                ('macl', models.ForeignKey(verbose_name=b'MACL - Classe', to='magazzino.ClasseDiMateriale')),
            ],
            options={
                'verbose_name_plural': 'materiali in cassa',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scavo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=5, choices=[(b'TEATR', b'Teatro'), (b'TERME', b'Terme'), (b'GAS', b'Gas'), (b'CAVAL', b'Cavalcavia'), (b'NECRO', b'Necropoli'), (b'VALTA', b'Ventimiglia alta'), (b'EXTRA', b'Scavi extraurbani')])),
                ('settore', models.CharField(max_length=50)),
                ('scan', models.CharField(help_text=b"\nDenominazione dello scavo. Es.\xe2\x80\x9cAlbintimilium, teatro, parodos est\xe2\x80\x9d.\nSeguire sempre l'ordine dal generale al particolare.", unique=True, max_length=45, verbose_name=b'SCAN')),
                ('scad', models.TextField(help_text=b'Descrizione', verbose_name=b'SCAD')),
                ('luogo', models.CharField(max_length=100, verbose_name=b'Localit\xc3\xa0')),
                ('dsch', models.CharField(help_text=b'Sigla identificativa. Es. \xe2\x80\x9cVGF\xe2\x80\x9d, \xe2\x80\x9cXXSP\xe2\x80\x9d', max_length=8, verbose_name=b'DSCH', blank=True)),
            ],
            options={
                'verbose_name_plural': 'scavi',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vano',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField(verbose_name=b'Numero del vano')),
                ('magazzino', models.CharField(max_length=5, choices=[(b'ENEL', b'Magazzino ENEL'), (b'GAS', b'Magazzino Gas'), (b'ANTIQ', b'Magazzino Antiquarium')])),
                ('desc', models.TextField(verbose_name=b'Descrizione')),
            ],
            options={
                'verbose_name_plural': 'vani',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='formadimateriale',
            unique_together=set([('famiglia', 'forma')]),
        ),
        migrations.AddField(
            model_name='contestoscavo',
            name='scavo',
            field=models.ForeignKey(to='magazzino.Scavo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='classedimateriale',
            name='forme',
            field=models.ManyToManyField(to='magazzino.FormaDiMateriale', blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='classedimateriale',
            unique_together=set([('classe', 'famiglia')]),
        ),
        migrations.AddField(
            model_name='cassa',
            name='ldcn',
            field=models.ForeignKey(verbose_name=b'LDCN', to='magazzino.Vano', help_text=b'Magazzino e vano'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='cassa',
            unique_together=set([('ldcn', 'number')]),
        ),
    ]
