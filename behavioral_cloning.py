from code.sim import sim_log_parse
from code.show import show_distribution


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

    args = parser.parse_args()

    # Unpack arguments

    data_sim_log = args.data_sim_log
    angle_correction = args.angle_corr

    show_dist = args.show_dist




    # Load data

    if data_sim_log:
        file_names, steering_angles = sim_log_parse(data_sim_log, angle_correction)
        print(len(file_names), "Files loaded!")
        print(len(steering_angles), "Angles loaded!")



    # Show data
    if show_dist and data_sim_log:
        title = "Angle distribution with " + str(angle_correction) + " angle correction"
        show_distribution(steering_angles, title = title)




main()