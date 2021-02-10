from code.sim import sim_log_parse


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
        '--show',
        default = None,
        type = str,
        nargs = '*',
        choices = ['images', 'dist', 'pred'],
        help = 'Visualize images, distributions or model predictions.'
    )

    args = parser.parse_args()

    # Unpack arguments

    data_sim_log = args.data_sim_log




    # Load data

    if data_sim_log:
        file_names, steering_angles = sim_log_parse(data_sim_log, 0.0)
        print(len(file_names), "Files loaded!")
        print(len(steering_angles), "Angles loaded!")




main()