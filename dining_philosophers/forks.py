import logging
from threading import Semaphore
from typing import List, Dict, Tuple, Any
from multiprocessing.managers import SyncManager

from ._states import ForkState
from .utils import AcquirerProxy

class Fork(Semaphore):
    def __init__(
        self,
        id_: int,
        state: ForkState = ForkState.DIRTY,
        ):
        Semaphore.__init__(self)

        self.id_ = id_
        self.state = state

# if you inherit Fork, please register your custom Fork!
SyncManager.register("Fork", Fork, AcquirerProxy)