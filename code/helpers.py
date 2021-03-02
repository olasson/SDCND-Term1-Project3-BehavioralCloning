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


def find_indices_to_delete(dist, n_bins, flatten_factor):

    values, bins = np.histogram(dist, n_bins)
    max_number_of_angles = (np.mean(values) * flatten_factor).astype('uint32')

    indices_to_delete = []

    for i, bin_right in enumerate(bins[1:]):
        bin_left = bins[i]
        if i == (len(bins) - 2):
            bin_angles = np.where((dist >= bin_left) & (dist <= bin_right))
        else:
            bin_angles = np.where((dist >= bin_left) & (dist < bin_right))
        if (len(bin_angles[0]) > max_number_of_angles):
            n_deletes = len(bin_angles[0]) - max_number_of_angles
            delete_index = np.random.choice(bin_angles[0], size = n_deletes, replace = False)
            indices_to_delete.extend(delete_index)

    indices_to_delete = np.array(indices_to_delete)

    return indices_to_delete