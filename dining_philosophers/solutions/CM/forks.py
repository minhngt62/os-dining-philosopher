import logging
from multiprocessing import Lock, Condition
import multiprocessing
from multiprocessing.managers import SyncManager

from ..._states import PhilosopherState, ForkState
from ...philosophers import logger
from .philosophers import CMPhilosopher


class CMFork:

    def __init__(
        self,
        id_: int,
        ):
        self.id_ = id_
        self.state = ForkState.DIRTY
        self.owner_id = None 
        self.lock = Lock()
        self.condition_lock = Condition()
    
    def request(self, philosopher_id):
        if self.owner_id == philosopher_id:
            self.lock.acquire()
            logger.info("Philosopher %d has the fork %d" % (self.owner_id, self.id_))
            self.state = ForkState.CLEAN
            self.lock.release()
        elif self.state is ForkState.DIRTY:
            self.lock.acquire()
            logger.info("Philosopher %d clean the fork %d and pass to philosopher %d" % (self.owner_id, self.id_, philosopher_id))
            self.state = ForkState.CLEAN
            self.owner_id = philosopher_id
            self.lock.release()
        elif self.state is ForkState.CLEAN:
            self.condition_lock.acquire()
            logger.info("Philosopher %d is waiting for the fork %d from philosopher %d" % (philosopher_id, self.id_, self.owner_id))
            self.condition_lock.wait()
            self.lock.acquire()
            logger.info("Philosopher %d clean the fork %d and pass to philosopher %d" % (self.owner_id, self.id_, philosopher_id))
            self.owner_id = philosopher_id
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

    def getOwner(self):
        return self.owner_id

    def setOwner(self, philosopher_id):
        self.owner_id = philosopher_id

SyncManager.register("CMFork", CMFork)