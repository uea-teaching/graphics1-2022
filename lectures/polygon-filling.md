---
title: Polygon Filling
subtitle: Graphics 1 CMP-5010B
author: Dr. David Greenwood
date: Spring 2022
---

# Content

- Polygon Filling
- Scan Line Algorithm
- Boundary Fill Algorithm

::: notes
We can start with what we mean by polygon filling - then we will look at a couple of different approaches to solve the problem.
Scan-line algorithm - works line by line and left to right to fill the polygon.
Boundary fill algorithm - works by growing a seed pixel within the boundary of the polygon.
:::

# Polygon Filling {data-auto-animate="true"}

Identify pixels that belong to the _interior_ of a polygon.
Once identified, we can:

::: incremental

- pass the pixel to the rasteriser
- assign colour to the pixel
- assign a depth value to the pixel
- sample a texture for the pixel

:::

::: notes
once we identify the pixel, we can perform a number of operations, given that knowledge.
:::

## Polygon Filling {data-auto-animate="true"}

::: incremental

- A polygon is a set of vertices that are connected by _edges_.
- We need _efficient_ algorithms to fill polygons.
- We can extend ideas from line drawing to polygon filling.
- Not all polygons are handled equally!

:::

::: notes
Graphics applications often use many, many polygons.
:::

## Convex Polygons {data-auto-animate="true"}

::: columns
::::: column
![convex polygon](assets/svg/convex_poly.svg)
:::::
::::: column

- interior angles $\leq 180^{\circ}$
- scan lines enter the interior once and exit once
- triangles are always convex

:::::
:::

::: notes
I want to be clear here - a scan line is the line we intend to draw
horizontally across the screen.
If we encounter a convex polygon it enters, then exits only once.
Triangles are convex.
One of the reasons many graphics pipelines decompose to tris - they are easier to handle.
:::

## Concave Polygons {data-auto-animate="true"}

::: columns
::::: column
![concave polygon](assets/svg/concave_poly.svg)
:::::
::::: column

- arbitrarily complex polygons
- scan lines enter and exit many times
- more difficult to fill

:::::
:::

::: notes
can be arbitrarily complex - many vertices and edges - ngons
:::
