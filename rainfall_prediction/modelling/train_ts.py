__author__ = "konwar.m"
__copyright__ = "Copyright 2022, AI R&D"
__credits__ = ["konwar.m"]
__license__ = "Individual Ownership"
__version__ = "1.0.1"
__maintainer__ = "konwar.m"
__email__ = "rickykonwar@gmail.com"
__status__ = "Development"

from rainfall_prediction.utility_scripts import read_input_data

class TrainTS:
    def __init__(self, **kwargs):
        self._library_utilized = kwargs.get('library_utilized') if 'library_utilized' in kwargs.keys() else 'darts'

        if self._library_utilized.__eq__('darts'):
            self._subprocess_instance = TrainDarts(self)

class TrainDarts():
    def __init__(self, base):
        self._base = base