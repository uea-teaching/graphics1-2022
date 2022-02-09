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

# plot the coordinate system

fig, ax = plt.subplots(1, 1)
set_spines(ax)
point_label(ax, (0, 0))
fig.savefig("coordinates_2D.png")


# %%

t1 = np.array([[-5, -2], [0, 3], [5, 0]])
t1_offset = np.array([[-0.5, -0.75], [-1.5, 0.0], [-0.5, -0.75]])

fig, ax = plt.subplots(1, 1)
set_spines(ax)
plot_triangle(ax, t1, label_offsets=t1_offset)
fig.savefig("triangle_01_translate_00.png")

# %%

t = np.array([9, 5])
fig, ax = plt.subplots(1, 1)
set_spines(ax)
plot_triangle(ax, t1, label_offsets=t1_offset)
plot_vector(ax, t, color='g')
fig.savefig("triangle_01_translate_01.png")

# %%

fig, ax = plt.subplots(1, 1)
set_spines(ax)
plot_triangle(ax, t1, label_offsets=t1_offset,
              facecolor=(0.5, 0.0, 0.5, 0.2),
              labels=True)
for c, ofs in zip(t1, [(-0.25, 0.5), None, None]):
    plot_vector(ax, c + t, c, color='g', label_offset=ofs)
fig.savefig("triangle_01_translate_02.png")

# %%

t2 = t1 + t
fig, ax = plt.subplots(1, 1)
set_spines(ax)
plot_triangle(ax, t1, label_offsets=t1_offset,
              facecolor=(0.5, 0.0, 0.5, 0.2),
              labels=True)
plot_triangle(ax, t2, label_offsets=t1_offset,
              facecolor=(0.5, 0.0, 0.5, 0.5),
              labels=True)
for c, ofs in zip(t1, [(-0.25, 0.5), None, None]):
    plot_vector(ax, c + t, c, color='g', label_offset=ofs, label=False)
fig.savefig("triangle_01_translate_03.png")

# %%

fig, ax = plt.subplots(1, 1)
set_spines(ax)
plot_triangle(ax, t2, label_offsets=t1_offset,
              facecolor=(0.5, 0.0, 0.5, 0.5),
              labels=True)
fig.savefig("triangle_01_translate_04.png")
