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


main()