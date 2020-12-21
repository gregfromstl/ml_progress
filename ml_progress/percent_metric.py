import sys

from .display import Display

class PercentMetric(Display):
    def __init__(self, metric: str):
        super().__init__()
        self.metric = metric

    def update(self, metrics: dict, width=25, height=1):
        sys.stdout.write("%s: %3d%% \n" % (self.metric, metrics[self.metric]))