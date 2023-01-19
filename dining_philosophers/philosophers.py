import threading
import logging
from random import uniform
import time
from typing import List, Dict, Tuple, Any

from .loggers import config_logging
config_logging("dining_philosophers\loggers\config.yaml")
logger = logging.getLogger(__name__)

from ._states import PhilosopherState
from .forks import Fork

class Philosopher(threading.Thread):
    EAT_TIMES_UNTIL_FULL = 3

    def __init__(
        self, 
        id: int,
        forks: Tuple[Fork, Fork],
        ):
        threading.Thread.__init__(self)
        
        self.id = id
        self.state = PhilosopherState.THINKING
        self.forks = forks
        self._full = 0
    
    def run(self):
        while self._full < self.EAT_TIMES_UNTIL_FULL:
            self.eat()
            self._full += 1
            self.think()
        logger.info("{:<13}".format(str(self)) + f" I'm full.")
        return

    def eat(self):
        # Set hungry state here
        # PROCESS SYNCH HERE
        
        self.state = PhilosopherState.EATING
        logger.info("{:<13}".format(str(self)) + f" {self.state.value}" + f" ({self._full + 1})")
        time.sleep(uniform(1.2, 5.0))

    def think(self):
        self.state = PhilosopherState.THINKING
        logger.info("{:<13}".format(str(self)) + f" {self.state.value}")
        time.sleep(uniform(1.2, 5.0))

    def __repr__(self) -> str:
        return f'[PHILOSOPHER {self.id:02}]'