from typing import List, Tuple, Dict, Any

from ..._states import PhilosopherState
from ...philosophers import Philosopher
from ...forks import Fork
from ...utils import logger

class HierachyPhilosopher(Philosopher):
    def __init__(
        self,
        id: int,
        state,
        forks: Tuple[Fork, Fork],
        n_philosophers: int,
        ):
        super().__init__(id, state, forks)
        self.n_philosopher = n_philosophers

    def eat(self):
        self.state.value = PhilosopherState.HUNGRY
        logger.info("{:<13}".format(str(self)) + f" {self.state.value.value}")

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
        return (self.id_ + 1) != self.n_philosopher
