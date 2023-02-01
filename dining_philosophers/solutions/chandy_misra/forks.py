import logging
from multiprocessing import Lock, Condition
from threading import Semaphore
import multiprocessing
from multiprocessing.managers import SyncManager
from typing import Optional

from ..._states import PhilosopherState, ForkState
from ...utils import logger
from .philosophers import CMPhilosopher
from ...forks import Fork


class CMFork(Fork):
    def __init__(
        self,
        id_: int,
        state: ForkState = ForkState.DIRTY,
        ):
        super().__init__(id_, state)
        
        self._owner_id: Optional[int] = None
        self.lock = Lock()
        self.condition_lock = Condition()
    
    def get_owner_id(self):
        return self._owner_id

    def set_owner_id(self, owner_id: CMPhilosopher):
        self._owner_id = owner_id
    
    def request(self, philosopher_id: int):
        if self._owner_id == philosopher_id:
            self.lock.acquire()
            logger.info("{:<13}".format(f"[PHILOSOPHER {self._owner_id:02}]") + " has " + str(self))
            self.state = ForkState.CLEAN
            self.lock.release()
        
        elif self.state is ForkState.DIRTY:
            self.lock.acquire()
            logger.info("%s clean %s and pass to %s" % ("{:<13}".format(f"[PHILOSOPHER {self._owner_id:02}]"), str(self), f"[PHILOSOPHER {philosopher_id:02}]"))
            self.state = ForkState.CLEAN
            self._owner_id = philosopher_id
            self.lock.release()
        
        elif self.state is ForkState.CLEAN:
            self.condition_lock.acquire()
            logger.info("%s waiting for %s from %s" % ("{:<13}".format(f"[PHILOSOPHER {philosopher_id:02}]"), str(self), f"[PHILOSOPHER {self._owner_id:02}]"))
            self.condition_lock.wait()
            self.lock.acquire()
            logger.info("%s clean %s and pass to %s" % ("{:<13}".format(f"[PHILOSOPHER {self._owner_id:02}]"), str(self), f"[PHILOSOPHER {philosopher_id:02}]"))
            self._owner_id = philosopher_id
            self.state = ForkState.CLEAN
            self.lock.release()
            self.condition_lock.release()

    def finish(self):
        self.lock.acquire()
        self.state = ForkState.DIRTY
        self.lock.release()
        self.condition_lock.acquire()
        self.condition_lock.notify_all()
        self.condition_lock.release()
    
    def __repr__(self) -> str:
        return f'[FORK {self.id_:02}]'

SyncManager.register("CMFork", CMFork)