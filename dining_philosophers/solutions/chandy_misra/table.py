from typing import List, Tuple, Dict, Any
import multiprocessing

from ...table import Table
from .forks import CMFork
from ...philosophers import Philosopher
from .philosophers import CMPhilosopher

class CMTable(Table):
    def __init__(self, event):
        super().__init__(event)

    def _serve_forks(self) -> List[CMFork]:
        return [self.manager.CMFork(i) for i in range(self.PHILOSOPHERS_ON_TABLE)]

    def _invite_philosophers(self, states, forks: List[CMFork]):
        philosophers = []

        for philosopher_number in range(self.PHILOSOPHERS_ON_TABLE):
            neighbor_forks = (
                forks[philosopher_number % self.PHILOSOPHERS_ON_TABLE],
                forks[(philosopher_number + 1) % self.PHILOSOPHERS_ON_TABLE]
            )
            philosopher = CMPhilosopher(philosopher_number, states[philosopher_number], neighbor_forks)

            # Giving ownership to forks if no one is the owner
            for fork in neighbor_forks:
                if fork.get_owner_id() is None:
                    fork.set_owner_id(philosopher.id_)
            philosophers.append(philosopher)

        return philosophers
