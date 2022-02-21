"""
Insert values into the maths environment
"""
# %%


def R(angle=r'\alpha'):
    return (rf"\begin{{bmatrix}}" "\n"
            rf"    \cos {angle} & - \sin {angle} & 0 \\" "\n"
            rf"    \sin {angle} & \cos {angle} & 0 \\ " "\n"
            rf"    0 & 0 & 1" "\n"
            rf"\end{{bmatrix}}")


def translate_xy(x=0, y=0):
    return (rf"\begin{{bmatrix}}" "\n"
            rf"    1 & 0 & {x} \\" "\n"
            rf"    0 & 1 & {y} \\" "\n"
            rf"    0 & 0 & 1" "\n"
            rf"\end{{bmatrix}}")


def scale_xy(x=1, y=1):
    return (rf"\begin{{bmatrix}}" "\n"
            rf"    {x} & 0 & 0 \\" "\n"
            rf"    0 & {y} & 0 \\" "\n"
            rf"    0 & 0 & 1" "\n"
            rf"\end{{bmatrix}}")


def vert():
    return rf"\begin{{bmatrix}} x \\ y \\ 1 \end{{bmatrix}}"


def vert_prime():
    return rf"\begin{{bmatrix}} x' \\ y' \\ 1 \end{{bmatrix}}"


# %%

def gantry(y_scale):
    ty = "s" if y_scale == 2 else f"{y_scale * 0.5:.2f}s"
    return ("$$\n" f"{vert_prime()}" "= \n"
            f"{translate_xy(x=0, y=ty)}\n"
            f"{scale_xy(x=1, y=y_scale)}\n"
            f"{vert()} \n$$")


# %%


def link_1(gantry_y_scale, link1_x_scale):
    gys = "s" if gantry_y_scale == 1 else f"{gantry_y_scale}s"
    lx = "s" if link1_x_scale == 2 else f"{link1_x_scale * 0.5:.2f}s"
    alpha = R(angle=r'\alpha')
    return ("$$\n" f"{vert_prime()}" "= \n"
            f"{translate_xy(x=0, y=gys)}\n"
            f"{alpha}\n"
            f"{translate_xy(x=lx, y=0)}\n"
            f"{scale_xy(x=link1_x_scale, y=1)}\n"
            f"{vert()} \n$$")


# %%


def link_2(gantry_y_scale, link1_x_scale, link2_x_scale):
    gys = "s" if gantry_y_scale == 1 else f"{gantry_y_scale}s"
    l1x = "s" if link1_x_scale == 1 else f"{link1_x_scale:.2f}s"
    l2x = "s" if link2_x_scale == 2 else f"{link2_x_scale * 0.5:.2f}s"
    alpha = R(angle=r'\alpha')
    beta = R(angle=r'\beta')
    return ("$$\n" f"{vert_prime()}" " = \n"
            f"{translate_xy(x=0, y=gys)}\n"
            f"{alpha}\n"
            f"{translate_xy(x=l1x, y=0)}\n"
            f"{beta}\n"
            f"{translate_xy(x=l2x, y=0)}\n"
            f"{scale_xy(x=link2_x_scale, y=1)}\n"
            f"{vert()} \n$$")

# %%


# example
a, b, c, alpha, beta = 2, 1.5, 3, 30, 60

print(gantry(a))
print(link_1(a, b))
print(link_2(a, b, c))
