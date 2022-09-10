import logging


class Observer:
    _last_change = None

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def update(self, subject):
        self._last_change = subject.updated_at

    @property
    def last_change(self):
        return self._last_change
