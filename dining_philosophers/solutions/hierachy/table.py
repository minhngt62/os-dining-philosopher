from ...table import Table
from ...forks import Fork
from .philosophers import HierachyPhilosopher
from typing import List, Tuple, Dict, Any


class HierachyTable(Table):
    def __init__(self):
        super().__init__()

    def _serve_forks(self) -> List[Fork]:
        return [self.manager.Fork(i) for i in range(self.PHILOSOPHERS_ON_TABLE)]

    def _invite_philosophers(
        self,
        forks: List[Fork],
        ) -> List[HierachyPhilosopher]:
        philosophers = []
        for id in range(self.PHILOSOPHERS_ON_TABLE):
            neighbor_forks = (
                forks[id % self.PHILOSOPHERS_ON_TABLE],
                forks[(id + 1) % self.PHILOSOPHERS_ON_TABLE]
            )
            philosopher = HierachyPhilosopher(id, neighbor_forks, self.PHILOSOPHERS_ON_TABLE)
            philosophers.append(philosopher)

        return philosophers
