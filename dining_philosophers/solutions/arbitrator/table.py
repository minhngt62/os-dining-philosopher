from typing import List, Tuple, Dict, Any
from multiprocessing.synchronize import Semaphore

from ...table import Table
from ...forks import Fork
from .philosophers import ArbitratorPhilosopher
from ...utils import AcquirerProxy

class ArbitratorTable(Table):
    def __init__(self, event):
        super().__init__(event)

    def _serve_forks(self):
        return [self.manager.Fork(i) for i in range(self.PHILOSOPHERS_ON_TABLE)]

    def _invite_philosophers(self, states, forks):
        philosophers = []
        waiter = self.manager.Semaphore()
        for id_ in range(self.PHILOSOPHERS_ON_TABLE):
            neighbor_forks = (
                forks[id_ % self.PHILOSOPHERS_ON_TABLE],
                forks[(id_ + 1) % self.PHILOSOPHERS_ON_TABLE]
            )
            philosopher = ArbitratorPhilosopher(id_, states[id_], neighbor_forks, waiter)
            philosophers.append(philosopher)
        
        return philosophers