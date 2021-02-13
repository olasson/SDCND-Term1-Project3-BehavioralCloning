#from code.helpers import folder_number_of_elements

import numpy as np
import csv
import cv2


def sim_log_parse(path_sim_log, angle_correction):

    file_names = []
    steering_angles = []

    with open(path_sim_log) as csv_file:
        sim_log = csv.reader(csv_file)

        for line in sim_log:
            # Append images from the three different cams
            file_names.extend([line[0], # Center
                               line[1], # Left
                               line[2]]) # Right

            # Append the steering angle once for each cam
            steering_angles.extend([float(line[3]), # Center 
                                    float(line[3]) + angle_correction, # Left
                                    float(line[3]) - angle_correction]) # Right

    file_names = np.array(file_names)
    steering_angles = np.array(steering_angles)

    return file_names, steering_angles


def sim_find_indices_to_delete(steering_angles, n_bins, flatten_factor):

    values, bins = np.histogram(steering_angles, n_bins)
    max_number_of_angles = (np.mean(values) * flatten_factor).astype('uint32')

    indices_to_delete = []

    for i, bin_right in enumerate(bins[1:]):
        bin_left = bins[i]
        if i == (len(bins) - 2):
            bin_angles = np.where((steering_angles >= bin_left) & (steering_angles <= bin_right))
        else:
            bin_angles = np.where((steering_angles >= bin_left) & (steering_angles < bin_right))
        if (len(bin_angles[0]) > max_number_of_angles):
            n_deletes = len(bin_angles[0]) - max_number_of_angles
            delete_index = np.random.choice(bin_angles[0], size = n_deletes, replace = False)
            indices_to_delete.extend(delete_index)

    indices_to_delete = np.array(indices_to_delete)

    return indices_to_delete