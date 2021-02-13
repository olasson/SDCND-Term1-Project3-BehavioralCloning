import matplotlib.pyplot as plt
import numpy as np


def show_distribution(data, title = None, bins = 'auto', save_path = None, fig_size = (15, 6)):

    fig = plt.figure(figsize = fig_size)

    plt.hist(data, bins = bins)
    plt.title(title, fontsize = 20)
    fig.text(0.9, 0.9, '{} samples'.format(len(data)),
            verticalalignment='top', 
            horizontalalignment='center',
            color = 'black', fontsize = 12)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()