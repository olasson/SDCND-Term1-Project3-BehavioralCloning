from os import listdir, mkdir
from os.path import exists as file_exists
from os.path import isdir as folder_exists
from os.path import join as path_join

import numpy as np

def folder_is_empty(path):

    """
    Check if a folder is empty
    
    Inputs
    ----------
    path: string
        Full path to a keras model
        
    Outputs
    -------
    result: bool
        True if folder is empty, false otherwise
    """

    result = True

    if folder_exists(path):
        result = (len(listdir(path)) == 0)
    
    return result

def folder_number_of_elements(path):
    return len(listdir(path))