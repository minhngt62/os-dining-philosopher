from typing import List, Dict, Tuple, Any
from abc import ABC, abstractmethod

from .forks import Fork
from .philosophers import Philosopher, logger

class Table(ABC):
    '''
    Prepare the philosophers and the forks on the table.
    '''
    PHILOSOPHERS_ON_TABLE: int = 5

    def start_dining(self):
        logger.info(
            f'Starting the dinner with {self.PHILOSOPHERS_ON_TABLE:02} philosophers'
        )
        forks = self._serve_forks()
        philosophers = self._invite_philosophers(forks)
        for philosopher in philosophers:
            philosopher.start()

    @abstractmethod
    def _serve_forks(self) -> List[Fork]:
        '''
        Invoke forks and return a list of them (<= PHILOSOPHERS_ON_TABLE).
        '''
        pass
    
    @abstractmethod
    def _invite_philosophers(
        self, 
        forks: List[Fork],
        ) -> List[Philosopher]:
        '''
        Invoke philosophers (<= PHILOSOPHERS_ON_TABLE).
        Assign each fork to the corresponding philosophers.
        Assign more sermaphores (if needed).
        Return a list of philosophers.
        '''
        pass
        
