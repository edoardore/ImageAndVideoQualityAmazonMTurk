# ImageQualityAmazonMTurk

## Come utilizzare il codice:
* Trascinare nella cartella 'images' le immagini che si intende far valutare su Amazon MTurk.
* Eseguire il modulo imageManager.py, le immagini inserite nella cartella verranno caricate sul Bucket di Amazon S3 e verranno collezionati i rispettivi indirizzi. [Il servizio di hosting delle immagini può essere anche fornito da altri]
* Eseguire il modulo Create.py per creare un numero di HITs pari alle immagini caricate su S3 (quelle trascinate al punto iniziale). Le HITs vengono assegnate a 5 utenti differenti da Amazon tramite il parametro MaxAssignments = 5 e non possono essere valutate più di una volta.
* Eseguire il modulo Results.py per ricevere i risultati delle immmagini per ognuno dei 5 Worker che le hanno valutate.
* [Opzionale] il modulo Delete.py serve ad eliminare le HITs appena create

Il modulo initDB.py serve ad inizializzare il database mySQL in localhost per ricevere i dati dalla piattaforma.
Le colonne del DB sono: worker id, età, sesso, qualità immagine, risoluzione schermo (acquisita automaticamente).

##Video Example:
[![Watch the video](InkedCattura_LI.jpg)](https://drive.google.com/file/d/1NCrJDslsOT436VfNLMmBHUkw5WCCPaJq/view?usp=sharing)


## License
[Edoardo Re](https://github.com/edoardore), 2019

