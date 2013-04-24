=========================
 Considerazioni generali
=========================

Si possono adottare due approcci opposti alla creazione di un database
che debba essere compatibile con le specifiche ICCD:

1. corrispondenza molto stretta con le specifiche, cercando di
   replicare in dettaglio tutti i campi, le obbligatorietà e così via
2. creare un modello ad hoc, tipicamente semplificato rispetto
   all'originale in particolare per la ripetitività di molti campi, e
   demandare la creazione di un tracciato conforme alle specifiche ad
   una operazione di esportazione

Apparentemente l'approccio 1 è quello più usato, anche nel caso di
sviluppi più recenti come le versioni XML dei tracciati (ArtIn di
Liberologico). È perfettamente legittimo. Però questo significa che
non ci sono strumenti di conversione.

Tabella materiali (TMA)
=======================

Il fulcro della scheda di cassa e della scheda TMA in generale è il
paragrafo `MA` (materiale), che deve essere ripetuto per ogni “record”
dettagliato. Facciamo un esempio in cui ho:

- 1 orlo e 2 pareti di Hayes 50 in sigillata africana C
- 1 orlo di Hayes 14 in sigillata africana A
- 1 ansa e 1 fondo di anfora Gauloise 4.

La parte di tracciato corrispondente sarà come segue.

::

   MA:
   MAC:
   MACC: ceramica
   MACL: Terra sigillata africana C
   MACD: scodella
   MACP: Hayes 50
   MACQ: 3
   MAD:
   MADD: orlo
   MADQ: 1
   MADI: 1
   MAD:
   MADD: parete
   MADQ: 2
   MADI: 2/3
   MA:
   MAC:
   MACC: ceramica
   MACL: Terra sigillata africana A
   MACD: coppa
   MACP: Hayes 14
   MACQ: 1
   MAD:
   MADD: orlo
   MADQ: 1
   MADI: 4
   MA:
   MAC:
   MACC: ceramica
   MACL: Anfore galliche
   MACD: anfora
   MACP: Gauloise 4
   MACQ: 1
   MAD:
   MADD: ansa
   MADQ: 1
   MADI: 5
   MAD:
   MADD: fondo
   MADQ: 1
   MADI: 6

Quindi per ogni gruppo tipologico va ripetuto il paragrafo `MA` e
all'interno va ripetuto il campo `MAD` per ogni gruppo di orli,
pareti, etc. Il campo `MAC` invece non è ripetitivo ed è unico per
ogni paragrafo `MA`. Sintetizzando l'esempio sopra::

  MA
   MAC
   MAD
   MAD
  MA
   MAC
   MAD
  MA
   MAC
   MAD
   MAD

Il campo `MACQ` non va inserito manualmente nel database ma deve
essere ricavato dalla somma dei campi `MADQ` corrispondenti. Sarebbe
utile poter mostrare in tempo reale durante la compilazione della
scheda che viene calcolato il totale.

Lo scavo
--------

Le indicazioni sulla provenienza da scavo del materiale vanno inserite
nel campo `RE:DSC`, in cui si può indicare anche il numero di
inventario della cassa se gliene è stato assegnato uno specificamente
per lo scavo. Ad esempio::

  RE:
  DSC:
  SCAN: Ventimiglia, teatro romano, cavea, concamerazione est
  DSCF: Soprintendenza per i Beni Archeologici della Liguria
  DSCA: Gambaro, Luigi
  DSCD: 2013/01/07-2013/03/15
  DSCH: VGT
  DSCU: US 23
  DSCI: 12

Il campo `DSCI` (Numero inventario di scavo) può indicare il numero
della cassa nell'insieme dello scavo.

Questo è molto più stringato rispetto al forte dettaglio richiesto nel
nostro caso per l'indicazione della posizione degli strati o US, che
in pratica ricalca quello della scheda US:

- area (es. “teatro”)
- settore (es. “cavea”, “postscaenium”)
- saggio o scavo
- US o strato

Quindi i primi tre campi vanno tenuti separati nel database ma uniti
al momento dell'esportazione insieme all'indicazione della località di
scavo, costituendo il campo `SCAN`.

È possibile indicare queste informazioni forse anche con il campo `LA`
(altre localizzazioni geografico-amministrative), es::

  LA:
  TCL:  luogo di reperimento
  PRV:
  PRVR: Liguria
  PRVP: IM
  PRVC: Ventimiglia
  PRVL: Nervia
  PRC:
  PRCT: teatro
  PRCD: Teatro romano di Albintimilium
  PRCS: parascaenium

Ma non sembra una soluzione molto soddisfacente. In effetti il
problema è causato dalla necessità di combinare informazioni che sono
concepite per essere separate.

Campi specifici
---------------

Nel modello creato per il progetto locale ci sono alcuni elementi che
non sembrano corretti rispetto alle specifiche della scheda TMA.

DTZG
~~~~

Nella scheda TMA il campo `DT:DTZ:DTZG` è obbligatorio e indica la
cronologia generica. È problematica nel caso di piccoli scavi in cui
nella stessa cassa sono conservati materiali di US diverse, a conferma
del fatto che la scheda andrebbe considerata sulla base delle US e non
delle cassette. È comunque possibile indicare una cronologia molto
generica come "Età romana".

È obbligatorio anche il campo `DT:DTM` (motivazione cronologia) che
può comunque essere molto generico, tipo “analisi dei materiali”.

OGTD
~~~~

Nella scheda TMA il campo `OG:OGT:OGTD` è riferito alla intera scheda
e non può essere usato per un singolo oggetto, quindi deve indicare il
materiale nel suo complesso, es, “materiale proveniente da Unità
Stratigrafica”.

OGTT
~~~~

Nella scheda TMA il campo `OG:OGT:OGTT` non esiste e va indicata la
tipologia dei singoli oggetti nel campo `MA:MAC:MACP` (precisazioni
tipologiche).

MACC
~~~~

Il campo `MA:MAC:MACC` deve usare lo stesso vocabolario del campo
`OG:OGT:OGTM`. La differenza tra i due è che `OGTM` è un campo al
livello dell'intera scheda e quindi descrive il contenuto di una US o
di una cassa, mentre `MACC` è riferito al gruppo di oggetti specifico
(es. frammenti di una coppa Dragendorff 27). Nella scheda TMA non è
previsto il campo `MTC` (materia e tecnica) che invece fa parte della
scheda RA (reperto archeologico) e ha una connotazione più di
dettaglio.

MADI
~~~~

Il campo `MA:MAD:MADI` contiene i numeri di inventario dei pezzi
indicati e deve usare questa sintassi:

- numeri singoli separati da barre es. 121/124/128
- intervalli di numeri separati da trattino es. 123-126

ISR
~~~

Il campo `ISR` non fa parte della scheda TMA. Quindi va tenuto a parte
e inserito nel campo `MA:MAD:MADN` quando viene esportato.

Livello inventariale
--------------------

A livello inventariale si può mantenere un dettaglio ridotto, visto
che gli unici campi obbligatori sono `MA`, `MAC`, `MACC` e `MACQ`. Ad
esempio::

  MA:
  MAC:
  MACC: ceramica
  MACQ: 34
  MA:
  MAC:
  MACC: vetro
  MACQ: 12

Ma questo non è specificamente di interesse per il nostro caso, o
forse sì nel senso che è meglio avere delle schede di livello
inventariale che non avere niente.
