import tkinter as tk

from .gui import GUI
from ..solutions import *
from ..table import Table

class EventHandler:
    TABLES = [ArbitratorTable]

    def __init__(self, gui: GUI):
        self.gui = gui

    def method_selection(self):
        for btn in self.gui._btns:
            pass
    
    def _reset_kernel(self, table: Table):
        pass