from typing import List, Dict, Tuple, Any
from multiprocessing.synchronize import Semaphore

from ..._states import PhilosopherState
from ...philosophers import Philosopher, logger
from ...forks import Fork

class LimitPhilosopher(Philosopher):
    def __init__(
        self, 
        id_: int,
        forks: Tuple[Fork, Fork],
        room: Semaphore
        ):
        super().__init__(id_, forks)
        self.room = room
    
    def eat(self):
        self.state = PhilosopherState.HUNGRY
        logger.info("{:<13}".format(str(self)) + f" {self.state.value}")
        
        self.room.acquire()
        self.forks[0].acquire()
        self.forks[1].acquire()

        super().eat()

        self.forks[0].release()
        self.forks[1].release()
        self.room.release()