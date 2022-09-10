import logging


class Subject():
    _observers = []

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            self.logger.error("value error")

    def notify(self):
        for observer in self._observers:
            observer.update()
