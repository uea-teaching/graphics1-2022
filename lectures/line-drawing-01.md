---
title: Introduction to Line Drawing
subtitle: Graphics 1 CMP-5010B
author: Dr. David Greenwood
date: Spring 2022
---

# Contents {data-transition="convex"}

- Theory and Concepts
- Scan Conversion
- Digital Differential Analyser (DDA)

# Lines

A **line** is an _infinitely_ thin, infinitely long collection of points extending in two opposite directions.

::: notes
We know intuitively what a line is, it is actually difficult to give a good mathematical definition.
:::

## Lines

A line **segment** has two _endpoints_ and all the points of the line between them.

::: notes
You can measure the length of a segment, but not of a line.
:::

## Lines

A **ray** is part of a line with one endpoint and extends infinitely in _one_ direction.

::: notes
You cannot measure the length of a ray.
:::

## Representing Lines

We will consider two line representations:

- Parametric, or vector form.
- Cartesian form.

## Parametric Line Equation

A line can be defined as the set of all points in space that satisfy two criteria:

1. Contains a point, which we identify by a position vector $\textbf{r}_0$.
2. The vector between $\textbf{r}_0$ and _any_ position vector $\textbf{r}$ _on_ the line, is **parallel** to a given vector $\textbf{v}$.

## Parametric Line Equation

The vector with initial point $\textbf{r}_0$ and terminal point $\textbf{r}$ is given by:

$$
\textbf{s} = \textbf{r} - \textbf{r}_0
$$

This vector must be parallel to $\textbf{v}$ hence, for some scalar $\lambda$:

$$\textbf{s} = \lambda\textbf{v}$$

## Parametric Line Equation

Any position vector $\textbf{r}$, corresponding to a point $P$ on the line has the form:

$$\textbf{r} = \textbf{r}_0 + \lambda\textbf{v}$$

where $\lambda$ is a scalar called a _parameter_, and this is the **vector** equation.

::: notes
it follows...
The parameter is allowed to be any value, so that any point on the line can be obtained from this equation, which is called the vector equation of the line.
:::

## Parametric Line Equation

::: columns
::::: {.column width=60%}
![Parametric Line](assets/svg/vector-line.svg)
:::::
::::: {.column style="font-size: 1.8em;"}
$$\textbf{r} = \textbf{r}_0 + \lambda\textbf{v}$$
:::::
:::

::: notes
we don't define a coordinate space here, as r0 is a position vector from any origin.
:::

## Cartesian Line Equation

Algebraically, we can define a line with a _linear_ equation:

::: notes
or algebraic form.
:::
