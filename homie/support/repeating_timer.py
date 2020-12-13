import time
from threading import Event, Thread
import traceback

import logging

logger = logging.getLogger(__name__)


class Repeating_Timer(object):

    """Repeat `function` every `interval` seconds."""

    def __init__(self, interval):
        self.interval = float(interval)
        self.event = Event()
        self.thread = Thread(target=self._target)
        self.thread.daemon = True
        self.thread.start()
        self.callbacks = []

    def _target(self):
        while not self.event.wait(self.interval):
            for callback in self.callbacks:
                try:
                    callback()
                except Exception as e:
                    logger.error("Error in timer callback: {}  {}".format(e,traceback.format_exc()))

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def stop(self):
        self.event.set()
        self.thread.join()

