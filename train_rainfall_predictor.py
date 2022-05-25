__author__ = "konwar.m"
__copyright__ = "Copyright 2022, AI R&D"
__credits__ = ["konwar.m"]
__license__ = "Individual Ownership"
__version__ = "1.0.1"
__maintainer__ = "konwar.m"
__email__ = "rickykonwar@gmail.com"
__status__ = "Development"

from rainfall_prediction.preprocessing.preprocess_ts import PreprocessTS
from rainfall_prediction.utility_scripts.utility import read_config

if __name__ == '__main__':
    preprocessing_config = read_config(input_config_path=r'rainfall_prediction\config\ts_config.yaml')['preprocessing_parameters']
    training_config = read_config(input_config_path=r'rainfall_prediction\config\ts_config.yaml')['training_parameters']

    preprocessing_instance = PreprocessTS(
                                    library_utilized=preprocessing_config['library_utilized'],
                                    input_file_path=preprocessing_config['input_file_path'],
                                    date_column=preprocessing_config['date_column'],
                                    params=preprocessing_config['params']
                                )
    preprocessing_instance._read_data()
    preprocessing_instance._subprocess_instance.perform_preprocessing()