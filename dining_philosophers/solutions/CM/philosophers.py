from typing import List, Dict, Tuple, Any

from ..._states import PhilosopherState
from ...philosophers import Philosopher, logger
from ...forks import Fork

class CMPhilosopher(Philosopher):
    def __init__(
        self, 
        id_: int,
        forks: Tuple[Fork, Fork]):
        super().__init__(id_, forks)
    
    def eat(self):
        for fork in self.forks:
            fork.request(self.id_)

        super().eat()
        logger.info("Philosopher %d finish eating" % (self.id_))
        for fork in self.forks:
            fork.finish()