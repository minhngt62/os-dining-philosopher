from ...table import Table
from ...forks import Fork
from .philosophers import HierachyPhilosopher
from typing import List, Tuple, Dict, Any
import threading


class HierachyTable(Table):
    def _serve_forks(self) -> List[Fork]:
        return [Fork(i) for i in range(self.PHILOSOPHERS_ON_TABLE)]

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
            philosopher = HierachyPhilosopher(id, neighbor_forks)
            philosophers.append(philosopher)

        return philosophers
