import tkinter as tk
import time

from .gui import GUI
from ..solutions import *
from ..table import Table
from .._states import PhilosopherState

class EventHandler:
    TABLES = [ArbitratorTable]
    PHILO_STATE_COLOR = {
        PhilosopherState.THINKING: "#FFC300",
        PhilosopherState.EATING: "#B7AC44",
        PhilosopherState.HUNGRY: "#EE4537"
        }

    def __init__(self, gui: GUI):
        self.gui = gui
        self.kernel: Table = ArbitratorTable()

    def btn_select_method(self):
        for i in range(len(self.TABLES)):
            self.gui._btns[i].bind("<Button-1>", lambda e: self._reset_kernel(self.TABLES[i]))
    
    def btn_start(self):
        pass

    def _reset_kernel(self, table: Table):
        self.gui._canvas.delete("All")
        self.kernel = table
        self.gui.default_build()

    def _start_dining(self):
        dining_table = ArbitratorTable()
        dining_table.start_dining()

        self._animate_dining(dining_table)

    def _animate_dining(self, dining_table: Table):
        while True:
            for philosopher in dining_table._philosophers:
                self.PHILO_STATE_COLOR[philosopher.state]


