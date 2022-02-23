from matplotlib.transforms import IdentityTransform, TransformedBbox, Bbox
from matplotlib.patches import Arc
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


def set_spines(ax, x_range=(-7, 15), y_range=(-5, 10),
               colour=(0.0, 0.0, 0.0), line_width=1.0):
    """move the axes to the centre and show a labelled grid."""

    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['left', 'bottom']].set_visible(True)
    ax.spines[['left', 'bottom']].set_color(colour)
    ax.spines[['left', 'bottom']].set_linewidth(line_width)
    ax.spines[['left', 'bottom']].set_position(('data', 0))
    # arrows on ends of axes
    ax.plot(1, 0, ">", color=colour,
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^", color=colour,
            transform=ax.get_xaxis_transform(), clip_on=False)
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


class AngleAnnotation(Arc):
    """
    Draws an arc between two vectors which appears circular in display space.
    see:
    https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html
    """

    def __init__(self, xy, p1, p2, size=75, unit="points", ax=None,
                 text="", textposition="inside", text_kw=None, **kwargs):
        """
        Parameters
        ----------
        xy, p1, p2 : tuple or array of two floats
            Center position and two points. Angle annotation is drawn between
            the two vectors connecting *p1* and *p2* with *xy*, respectively.
            Units are data coordinates.

        size : float
            Diameter of the angle annotation in units specified by *unit*.

        unit : str
            One of the following strings to specify the unit of *size*:

            * "pixels": pixels
            * "points": points, use points instead of pixels to not have a
              dependence on the DPI
            * "axes width", "axes height": relative units of Axes width, height
            * "axes min", "axes max": minimum or maximum of relative Axes
              width, height

        ax : `matplotlib.axes.Axes`
            The Axes to add the angle annotation to.

        text : str
            The text to mark the angle with.

        textposition : {"inside", "outside", "edge"}
            Whether to show the text in- or outside the arc. "edge" can be used
            for custom positions anchored at the arc's edge.

        text_kw : dict
            Dictionary of arguments passed to the Annotation.

        **kwargs
            Further parameters are passed to `matplotlib.patches.Arc`. Use this
            to specify, color, linewidth etc. of the arc.

        """
        self.ax = ax or plt.gca()
        self._xydata = xy  # in data coordinates
        self.vec1 = p1
        self.vec2 = p2
        self.size = size
        self.unit = unit
        self.textposition = textposition

        super().__init__(self._xydata, size, size, angle=0.0,
                         theta1=self.theta1, theta2=self.theta2, **kwargs)

        self.set_transform(IdentityTransform())
        self.ax.add_patch(self)

        self.kw = dict(ha="center", va="center",
                       xycoords=IdentityTransform(),
                       xytext=(0, 0), textcoords="offset points",
                       annotation_clip=True)
        self.kw.update(text_kw or {})
        self.text = ax.annotate(text, xy=self._center, **self.kw)

    def get_size(self):
        factor = 1.
        if self.unit == "points":
            factor = self.ax.figure.dpi / 72.
        elif self.unit[:4] == "axes":
            b = TransformedBbox(Bbox.from_bounds(0, 0, 1, 1),
                                self.ax.transAxes)
            dic = {"max": max(b.width, b.height),
                   "min": min(b.width, b.height),
                   "width": b.width, "height": b.height}
            factor = dic[self.unit[5:]]
        return self.size * factor

    def set_size(self, size):
        self.size = size

    def get_center_in_pixels(self):
        """return center in pixels"""
        return self.ax.transData.transform(self._xydata)

    def set_center(self, xy):
        """set center in data coordinates"""
        self._xydata = xy

    def get_theta(self, vec):
        vec_in_pixels = self.ax.transData.transform(vec) - self._center
        return np.rad2deg(np.arctan2(vec_in_pixels[1], vec_in_pixels[0]))

    def get_theta1(self):
        return self.get_theta(self.vec1)

    def get_theta2(self):
        return self.get_theta(self.vec2)

    def set_theta(self, angle):
        pass

    # Redefine attributes of the Arc to always give values in pixel space
    _center = property(get_center_in_pixels, set_center)
    theta1 = property(get_theta1, set_theta)
    theta2 = property(get_theta2, set_theta)
    width = property(get_size, set_size)
    height = property(get_size, set_size)

    # The following two methods are needed to update the text position.
    def draw(self, renderer):
        self.update_text()
        super().draw(renderer)

    def update_text(self):
        c = self._center
        s = self.get_size()
        angle_span = (self.theta2 - self.theta1) % 360
        angle = np.deg2rad(self.theta1 + angle_span / 2)
        r = s / 2
        if self.textposition == "inside":
            r = s / np.interp(angle_span, [60, 90, 135, 180],
                              [3.3, 3.5, 3.8, 4])
        self.text.xy = c + r * np.array([np.cos(angle), np.sin(angle)])
        if self.textposition == "outside":
            def R90(a, r, w, h):
                if a < np.arctan(h/2/(r+w/2)):
                    return np.sqrt((r+w/2)**2 + (np.tan(a)*(r+w/2))**2)
                else:
                    c = np.sqrt((w/2)**2+(h/2)**2)
                    T = np.arcsin(c * np.cos(np.pi/2 - a + np.arcsin(h/2/c))/r)
                    xy = r * np.array([np.cos(a + T), np.sin(a + T)])
                    xy += np.array([w/2, h/2])
                    return np.sqrt(np.sum(xy**2))

            def R(a, r, w, h):
                aa = (a % (np.pi/4))*((a % (np.pi/2)) <= np.pi/4) + \
                     (np.pi/4 - (a % (np.pi/4)))*((a % (np.pi/2)) >= np.pi/4)
                return R90(aa, r, *[w, h][::int(np.sign(np.cos(2*a)))])

            bbox = self.text.get_window_extent()
            X = R(angle, r, bbox.width, bbox.height)
            trans = self.ax.figure.dpi_scale_trans.inverted()
            offs = trans.transform(((X-s/2), 0))[0] * 72
            self.text.set_position([offs*np.cos(angle), offs*np.sin(angle)])
