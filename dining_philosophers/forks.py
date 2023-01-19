import logging
import threading
from typing import List, Dict, Tuple, Any

from ._states import ForkState

class Fork(threading.Semaphore):
    def __init__(
        self,
        id: int,
        state: ForkState = ForkState.DIRTY,
        ):
        threading.Semaphore.__init__(self)

        self.id = id
        self.state = state