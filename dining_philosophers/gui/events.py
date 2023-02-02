import tkinter as tk
import time
from multiprocessing import Process

from .gui import GUI, rel
from ..solutions import *
from ..table import Table
from .._states import PhilosopherState

class EventHandler:
    TABLES = [ArbitratorTable, CMTable, HierachyTable, LimitTable]
    STATE_IMG = {
        PhilosopherState.THINKING: tk.PhotoImage(file=rel("philosopher_thinking.png")),
        PhilosopherState.EATING: tk.PhotoImage(file=rel("philosopher_eating.png")),
        PhilosopherState.HUNGRY: tk.PhotoImage(file=rel("philosopher_hungry.png")),
        "default": tk.PhotoImage(file=rel("philosopher.png"))
    }

    def __init__(self, gui: GUI):
        self.gui = gui
        self.kernel: Table = ArbitratorTable(self)

    def btn_select_method(self):
        for i in range(len(self.TABLES)):
            self.gui._btns[i].bind("<Button-1>", lambda e: self._reset_kernel(self.TABLES[i]))
    
    def btn_start(self):
        self.gui._btn_start.bind("<Button-1>", lambda e: self._start_dining())

    def _reset_kernel(self, table: Table):
        self.gui._canvas.delete("All")
        self.kernel = table(self)
        self.gui.default_build()

    def _start_dining(self):
        self.kernel.start_dining()

    def _animate_dining(self, dining_table: Table):
        stop = False
        while not stop:
            all_alive = False
            for philosopher in dining_table._philosophers:
                cur_state = philosopher.is_alive()
                if cur_state:
                    self.gui._canvas.itemconfig(
                        self.gui._philosophers[philosopher.id_], 
                        image=self.STATE_IMG[philosopher.state.value]
                    )
                else:
                    self.gui._canvas.itemconfig(
                        self.gui._philosophers[philosopher.id_], 
                        image=self.STATE_IMG["default"]
                    )
                self.gui.window.update()
                all_alive = all_alive or cur_state
            stop = stop or not all_alive

                
                
                    


