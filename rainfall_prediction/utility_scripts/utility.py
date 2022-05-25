__author__ = "konwar.m"
__copyright__ = "Copyright 2022, AI R&D"
__credits__ = ["konwar.m"]
__license__ = "Individual Ownership"
__version__ = "1.0.1"
__maintainer__ = "konwar.m"
__email__ = "rickykonwar@gmail.com"
__status__ = "Development"

import os
import yaml
import json
import pandas as pd

# region Generic functions
def read_config(input_config_path=None):
    if input_config_path is not None and os.path.exists(input_config_path):
        file_name = os.path.basename(input_config_path)
        file_type = os.path.splitext(file_name)[1]
        try:
            if file_type.__eq__('.yaml'):
                with open(input_config_path, "r") as stream:
                    try:
                        return yaml.safe_load(stream)
                    except yaml.YAMLError as exc:
                        print(exc)
            
            elif file_type.__eq__('.json'):
                with open(input_config_path, "r") as f:
                    try:
                        return json.load(f)
                    except json.decoder.JSONDecodeError as exc:
                        print(exc)
        except Exception as ex:
            print('Caught Exception while reading configuration file: %s' %(str(ex)))

def read_input_data(input_file_path=None, **kwargs):
    parse_dates = kwargs.get('parse_dates') if 'parse_dates' in kwargs.keys() else None

    if input_file_path is not None and os.path.exists(input_file_path):
        filename = os.path.basename(input_file_path)
        extension = os.path.splitext(filename)[1]
        try:
            if extension.__eq__('.csv'):
                if parse_dates is None:
                    return pd.read_csv(input_file_path)
                else:
                    return pd.read_csv(input_file_path, parse_dates=parse_dates)
        except Exception as ex:
            print('Caught Exception while reading input file: %s' %(str(ex)))
#endregion