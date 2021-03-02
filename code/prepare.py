from os.path import join as path_join

from code.sim import sim_log_parse
from code.helpers import find_indices_to_delete

import matplotlib.image as mpimg
import numpy as np
import csv
import cv2

def prepare_data(path_sim_log):

    file_names, steering_angles = parse_sim_log(path_sim_log, angle_correction)

