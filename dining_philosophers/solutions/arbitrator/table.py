from typing import List, Tuple, Dict, Any
import threading

from ...table import Table
from ...forks import Fork
from .philosophers import ArbitratorPhilosopher

class ArbitratorTable(Table):
    def _serve_forks(self):
        return [Fork(i) for i in range(self.PHILOSOPHERS_ON_TABLE)]

    def _invite_philosophers(self, forks: List[Fork]):
        philosophers = []
        waiter = threading.Semaphore()
        for id in range(self.PHILOSOPHERS_ON_TABLE):
            neighbor_forks = (
                forks[id % self.PHILOSOPHERS_ON_TABLE],
                forks[(id + 1) % self.PHILOSOPHERS_ON_TABLE]
            )
            philosopher = ArbitratorPhilosopher(id, neighbor_forks, waiter)
            philosophers.append(philosopher)
        
        return philosophers