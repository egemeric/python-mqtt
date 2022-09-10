from subjects.mqttjsonsubject import MqttJsonSubject
from observers.mqttobserver import MqttObserver
import paho.mqtt.client as mqtt
import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(name)s:: %(message)s", handlers=[
                    logging.FileHandler("application.log")])


def main():
    client = mqtt.Client(client_id="sub2", clean_session=False)
    barometer_subject = MqttJsonSubject(url="/home/egemeric/ESP8266Client-3C:61:05:E4:BF:D5/#",mqttclient=client)
    barometer_subject.connect("10.1.1.2",1883,60)

    barometer_subject.attach(MqttObserver())

    barometer_subject.run()

if __name__ == "__main__":
    main()