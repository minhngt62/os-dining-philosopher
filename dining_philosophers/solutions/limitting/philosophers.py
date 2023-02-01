from typing import List, Dict, Tuple, Any
from multiprocessing.synchronize import Semaphore

from ..._states import PhilosopherState
from ...philosophers import Philosopher
from ...forks import Fork
from ...utils import logger

class LimitPhilosopher(Philosopher):
    def __init__(
        self, 
        id_: int,
        state,
        forks: Tuple[Fork, Fork],
        room: Semaphore
        ):
        super().__init__(id_, state, forks)
        self.room = room
    
    def eat(self):
        self.state.value = PhilosopherState.HUNGRY
        logger.info("{:<13}".format(str(self)) + f" {self.state.value.value}")
        
        self.room.acquire()
        self.forks[0].acquire()
        self.forks[1].acquire()

        super().eat()

        self.forks[0].release()
        self.forks[1].release()
        self.room.release()