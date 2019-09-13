# ImageAndVideoQualityAmazonMTurk

## Come utilizzare il codice:
#### Image quality:
* Trascinare nella cartella 'images' le immagini che si intende far valutare su Amazon MTurk.
* Eseguire il modulo CreateImmHIT.py per creare un numero di HITs pari alle immagini trascinate nella cartella images. Le HITs vengono assegnate a 5 utenti differenti da Amazon tramite il parametro MaxAssignments = 5 e non possono essere valutate più di una volta da parte di uno stesso utente.
* Eseguire il modulo ResultsImm.py per ricevere i risultati delle immmagini per ognuno dei 5 Worker che le hanno valutate, fino a che non vi sono almeno 3 Workers che hanno sottomesso un assignment non si inseriscono i risultati nel DB MinAssignments = 3.
* [Opzionale] il modulo DeleteImm.py serve ad eliminare le HITs appena create
* [Opzionale] se si intende creare nuove HITs basta trascinare altre immagini nella cartella ed eseguire di nuovo CreateImmHIT.py, in automatico si creeranno HIT solo con le nuove immagini da far valutare.
#### Video quality:
* Trascinare nella cartella 'videos' i video che si intende far valutare su Amazon MTurk.
* Eseguire il modulo CreateVideoHIT.py per creare un numero di HITs pari ai video trascinati nella cartella videos. Le HITs vengono assegnate a 5 utenti differenti da Amazon tramite il parametro MaxAssignments = 5 e non possono essere valutate più di una volta da parte di uno stesso utente.
* Eseguire il modulo ResultsVideo.py per ricevere i risultati dei video per ognuno dei 5 Worker che le hanno valutate, fino a che non vi sono almeno 3 Workers che hanno sottomesso un assignment non si inseriscono i risultati nel DB MinAssignments = 3.
* [Opzionale] il modulo DeleteVideo.py serve ad eliminare le HITs appena create
* [Opzionale] se si intende creare nuove HITs basta trascinare altri video nella cartella ed eseguire di nuovo CreateVideoHIT.py, in automatico si creeranno HIT solo con i nuovi video da far valutare.


#### Other .py files:
Il modulo initDB.py serve ad inizializzare il database mySQL in localhost per ricevere i dati dalla piattaforma.
Le colonne del DB sono:
immquality: 
worker id, età, sesso, qualità immagine, risoluzione schermo (acquisita automaticamente).
vidquality:
worker id, età, sesso, qualità video, risoluzione schermo (acquisita automaticamente).


Il modulo imageManager.py viene chiamato da Create.py per caricare sul bucket S3 le immagini nella cartella images.
Il modulo videoManager.py viene chiamato da Create.py per caricare sul bucket S3 i video nella cartella videos.

Il modulo Key.py serve a raccogliere tutti gli identificativi necessari.
### Video Example:
[![Watch the video](InkedCattura_LI.jpg)](https://drive.google.com/file/d/1C38FKbey1eFeFJC5GUU5YzXqckEMmoSj/view?usp=sharing)

Nel video si valutano inizialmente 2 HITs con 3 account differenti, si mostra che sono necessarie almeno 3 valutazioni di una immagine affinchè vengano inserite nel DB. Si aggiunge in un secondo momento una terza immagine e si esegue Create.py, i Workers hanno così a disposizione una nuova HIT collegata alle precedenti. 

## License
[Edoardo Re](https://github.com/edoardore), 2019

