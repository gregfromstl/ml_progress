from threading import Thread

from .dashboard import Dashboard

class Progress():
    def __init__(self, metrics={}, displays={}):
        super().__init__()

        self.metrics = metrics
        self.displays = displays

        self.dashboard = Dashboard(self)
        self.thread = Thread(target=self.dashboard.start)
    
    def start(self):
        self.dashboard.show = True
        self.thread.start()
    
    def stop(self):
        self.dashboard.show = False
        self.thread.join()
