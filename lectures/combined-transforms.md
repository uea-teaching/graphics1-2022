---
title: Combined Transformations
subtitle: Graphics 1 CMP-5010B
author: Dr. David Greenwood
date: February 21, 2022
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
