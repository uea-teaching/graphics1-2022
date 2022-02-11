"""
Plots for the transforms 01 lecture

Useful links:
Arcs : https://stackoverflow.com/a/54850819/10188737
"""

# %%

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc, FancyArrowPatch

from utils import *
set_style()


# %%

t1 = np.array([[13, 5], [16, 7], [18, 4]])
theta = np.pi / 9
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])
t2 = t1 @ R.T
radius = np.linalg.norm(t1[0])

fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-1, 20), y_range=(-1, 13))
point_label(ax, (0, 0))
plot_triangle(ax, t1, label_offsets=None, labels=False)

# %%


def cos_sin(ax, p, x='x', y='y'):
    ax.plot(p[0], p[1], 'ro', ms=5)
    ax.plot([0, p[0]], [p[1], p[1]], '--k', lw=1.2)
    ax.plot([p[0], p[0]], [0, p[1]], '--k', lw=1.2)
    ax.text(p[0], -0.5, x, ha='center', va='center', fontsize=12)
    ax.text(-0.5, p[1], y, ha='center', va='center', fontsize=12)
    ax.plot([0, p[0]], [0, p[1]], '-k', lw=1.2)


fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-1, 20), y_range=(-1, 13))
point_label(ax, (0, 0))
plot_triangle(ax, t1, label_offsets=None, labels=False)
cos_sin(ax, t1[0])

# %%

fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-1, 20), y_range=(-1, 13))
point_label(ax, (0, 0))
plot_triangle(ax, t1, label_offsets=None, labels=False)
cos_sin(ax, t1[0])

# %%


def angle_arrow(ax, p1=(6, 0), p2=(5, 2), r=0.2, text=r"$\theta$"):
    style = "Simple, tail_width=0.5, head_width=4, head_length=8"
    kw = dict(arrowstyle=style, color="k")
    a = FancyArrowPatch(p1, p2,
                        connectionstyle=f"arc3,rad={r}", **kw)
    ax.text(p1[0], (p1[1] + p2[1]) / 2, text,
            ha="left", va="bottom", fontsize=12)
    ax.add_patch(a)


fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-1, 20), y_range=(-1, 13))
point_label(ax, (0, 0))
plot_triangle(ax, t1, label_offsets=None, labels=False)
cos_sin(ax, t1[0])
angle_arrow(ax, p1=(6, 0), p2=(5, 2), r=0.2, text=r"$\beta$")

# %%

fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-1, 20), y_range=(-1, 13))
point_label(ax, (0, 0))
plot_triangle(ax, t1, label_offsets=None, labels=False)
cos_sin(ax, t1[0])
angle_arrow(ax, p1=(6, 0), p2=(5, 2), r=0.2, text=r"$\beta$")
c = Circle((0, 0), radius=radius, color='k', fill=False)
ax.add_patch(c)

# %%

fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-1, 20), y_range=(-1, 13))
point_label(ax, (0, 0))
plot_triangle(ax, t1, label_offsets=None, labels=False)
plot_triangle(ax, t2, label_offsets=None, labels=False)
cos_sin(ax, t1[0])
angle_arrow(ax, p1=(6, 0), p2=(5, 2), r=0.2, text=r"$\beta$")
c = Circle((0, 0), radius=radius, color='k', fill=False)
ax.add_patch(c)

# %%

fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-1, 20), y_range=(-1, 13))
point_label(ax, (0, 0))
plot_triangle(ax, t1, label_offsets=None, labels=False)
plot_triangle(ax, t2, label_offsets=None, labels=False)
cos_sin(ax, t1[0])
angle_arrow(ax, p1=(6, 0), p2=(5, 2), r=0.2, text=r"$\beta$")
cos_sin(ax, t2[0], "x'", "y'")
angle_arrow(ax, p1=(6, 2.2), p2=(5, 4.3), r=0.25, text=r"$\alpha$")

c = Circle((0, 0), radius=radius, color='k', fill=False)
ax.add_patch(c)
