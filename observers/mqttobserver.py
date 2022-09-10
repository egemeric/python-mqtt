import logging
from .observer import Observer


class MqttObserver(Observer):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def update(self, subject):
        super().update(subject)
        self.logger.info(f"observer catched the update: {subject.msg}")
