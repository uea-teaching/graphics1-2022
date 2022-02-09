import numpy as np
import matplotlib.pyplot as plt


def set_style():
    """set the style of the plots"""
    plt.style.use('fivethirtyeight')
    plt.rcParams['figure.figsize'] = [9.0, 5.0]
    plt.rcParams['figure.dpi'] = 240
    plt.rcParams['axes.linewidth'] = 1.25
    plt.rcParams['savefig.pad_inches'] = 0.2
    plt.rcParams['savefig.bbox'] = 'tight'


def set_spines(ax, x_range=(-7, 15), y_range=(-5, 10)):
    """move the axes to the centre and show a labelled grid."""
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['left', 'bottom']].set_visible(True)
    ax.spines[['left', 'bottom']].set_color('black')
    ax.spines[['left', 'bottom']].set_position(('data', 0))
    # arrows on ends of axes
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    # grid
    ax.set_aspect('equal')
    x_ticks = range(x_range[0], x_range[1] + 1)
    y_ticks = range(y_range[0], y_range[1] + 1)
    x_tick_labels = ['' for _ in x_ticks[:-1]] + [r'$x$']
    y_tick_labels = ['' for _ in y_ticks[:-1]] + [r'$y$']
    ax.set_xticks(x_ticks, labels=x_tick_labels)
    ax.set_yticks(y_ticks, labels=y_tick_labels)
    ax.set_xlim(x_range)
    ax.set_ylim(y_range)


def point_label(ax, p=(0, 0), label_offset=None, color='k'):
    """add a label to the origin"""
    if label_offset is None:
        label_offset = (0.25, -0.75)
    x, y = p[0] + label_offset[0], p[1] + label_offset[1]
    ax.text(x, y, f'({p[0]}, {p[1]})', color=color, fontsize=10)


def plot_vector(ax, v, p=(0, 0), color='g', label_offset=None, label=True):
    """plot a vector"""
    if label_offset is None:
        label_offset = (0.25, -0.75)
    d = v-p
    ax.arrow(p[0], p[1], d[0], d[1], color=color, linestyle='--',
             linewidth=1.5, head_width=0.25, head_length=0.25,
             length_includes_head=True)
    if label:
        point_label(ax, v, label_offset=label_offset, color=color)


def plot_triangle(ax, points, facecolor=(0.5, 0.0, 0.5, 0.5),
                  label_offsets=None, labels=True):
    """plot a triangle"""
    ax.fill(points[:, 0], points[:, 1],
            facecolor=facecolor, edgecolor='k', linewidth=1)

    if label_offsets is None:
        label_offsets = [[-0.5, -0.75], [0.5, 0.0], [-0.5, -0.75]]
    if labels:
        for p, offset in zip(points, label_offsets):
            point_label(ax, p, offset)
