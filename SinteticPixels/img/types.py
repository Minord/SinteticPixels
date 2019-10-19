"""
This module is for declare dictionaries with the image type information.

common expresion
"""

import numpy as np

common_valid_dtypes = (np.float32, np.float64, np.int8, np.int32, np.int64)
common_int_valid_dtypes = (np.int8, np.int32, np.int64)

gray_image = {  
    'type_name': 'gray_scale',
    'valid_shapes': (1,),
    'valid_dtypes': common_valid_dtypes,
    'alpha': True
}

rgb_image = {
    'type_name': 'rgb',
    'valid_shapes': (3,),
    'valid_dtypes': common_valid_dtypes,
    'alpha': True
}

binary_image = {
    'type_name': 'binary',
    'valid_shapes': (1,),
    'valid_dtypes': (np.bool,),
    'alpha': False
}

indexed_image = {
    'type_name': 'indexed',
    'valid_shapes': (1,),
    'valid_dtypes': (common_int_valid_dtypes,),
    'alpha': False
}