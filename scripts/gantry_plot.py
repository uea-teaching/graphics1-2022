"""
Plots for the transforms 03 lecture

Useful links:
Arcs : https://stackoverflow.com/a/54850819/10188737
"""

# %%

import numpy as np
import matplotlib.pyplot as plt

from utils import *
set_style()
plt.rcParams['figure.figsize'] = [6.0, 5.0]

FILL0 = (0.5, 0.5, 0.5, 0.5)
FILL1 = (0.5, 0.0, 0.5, 0.5)
FILL2 = (0.0, 0.5, 0.5, 0.5)
FILL3 = (0.5, 0.5, 0.0, 0.5)
STROKE = (0.0, 0.0, 0.0, 1.0)


# %%

# square homogeneous coordinates
square = np.array([
    [-0.5, -0.5, 1], [0.5, -0.5, 1],
    [0.5, 0.5, 1], [-0.5, 0.5, 1]]).T

# %%

spines = dict(x_range=(-1, 6), y_range=(-1, 6),
              colour=(0.5, 0.5, 0.5), line_width=0.7)


def plot_rect(ax, rect, col=FILL0):
    """plot a rectangle"""
    ax.fill(rect[0], rect[1], facecolor=col, edgecolor=STROKE, linewidth=1)


# start
fig, ax = plt.subplots(1, 1)
set_spines(ax, **spines)
ax.text(0, 0.7, s=r'$s$', ha='center', va='center')
plot_rect(ax, square)
ax.grid(False)
fig.savefig("articulated_start.png")

# %%


def scale_xy(x=1, y=1):
    """scale the x and y axes"""
    return np.array([[x, 0, 0],
                     [0, y, 0],
                     [0, 0, 1]])


def trans_xy(x=0, y=0):
    """transform the x and y axes"""
    return np.array([[1, 0, x],
                     [0, 1, y],
                     [0, 0, 1]])


def R(a):
    """Rotation matrix"""
    rad = a / 180 * np.pi
    return np.array([[np.cos(rad), -np.sin(rad), 0],
                     [np.sin(rad), np.cos(rad), 0],
                     [0, 0, 1]])


# %%

a, b, c, alpha, beta = 2, 3, 2, 30, 45

# %%

# gantry
gantry = trans_xy(y=a/2) @ scale_xy(y=a) @ square.copy()

fig, ax = plt.subplots(1, 1)
set_spines(ax, **spines)
plot_rect(ax, gantry, col=FILL1)
ax.grid(False)


# %%

# link1
link1 = (trans_xy(y=a)
         @ R(alpha)
         @ trans_xy(x=b / 2)
         @ scale_xy(x=b)
         @ square.copy())

fig, ax = plt.subplots(1, 1)
set_spines(ax, **spines)
plot_rect(ax, gantry, col=FILL1)
plot_rect(ax, link1, col=FILL2)
ax.grid(False)

# %%

# link2
link2 = (trans_xy(y=a)
         @ R(alpha)
         @ trans_xy(x=b)
         @ R(beta)
         @ trans_xy(x=c / 2)
         @ scale_xy(x=c)
         @ square.copy())

fig, ax = plt.subplots(1, 1)
set_spines(ax, **spines)
plot_rect(ax, gantry, col=FILL1)
plot_rect(ax, link1, col=FILL2)
plot_rect(ax, link2, col=FILL3)
ax.grid(False)

# %%

fig, ax = plt.subplots(1, 1)
set_spines(ax, **spines)
plot_rect(ax, gantry, col=FILL1)
plot_rect(ax, link1, col=FILL2)
plot_rect(ax, link2, col=FILL3)
ax.grid(False)
ax.text(-0.75, 1, s=rf'${a}s$', ha='center', va='center', fontsize=12)
ax.text(1, 3.5, s=rf'${b}s$', ha='center', va='center', fontsize=12)
ax.text(2, 4.75, s=rf'${c}s$', ha='center', va='center', fontsize=12)


# %%

p1_1 = (link1[:2, 0] + link1[:2, 3]) * 0.5
p1_2 = p1_1 + 2 * (link1[:2, 1] - link1[:2, 0]).T

p2_1 = (link2[:2, 0] + link2[:2, 3]) * 0.5
p2_2 = p2_1 + 2 * (link2[:2, 1] - link2[:2, 0]).T

fig, ax = plt.subplots(1, 1)
set_spines(ax, **spines)
plot_rect(ax, gantry, col=FILL1)
plot_rect(ax, link1, col=FILL2)
plot_rect(ax, link2, col=FILL3)
ax.grid(False)
ax.text(-0.75, 1, s=rf'${a}s$', ha='center', va='center', fontsize=12)
ax.text(1, 3.5, s=rf'${b}s$', ha='center', va='center', fontsize=12)
ax.text(2, 4.75, s=rf'${c}s$', ha='center', va='center', fontsize=12)
ax.plot((0, 5), (2, 2), '--k', linewidth=1)
ax.plot((p1_1[0], p1_2[0]), (p1_1[1], p1_2[1]), '--k', linewidth=1)
ax.plot((p2_1[0], p2_2[0]), (p2_1[1], p2_2[1]), '--k', linewidth=1)

AngleAnnotation(
    p1_1, (p2_1[0], 2), p1_2, ax=ax, size=1000, unit='pixels',
    textposition='outside',
    color='k', text=rf"$\alpha={alpha}^{{\circ}}$")

AngleAnnotation(
    p2_1, p1_2, p2_2, ax=ax, size=600, unit='pixels',
    textposition='outside',
    color='k', text=rf"$\beta={beta}^{{\circ}}$")

# %%
