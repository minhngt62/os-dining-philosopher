from typing import List, Tuple, Dict, Any
from multiprocessing.synchronize import Semaphore



from ...table import Table
from ...forks import Fork
from .philosophers import LimitPhilosopher
from ...utils import AcquirerProxy

class LimitDiners(Table):
    def __init__(self):
        super().__init__()

    def _serve_forks(self):
        return [self.manager.Fork(i) for i in range(self.PHILOSOPHERS_ON_TABLE)]

    def _invite_philosophers(self, forks):
        philosophers = []
        waiter_to_sit = self.manager.Semaphore(4)
        for id_ in range(self.PHILOSOPHERS_ON_TABLE):
            neighbor_forks = (
                forks[id_ % self.PHILOSOPHERS_ON_TABLE],
                forks[(id_ + 1) % self.PHILOSOPHERS_ON_TABLE]
            )
            philosopher = LimitPhilosopher(id_, neighbor_forks, waiter_to_sit)
            philosophers.append(philosopher)
        
        return philosophers
    