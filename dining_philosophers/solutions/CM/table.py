from typing import List, Tuple, Dict, Any
import multiprocessing

from ...table import Table
from .forks import CMFork
from ...philosophers import Philosopher, logger
from .philosophers import CMPhilosopher

class CMTable(Table):

    def _serve_forks(self):
        return [self.manager.CMFork(i) for i in range(self.PHILOSOPHERS_ON_TABLE)]

    def _invite_philosophers(self, forks):
        philosophers = []

        for philosopher_number in range(self.PHILOSOPHERS_ON_TABLE):
            neighbor_forks = (
                forks[philosopher_number % self.PHILOSOPHERS_ON_TABLE],
                forks[(philosopher_number + 1) % self.PHILOSOPHERS_ON_TABLE]
            )
            philosopher = CMPhilosopher(philosopher_number, neighbor_forks)

            # Giving ownership to forks if no one is the owner
            for fork in neighbor_forks:
                if fork.getOwner() is None:
                    fork.setOwner(philosopher.id_)
            philosophers.append(philosopher)

        return philosophers
