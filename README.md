# Repo per il corso Protocolli IoT

## Componenti:

- [Erik Drozina](https://github.com/erikdrozina)
- [Rudi Folla](https://github.com/FollaRudi)

## **AMQP**

### **CODE**

Per raccogliere i dati dei sensori, ogni drone manda i dati di telemetria nella stessa coda. Nei dati raccolti dal server, il primo paramentro corrisponde all'id del drone in modo tale da determinarne la provenienza.

Per i comandi assegniamo una coda ad ogni drone in modo tale che ogni drone consumi solamente i comandi dalla corrispettiva coda.

### **EXCHANGE**

Come Excange usiamo un Headers Exchange che permette di instradare su più route specificate nell'attributo nel header del messaggio rispetto che nella routing key, ignorandola.

Come Exchange si comporta similmente ad un DIrect Exchange come performance e routing algorithm.
