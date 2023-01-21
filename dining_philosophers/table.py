from typing import List, Dict, Tuple, Any
from abc import ABC, abstractmethod
import multiprocessing

from .forks import Fork
from .philosophers import Philosopher, logger

class Table(ABC):
    '''
    Prepare the philosophers and the forks on the table.
    '''
    PHILOSOPHERS_ON_TABLE: int = 5

    def __init__(self):
        self.manager = multiprocessing.Manager()

    def start_dining(self):
        with self.manager:
            logger.info(
                f'Starting the dinner with {self.PHILOSOPHERS_ON_TABLE:02} philosophers'
            )
            forks = self._serve_forks()
            self._philosophers = self._invite_philosophers(forks)
            
            for philosopher in self._philosophers:
                philosopher.start()
            for philosopher in self._philosophers:
                philosopher.join() 

    @abstractmethod
    def _serve_forks(self) -> List[Fork]:
        '''
        If inheriting Fork, please register yours first (REF: forks.py).
        Invoke forks (THROUGH self.manager - REF: arbitrator/table.py).
        Return a list of them (<= PHILOSOPHERS_ON_TABLE).
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
        
