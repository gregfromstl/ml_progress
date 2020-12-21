import time
import shutil
import os

from .progress_bar import ProgressBar
from .util import clear

class Dashboard():
    def __init__(self, progress):
        super().__init__()

        self.show = False
        self.metrics = progress.metrics
        self.displays = progress.displays
    
    def update(self):
        columns, lines = shutil.get_terminal_size((80, 20))
        clear()
        for display in self.displays:
            display.update(self.metrics, width=columns)
            
    def start(self):
        while self.show:
            self.update()
            time.sleep(0.25)
