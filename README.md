# Repo per il corso Protocolli IoT

## Componenti:

- [Erik Drozina](https://github.com/erikdrozina)
- [Rudi Folla](https://github.com/FollaRudi)


## **MQTT**
### **TOPICS**
<u>iot/drone/{id}/sensors</u>

Ascolta i dati provenienti dai sensori di un determinato drone.


<u>iot/drone/{id}/command</u>

Ascolta i comandi provenienti dal server ad un determinato drone.

Abbiamo suddiviso il drone e i suo id per due semplici motivi:
- Se si vogliono sapere tutti i dati/comandi di tutti i droni basta usare `iot/drone/+/sensors` / `iot/drone/+/commands`
- Se si vogliono sapere tutti i dati e comandi di un determinato drone basta usare `iot/drone/{id}/#` oppure di tutti i droni `iot/drone/#`

### **QOS**
I comandi hanno un QOS di 2 in modo tale che il comando venga mandato ed eseguito nel modo più affidabile possibile per evitare incidenti o infortuni.

I dati dei sensori hanno un QOS di 0, se non vengono inviati al server le conseguenze sono minori.

### **FLAGS**
Il topic per ottenere i dati dei senori ha il flag ```retained``` a ```True``` in modo tale che appena un subscriber si connette al topic può ottenere gli utlimi dati dal broker stesso.

Il subscriber che vuole ottenere i comandi ha il flag ```clean_session``` a ```True``` in modo tale che, una volta acceso il drone, non legga ed esegua i comandi inviati mentre era spento.

### **SICUREZZA**
Inanzitutto mettiamo dei paletti a chi e dove si può scrivere. 

Per esempio, un drone potrà solamente pubblicare nel topic ```iot/drone/{id}/sensors```, non potrà pubblicare negli altri topic con altri id o nel topic destinato ai comandi.

Un drone potrà iscriversi solamente al topic ```iot/drone/{id}/command``` per evitare che i comandi destinati ad un drone possano essere letti da un altro drone.

I comandi possono essere mandati sul topic del drone solamente dal controllore abbinato al drone affidato all'utente al momento del noleggio e dai gestori del noleggio dei droni che possono mandare comandi da remoto.

Successivamente instauriamo una connessione tramite VPN per rendere sicura la comunicazione dei dati e comandi dall'esterno.