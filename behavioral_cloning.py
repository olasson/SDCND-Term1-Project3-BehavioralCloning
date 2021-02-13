from code.sim import sim_log_parse, sim_find_indices_to_delete
from code.show import show_distribution


import numpy as np
import argparse



def main():

    # ---------- Command line arguments ---------- #

    parser = argparse.ArgumentParser(description = 'Traffic Sign Classifier')

    parser.add_argument(
        '--data_sim_log',
        type = str,
        nargs = '?',
        default = '',
        help = 'Path to the driving_log.csv from the Udacity simulator.'
    )
    parser.add_argument(
        '--data_train',
        type = str,
        nargs = '?',
        default = '',
        help = 'Path to a pickled (.p) training set.'
    )

    parser.add_argument(
        '--data_valid',
        type = str,
        nargs = '?',
        default = '',
        help = 'Path to a pickled (.p) validation set.'
    )

    parser.add_argument(
        '--data_test',
        type = str,
        nargs = '?',
        default = '',
        help = 'Path to a pickled (.p) testing set.'
    )

    parser.add_argument(
        '--show_dist',
        action = 'store_true',
        help = 'Show angle distribution.'
    )


    parser.add_argument(
        '--angle_corr',
        type = float,
        nargs = '?',
        default = 0.15,
        help = 'Angle correction applied to images from right and left camera'
    )


    parser.add_argument(
        '--angle_flatten',
        type = float,
        nargs = '?',
        default = 2.5,
        help = 'Flattening factor applied to angle distribution. Higher, more flat. Lower, less flat.'
    )

    args = parser.parse_args()

    # Unpack arguments

    data_sim_log = args.data_sim_log

    angle_correction = args.angle_corr
    angle_flatten = args.angle_flatten

    show_dist = args.show_dist



    # ---------- Load data ---------- #

    if data_sim_log:
        file_names, steering_angles = sim_log_parse(data_sim_log, angle_correction)
        print(len(file_names), "Files loaded!")
        print(len(steering_angles), "Angles loaded!")


        # Show data
        if show_dist:
            if angle_flatten != 1.0:
                indices_to_delete = sim_find_indices_to_delete(steering_angles, 'auto', angle_flatten)
                steering_angles = np.delete(steering_angles, indices_to_delete)
            title = ("Angle distribution | " + str(angle_correction) + " angle correction | " + 
                     str(angle_flatten) + " flattening factor.")
            show_distribution(steering_angles, title = title)




main()