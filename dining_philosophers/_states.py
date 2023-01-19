from enum import Enum, auto

class ForkState(Enum):
    DIRTY = auto()
    CLEAN = auto()

class PhilosopherState(Enum):
    EATING = "I'm eating."
    HUNGRY = "I'm hungry."
    THINKING = "I'm thinking."