# Esercitazione pista sciistica

## Componenti:

- [Erik Drozina](https://github.com/erikdrozina)
- [Rudi Folla](https://github.com/FollaRudi)

## Spiegazione

### Panoramica

I totem verranno posizionati in un punto lento della pista per non far fermare completamente lo sciatore, in un punto con alimentazione e dotati di una SIM per la comunicazione. Saranno dotati di un lettore di skypass (RFID) e lo sciatore dovrà convalidare lo skypass similmente a come si fa ai tornelli.

Per controllare che lo sciatore ha validato le piste, si verificherà se l'id dello skypass ha passato determinati totem.
Il totem sarà fornito di uno schermo LCD o un semplice LED che mostrerà allo sciatore la conferma del passaggio in quella pista.

### Protocollo

Il protocollo IoT scelto per far comunicare i totem è MQTT peri seguenti motivi:

- permette un controllo dello stato dell totem
- posso iscivermi solamente ai topic desiderati o limitarne la scrittura/lettura solo su topic scelti
- posso assegnare un QOS per garantire la ricezione dei messaggi
- possibilità di monitorare i topic tramite pagina web con MQTT via websocket

Il broker MQTT verrà posizionato nella sede centrale assieme al server che erlaborerà i messaggi ed un database per l'inserimento dei dati.

### Totems

Il totem raccoglierà i dati degli sciatori, che verranno successivamente mandati tramite il protocollo MQTT al server dell'impianto.

Il topic del messaggio sarà composto da "comprensorio_sciisctico/totem_id/skypass_id" in modo tale da monitorare il percorso dello sciatore o monitorare il totem tramite wildcards.
Nel corpo del messaggio verrà scritto l'id dello skypass, l'id del totem, il nome/numero della pista in cui il totem si trova e la data in cui è stato validato lo skypass.

```
{
    "skypass_id": 12345,
    "totem_id": 1,
    "pista_id": 12,
    "data": "2022_01_27"
}
```

Per conoscere lo stato del totem invierà un messaggio al topic "comprensorio_sciisctico/totem_id/status" in cui scriverà il suo stato e l'orario in cui questa verifica viene fatta.
Per i totem impostiamo un keepalive di 15 minuti e impostiamo un last will message che venga mandato nello stesso canale in cui segnerà che il totem ha problemi e l'orario, in modo tale che l'operatore possa vedere quando il totem è stato disconnesso.

I totem avranno il permesso di scrivere solamente nel topic con il proprio totem_id e i messaggi verranno mandati con un QOS uguale a 1.

### Server

Una volta che il server riceve i messaggi, eseguirà i seguenti controlli:

- lo skypass sia valido e attivo per qella giornata
- che il totem precendete sia un totem valido (come ad esempio il totem/tornello della funivia/cabinovia) per evitare che il totem venga convalidato più volte

Se i controlli sono soddisfatti, verrà controllato il progresso nella sfida per eventualmente notificare lo sciatore e infine il messaggio verrà immagazzinato nel database.
