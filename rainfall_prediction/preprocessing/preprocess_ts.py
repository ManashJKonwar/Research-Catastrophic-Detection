__author__ = "konwar.m"
__copyright__ = "Copyright 2022, AI R&D"
__credits__ = ["konwar.m"]
__license__ = "Individual Ownership"
__version__ = "1.0.1"
__maintainer__ = "konwar.m"
__email__ = "rickykonwar@gmail.com"
__status__ = "Development"

from rainfall_prediction.utility_scripts.utility import read_input_data

class PreprocessTS:
    def __init__(self, **kwargs):
        self._library_utilized = kwargs.get('library_utilized') if 'library_utilized' in kwargs.keys() else 'darts'
        self._input_file_path = kwargs.get('input_file_path')
        self._date_column = kwargs.get('date_column')
        self._preprocessed_data = None
        
        if self._library_utilized.__eq__('darts'):
            self._subprocess_instance = PreprocessDarts(self)

    def _read_data(self):
        self._input_data = read_input_data(self._input_file_path, parse_dates=[self._date_column])

class PreprocessDarts():
    def __init__(self, base):
        self._base = base

    def perform_preprocessing(self):
        pass