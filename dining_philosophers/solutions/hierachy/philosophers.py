from typing import List, Tuple, Dict, Any

from ..._states import PhilosopherState
from ...philosophers import Philosopher, logger
from ...forks import Fork

class HierachyPhilosopher(Philosopher):
    def __init__(self,
                 id:int,
                 forks: Tuple[Fork, Fork],
                 numPhilo: int,
                 ):
        super().__init__(id, forks)
        self.numPhilosopher = numPhilo

    def eat(self):
        self.state = PhilosopherState.HUNGRY
        logger.info("{:<13}".format(str(self)) + f" {self.state.value}")

        if self.left_fork_first():
            self.forks[0].acquire()
            self.forks[1].acquire()
        else:
            self.forks[1].acquire()
            self.forks[0].acquire()

        super().eat()

        self.forks[0].release()
        self.forks[1].release()

    def left_fork_first(self):
        return (self.id_ + 1) != self.numPhilosopher
