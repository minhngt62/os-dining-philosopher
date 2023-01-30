from typing import List, Dict, Tuple, Any
from multiprocessing.synchronize import Semaphore

from ..._states import PhilosopherState
from ...philosophers import Philosopher, logger
from ...forks import Fork

class ArbitratorPhilosopher(Philosopher):
    def __init__(
        self, 
        id_: int,
        state,
        forks: Tuple[Fork, Fork],
        waiter: Semaphore
        ):
        super().__init__(id_, state, forks)
        self.waiter = waiter
    
    def eat(self):
        self.state.value = PhilosopherState.HUNGRY
        logger.info("{:<13}".format(str(self)) + f" {self.state.value.value}")
        
        self.waiter.acquire()
        self.forks[0].acquire()
        self.forks[1].acquire()
        self.waiter.release()

        super().eat()

        self.forks[0].release()
        self.forks[1].release()