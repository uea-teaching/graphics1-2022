---
title: Combined Transformations
subtitle: Graphics 1 CMP-5010B
author: Dr. David Greenwood
date: February, 2022
---

# Content

- World Coordinate System
- Combined Transformations
- Articulated Structures

# Combining 2D Transformations

**Order** matters!

## Recap {data-auto-animate="true"}

So far we have looked at individual 2D transformations applied to the vertices of a 2D polygon.

::: notes
Even though a polygon - or indeed a model - may have many vertices, we apply the same operation to each vertex.
:::

## Recap {data-auto-animate="true"}

Having put in place a uniform method, applicable to **all** transformations, we can now look at _combining_ transformations.

::: notes
What is this uniform method called?
:::

## Recap {data-auto-animate="true"}

We will show now that the _order_ of the applied transformations is absolutely **crucial** to obtain the desired results!

## World Coordinate System {data-auto-animate="true"}

Where in the world do we start?

## World Coordinate System {data-auto-animate="true"}

Most graphics systems adopt a World Coordinate System (WCS),
with a camera in a particular position and orientation.

## World Coordinate System {data-auto-animate="true"}

For example in _OpenGL_, the camera is at the origin of the WCS pointing in the negative z-direction with its "up" vector pointing in the y-direction.

::: notes
Different frameworks adopt different conventions. It is common to see z-up and y-up.
3D packages?
Note - these are just labels for consistent reference - we could easily convert to other conventions.
:::

## World Coordinate System {data-auto-animate="true"}

So far we have been working with 2D transformations.

Given the description of the OpenGL coordinate system, what has been the significance of the z-axis?

::: incremental

- Answer: It is the _axis_ of **rotation**.

:::

::: notes
wherever some vertex is in our scene, when we rotate with R, we rotate about the z-axis.
:::

## World Coordinate System {data-auto-animate="true"}

::: columns

::: column

The WCS is represented by a _right-handed_ coordinate system, with the z-axis popping out of the screen.

- For 2D, we draw in the x-y plane, and **rotate** about the z-axis.

:::

::: column
![right handed coordinate system](assets/svg/xyz-gnomon.svg)
:::

:::

# Combined Transformations

**Order** matters...

::: notes
This is the big takeaway from this lecture.
:::

## Recap: Matrix Multiplication

Matrix multiplication **is** _associative_:

$$ABC=A(BC)=(AB)C$$

Matrix multiplication is **not** _commutative_:

$$AB \neq BA$$

::: notes
Of course, we need the shape to be appropriate for multiplication.
Emphasis - this is really important to understand - and remember.
:::

# Combined Transformations

Start with two common concatenated transformations:

1. _Rotate_ the model, then _translate_ it.
2. _Translate_ the model, then _rotate_ it.

::: notes
As well as the rules of multiplication, we need to remember that the order of the transformations is important.
REMEMBER: Rotation is about the z-axis!!
:::

# Combined Transformations

Start with two common concatenated transformations:

1. $$
   \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} =
   \begin{bmatrix} 1  & ~0& ~t_x \\ 0  & ~1& ~t_y \\ 0  & ~0& ~1 \end{bmatrix}
   \begin{bmatrix}
    \cos \alpha&        -\sin \alpha& ~0 \\
    \sin \alpha&~       ~\cos \alpha& ~0 \\
            0&                   0& ~1
    \end{bmatrix}
   \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
   $$

2. $$
   \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} =
   \begin{bmatrix}
    \cos \alpha&        -\sin \alpha& ~0 \\
    \sin \alpha&~       ~\cos \alpha& ~0 \\
            0&                   0& ~1
    \end{bmatrix}
   \begin{bmatrix} 1  & ~0& ~t_x \\ 0  & ~1& ~t_y \\ 0  & ~0& ~1 \end{bmatrix}
   \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
   $$

::: notes
let's look at this more concretely, with two very common transforms.
:::

---

Multiplying out the first example from right to left:

1. $$
    \begin{aligned}
    \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} &=
    %
    \begin{bmatrix} 1  & ~0& ~t_x \\ 0  & ~1& ~t_y \\ 0  & ~0& ~1 \end{bmatrix}
    %
    \begin{bmatrix}
    x \cos \alpha - y \sin \alpha \\
    x \sin \alpha + y \cos \alpha \\
    1
    \end{bmatrix} \\[10pt]
    %
    \Rightarrow
    %
    \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} &=
    \begin{bmatrix}
    (x \cos \alpha - y \sin \alpha) + t_x \\
    (x \sin \alpha + y \cos \alpha) + t_y \\
    1
    \end{bmatrix}
    \end{aligned}
   $$

::: notes
let's multiply out from right to left.
Here we rotate first, then translate.
:::

---

Multiplying out the second example from right to left:

2. $$
    \begin{aligned}
    \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} &=
    %
   \begin{bmatrix}
    \cos \alpha&  -\sin \alpha& ~0 \\
    \sin \alpha&~ ~\cos \alpha& ~0 \\
               0&            0& ~1
    \end{bmatrix}
    %
    \begin{bmatrix} x + t_x \\ y + t_y \\ 1 \end{bmatrix} \\[10pt]
    %
    \Rightarrow
    %
    \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} &=
    \begin{bmatrix}
    (x + t_x) \cos \alpha - (y + t_y) \sin \alpha \\
    (x + t_x) \sin \alpha + (y + t_y) \cos \alpha \\
    1
    \end{bmatrix}
    \end{aligned}
   $$

::: notes
now the 2nd equation - translate first then rotate.
:::

# Combined Transformations

::: {style="font-size: 2.5em"}

$$
RTv \neq TRv
$$

:::

The **order** of the transformations is important.
