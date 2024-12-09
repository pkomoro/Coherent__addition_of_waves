# Class for visualisation of results

import numpy as np
import os
from pathlib import Path
from matplotlib import pyplot as plt

class Plotter:
    def __init__(self, image):
        self.image = image
                

    def save_output_amplitude(self, path):
        self._prepare_path_to_save(path)
        pass

    def save_output_phase(self, path):
        self._prepare_path_to_save(path)
        pass

    def show(self):
        plt.show()

    def _prepare_path_to_save(self, path):
        dirs = os.path.dirname(path)
        Path(dirs).mkdir(parents=True, exist_ok=True)