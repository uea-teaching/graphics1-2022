# %%

import svgwrite


# %%

# some consistent components

axes_color = 'black'
stroke_width = 1
fill_color = '#f0f0f0'


def arrowhead(dwg, x=0, y=2, dx=5, dy=4):
    """Add an arrowhead marker to the drawing"""
    marker = dwg.marker(insert=(x, y), size=(dx, dy),
                        orient="auto", id="arrowhead")
    shape = dwg.polygon(
        points=[[x, 0], [dx, y], [x, dy]],
        fill=axes_color)
    marker.add(shape)
    dwg.defs.add(marker)
    return marker


def axes(dwg):
    """Add an axes to the drawing. using 2 lines.
    """
    xmin, xmax, ymin, ymax = 0, 100, 100, 0
    marker = arrowhead(dwg)
    x_line = dwg.line(start=(xmin, ymin), end=(xmax, ymin),
                      stroke=axes_color,
                      stroke_width=stroke_width)
    y_line = dwg.line(start=(xmin, ymin), end=(xmin, ymax),
                      stroke=axes_color,
                      stroke_width=stroke_width)
    x_axis = dwg.add(x_line)
    x_axis['marker-end'] = marker.get_funciri()
    y_axis = dwg.add(y_line)
    y_axis['marker-end'] = marker.get_funciri()


dwg = svgwrite.Drawing(size=(600, 400), debug=True)
dwg.viewbox(-20, -80, width=300, height=200)

axes(dwg)
dwg

# %%
print(dwg._repr_svg_())
