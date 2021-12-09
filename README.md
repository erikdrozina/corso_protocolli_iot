# Repo per il corso Protocolli IoT

## Componenti:

- [Erik Drozina](https://github.com/erikdrozina)
- [Rudi Folla](https://github.com/FollaRudi)


## MQTT
### **Topic:** iot/drone/{id}/sensors
Ascolta i dati provenienti dai sensori di un determinato drone.


### **Topic:** iot/drone/{id}/command
Ascolta i comandi provenienti dal server ad un determinato drone.

Abbiamo suddiviso il drone e i suo id per due semplici motivi:
- Se si vogliono sapere tutti i dati/comandi di tutti i droni basta usare `iot/drone/+/sensors` / `iot/drone/+/commands`
- Se si vogliono sapere tutti i dati e comandi di un determinato drone basta usare `iot/drone/{id}/#` oppure di tutti i droni `iot/drone/#`

I comandi hanno un QOS di 2 in modo tale che il comando venga mandato ed eseguito nel modo più affidabile possibile per evitare incidenti o infortuni.

I dati dei sensori hanno un QOS di 0, se non vengono inviati al server le conseguenze sono minori.
