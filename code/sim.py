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
