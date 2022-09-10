from datetime import datetime
import json
from threading import Thread
import logging
from .subject import Subject
import paho.mqtt.client as mqtt


class MqttSubject(Subject, Thread):
    _mqtt_client = None
    _mqtt_url = None
    _msg = None
    _userdata = None
    _client = None
    _qos = None

    def __init__(self, url, mqttclient: mqtt.Client, qos=0):
        self._mqtt_url = url
        self._qos = qos
        self._mqtt_client = mqttclient
        self._mqtt_client.on_connect = self._subscribe
        self._mqtt_client.on_message = self._notify
        Thread.__init__(self)
        Subject.__init__(self)

    def _notify(self, client, userdata, msg):
        self.logger.info("A msg has received!, Notifying Observers...")
        self._msg = msg
        self._client = client
        self._userdata = userdata
        self._updated_at = datetime.now()
        for observer in self._observers:
            observer.update(self)

    def _subscribe(self, client, userdata, flags, rc):
        client.subscribe(self._mqtt_url, self._qos)

    def connect(self, *args):
        self._mqtt_client.connect(*args)

    def run(self):
        self._mqtt_client.loop_forever()

    @property
    def msg(self):
        return self._msg

    @property
    def userdata(self):
        return self._userdata

    @property
    def client(self):
        return self._client

    @property
    def updated_at(self):
        return self._updated_at
