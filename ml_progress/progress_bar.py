import sys

from .display import Display

class ProgressBar(Display):
    def __init__(self, numerator: str, denominator: str):
        super().__init__()
        self.numerator = numerator
        self.denominator = denominator

    def update(self, metrics: dict, width=25, height=1):
        progress: float = self.get_progress(metrics)
        width: int = width - 7 # make room for constant outputs (e.g. |)
        solid: str = u"\u2588"*int(progress*width)
        empty: str = " "*(width-int(progress*width))
        sys.stdout.write("%3d%% " % (int(progress*100)))
        for line in range(height):
            if line > 0:
                sys.stdout.write("     ")
            sys.stdout.write("|%s%s|\n" % (solid, empty))

    def get_progress(self, metrics: dict) -> float:
        return metrics[self.numerator] / metrics[self.denominator]