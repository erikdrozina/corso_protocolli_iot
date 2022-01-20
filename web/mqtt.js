const clientId = "clientId_" + parseInt(Math.random() * 100);
const host = "broker.mqttdashboard.com";
const port = 8000;

const client = new Paho.MQTT.Client(host, port, clientId);
const topic = "iot/drone/+/sensors";

client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

client.connect({ onSuccess: onConnect });
let count = 0;
function onConnect() {
  console.log("onConnect");
  client.subscribe(topic);
  console.log(clientId + "subscribed to topic " + topic);
}

function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log(
      "Connection lost with " +
        clientId +
        " because " +
        responseObject.errorMessage
    );
  }
  client.connect({ onSuccess: onConnect });
}

const publish = (dest, msg) => {
  console.log("Publish to: ", dest, "with message: ", msg);
  let message = new Paho.MQTT.Message(msg);
  message.destinationName = dest;
  client.send(message);
};

function onMessageArrived(message) {
  console.log(message.payloadString);
  var mjson = JSON.parse(message.payloadString);
  var id = mjson["IdDrone"];
  document.getElementById("IdDrone" + id).innerHTML = mjson["IdDrone"];
  document.getElementById("Status" + id).innerHTML = mjson["Status"]
    ? "On"
    : "Off";
  document.getElementById("Battery" + id).innerHTML = mjson["Battery"];

  if (mjson["Status"]) {
    document.getElementById("box-drone" + id).style.backgroundColor =
      "lightgreen";
  } else {
    document.getElementById("box-drone" + id).style.backgroundColor = "tomato";
  }
}
