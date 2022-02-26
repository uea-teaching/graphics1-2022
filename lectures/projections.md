---
title: Projections
subtitle: Graphics 1 CMP-5010B
author: Dr. David Greenwood
date: February, 2022
---

# Content

- The Camera Model
- Perspective Projection
- Orthographic Projection

# Projection

From 3D to 2D...

## Projection {data=auto-animate="true"}

To give a meaningful account of projection in graphics we have to move to 3D.

- Projection from 3D results in a 2D image.

## Projection {data=auto-animate="true"}

There are typically two types of projections we consider in graphics:

- Perspective projection
- Orthographic projection

## Camera Model {data=auto-animate="true"}

![Camera Model: E. Angel, Interactive Computer Graphics](assets/png/camera-world.png){width="70%"}

::: notes
In graphics we have a coordinate system for the world, in which all objects are placed.
We often refer to these as the **world coordinate system**.

Within the world, we have objects, that have their own coordinate system.

We have an **image** coordinate system - this is always 2D, and is where we project the objects within the world.

Then we have a camera coordinate system - this is 3D and is a view of the world with respect to the camera.

:::

## View Frustum {data=auto-animate="true"}

![view frustum](assets/svg/frustum1.svg)

::: notes
The view frustum (a word difficult to pronounce) is a bound on the objects to be rendered.
It is defined by the angle of view, and the near and far clipping planes.
:::

## View Frustum {data=auto-animate="true"}

![projection on near plane](assets/svg/frustum2.svg)

::: notes
The locus of convergence of the frustum is the position of the camera.
We project at the near clipping plane in image coordinate space.
:::

## View Frustum {data=auto-animate="true"}

![view frustum culling](assets/svg/frustum3.svg)

::: notes
Only objects within the view frustum are rendered.
This is an important tool for rendering efficiently.
In project - near objects are larger, far objects are smaller.
:::

## View Frustum {data=auto-animate="true"}

![frustum metrics](assets/svg/frustum4.svg)

::: notes
d = distance from camera to the projection plane (the near plane of the frustum).
Z_c = distance from camera to the object - in camera coordinate space.
:::

## Perspective Projection {data=auto-animate="true"}

We need to extend the idea of _homogeneous_ coordinates to 3D.

The perspective projection is a projection from 3D to 2D, so we need a 4 x 4 matrix to transform 3D points in homogeneous coordinates.

## {data=auto-animate="true"}

consider a horizontal cross section of the scene:

![x-section](assets/svg/perspective-x.svg){width="70%"}

## {data=auto-animate="true"}

The relationship between the the 3D camera coordinate $x_c$ and the 2D image coordinate $x_i$ is:

::: columns

::::: {.column width=70%}
![x-section](assets/svg/perspective-x.svg){width="100%"}
:::::

::::: {.column style="font-size: 1.0em"}
$$\frac{x_i}{d} = \frac{x_c}{z_c}$$

$$\Rightarrow x_i = \frac{x_c}{\frac{z_c}{d}}$$
:::::

:::

::: notes
we want to find x_i - the image coordinate - we know the camera coordinate.
there is a reason why we put d in the denominator of the denominator...
:::

## {data=auto-animate="true"}

The relationship between the the 3D camera coordinate $y_c$ and the 2D image coordinate $y_i$ is:

::: columns

::::: {.column width=70%}
![y-section](assets/svg/perspective-y.svg){width="100%"}
:::::

::::: {.column style="font-size: 1.0em"}
$$\frac{y_i}{d} = \frac{y_c}{z_c}$$

$$\Rightarrow y_i = \frac{y_c}{\frac{z_c}{d}}$$
:::::

:::

::: notes
In a similar way we can find y_i in the vertical cross section.
:::
