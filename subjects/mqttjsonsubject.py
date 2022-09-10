from datetime import datetime
import json
import logging
from .mqttsubject import MqttSubject
import paho.mqtt.client as mqtt


class MqttJsonSubject(MqttSubject):
    def __init__(self, url, mqttclient: mqtt.Client):
        super().__init__(url, mqttclient)
        self.logger = logging.getLogger(__name__)

    def _notify(self, client, userdata, msg):
        try:
            super()._notify(client=client, userdata=userdata, msg=json.loads(msg.payload))

        except json.JSONDecodeError:
            self.logger.error(f"JSONDecodeError,  msg:{msg.payload}")
        except TypeError as e:
            self.logger.error(f"{e}: msg:{msg}")

