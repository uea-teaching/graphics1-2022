"""
Plots for the transforms 01 lecture

Useful links:
Arcs : https://stackoverflow.com/a/54850819/10188737
"""

# %%

import numpy as np
import matplotlib.pyplot as plt

from utils import *
set_style()

# %%

t0 = np.array([[-5, -2], [0, 3], [5, 0]])
t0_offset = np.array([[-0.5, -0.75], [-1.5, 0.0], [-0.5, -0.75]])

fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-12, 12), y_range=(-8, 8))
plot_triangle(ax, t0, label_offsets=t0_offset)
fig.savefig("scaling_01.png")

# %%

s1 = np.array([[2, 0], [0, 2]])
t1 = (s1 @ t0.T).T

fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-12, 12), y_range=(-8, 8))
plot_triangle(ax, t0, label_offsets=t0_offset,
              facecolor=(0.5, 0.0, 0.5, 0.2))
plot_triangle(ax, t1, label_offsets=t0_offset)
fig.savefig("scaling_02.png")

# %%

s2 = np.array([[1, 0], [0, 2]])
t2 = (s2 @ t0.T).T

fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-12, 12), y_range=(-8, 8))
plot_triangle(ax, t0, label_offsets=t0_offset,
              facecolor=(0.5, 0.0, 0.5, 0.2))
plot_triangle(ax, t2, label_offsets=t0_offset)
fig.savefig("scaling_03.png")

# %%

s3 = np.array([[1, 2], [0, 1]])
t3 = (s3 @ t0.T).T

fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-12, 12), y_range=(-8, 8))
plot_triangle(ax, t0, label_offsets=t0_offset,
              facecolor=(0.5, 0.0, 0.5, 0.2))
plot_triangle(ax, t3, label_offsets=t0_offset)
fig.savefig("shear_x.png")

# %%

s4 = np.array([[1, 0], [1, 1]])
t4 = (s4 @ t0.T).T

fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-12, 12), y_range=(-8, 8))
plot_triangle(ax, t0, label_offsets=t0_offset,
              facecolor=(0.5, 0.0, 0.5, 0.2))
plot_triangle(ax, t4, label_offsets=t0_offset)
fig.savefig("shear_y.png")
