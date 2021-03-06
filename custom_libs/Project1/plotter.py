import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    synth_tr: np.ndarray
    synth_te: np.ndarray
    pima_tr: np.ndarray
    pima_te: np.ndarray

    def __init__(self, synth_tr: np.ndarray, synth_te: np.ndarray, pima_tr: np.ndarray,
                 pima_te: np.ndarray):
        self.synth_tr = synth_tr
        self.synth_te = synth_te
        self.pima_tr = pima_tr
        self.pima_te = pima_te

    def plot_dataset(self):
        fig, ax = plt.subplots(1, 3, figsize=(11, 4))
        plot_color = 'dodgerblue'
        # synth_tr f1-f2 Scatter Plot
        ax[0].scatter(self.synth_tr[:, 0][self.synth_tr[:, -1] == 0],
                      self.synth_tr[:, 1][self.synth_tr[:, -1] == 0],
                      color='royalblue', s=12, marker='o', label="Class 0")
        ax[0].scatter(self.synth_tr[:, 0][self.synth_tr[:, -1] == 1],
                      self.synth_tr[:, 1][self.synth_tr[:, -1] == 1],
                      color='red', s=12, marker='o', label="Class 1")
        ax[0].margins(0.1)  # 1% padding in all directions
        ax[0].set_title("Synth Dataset Scatter Plot")
        ax[0].set_xlabel("Feature 1")
        ax[0].set_ylabel("Feature 2")
        ax[0].legend()
        ax[0].grid(True)
        # f1 Hist
        hist, bins, patches = ax[1].hist(self.synth_tr[:, 0], density=True, bins=20, color=plot_color,
                                         edgecolor='black',
                                         linewidth=0.5)  # density=False would make counts
        ax[1].set_title("Synth Dataset Density Histogram")
        ax[1].set_xlabel("Feature 1")
        ax[1].set_ylabel("Density")
        ax[1].margins(0.1)  # 1% padding in all directions
        # f2 Hist
        hist, bins, patches = ax[2].hist(self.synth_tr[:, 1], density=True, bins=20, color=plot_color,
                                         edgecolor='black',
                                         linewidth=0.5)  # density=False would make counts
        ax[2].set_title("Synth Dataset Density Histogram")
        ax[2].set_xlabel("Feature 2")
        ax[2].set_ylabel("Density")
        ax[2].margins(0.1)  # 1% padding in all directions
        fig.tight_layout()
        fig.show()
