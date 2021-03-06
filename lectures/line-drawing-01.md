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

## Cartesian Line Equation {data-auto-animate="true"}

Algebraically, we can define a line with an **implicit** _linear_ equation:

::: {style="font-size: 1.8em;"}

$$
ax + by + c = 0
$$

:::

::: notes
or algebraic form.
:::

## Cartesian Line Equation {data-auto-animate="true"}

We can derive the implicit form of the line equation from the vector equation.

- Consider coordinates of points on the line as vectors projected to the x-axis and y-axis.
- Apply the vector equation to the x-axis and y-axis projection to obtain the implicit form.

## Cartesian Line Equation {data-auto-animate="true"}

::: columns
::::: {.column width=60%}
![Parametric Line](assets/svg/implicit-line.svg)
:::::
::::: {.column style="font-size: 1.0em;"}

Projecting to the x-axis and y-axis.

$$
\begin{aligned}
\textbf{x} &= \textbf{x}_0 + \lambda(\textbf{x}_1 - \textbf{x}_0) \\
\textbf{y} &= \textbf{y}_0 + \lambda(\textbf{y}_1 - \textbf{y}_0)
\end{aligned}
$$

:::::
:::

::: notes
note that x and y are bold and are vectors, not scalars.
:::

## Cartesian Line Equation {data-auto-animate="true"}

We can remove the scalar $\lambda$ using simultaneous equations:

$$
\begin{aligned}
\textbf{x} &= \textbf{x}_0 + \lambda(\textbf{x}_1 - \textbf{x}_0)
\hspace{20pt} \times (\textbf{y}_1 - \textbf{y}_0) \\
- \textbf{y} &= \textbf{y}_0 + \lambda(\textbf{y}_1 - \textbf{y}_0)
\hspace{20pt} \times (\textbf{x}_1 - \textbf{x}_0)
\end{aligned}
$$

::: notes
we multiply each equation... then subtract...
:::

## Cartesian Line Equation {data-auto-animate="true"}

Giving:

$$
\begin{aligned}
\textbf{x} (\textbf{y}_1 - \textbf{y}_0) - \textbf{y} (\textbf{x}_1 - \textbf{x}_0) &= \textbf{x}_0 (\textbf{y}_1 - \textbf{y}_0) - \textbf{y}_0 (\textbf{x}_1 - \textbf{x}_0) \\
a \textbf{x} + b \textbf{y} &= -c
\end{aligned}
$$

with:

$$
\begin{aligned}
a &= \textbf{y}_1 - \textbf{y}_0 \\
b &= \textbf{x}_0 - \textbf{x}_1 \\
c &= -b\textbf{y}_0 - a\textbf{x}_0
\end{aligned}
$$

::: notes
bold x and y are the vectors projected to the axes...
:::

## Cartesian Line Equation {data-auto-animate="true"}

The vectors $\textbf{x}$ and $\textbf{y}$ can be replaced with scalar values $x$ and $y$, yielding:

$$
ax + by + c = 0 \hspace{20pt} \square
$$

::: notes
Q.E.D. quod erat demonstrandum - what was demonstrated...
:::

## Cartesian Line Equation {data-auto-animate="true"}

The implicit equation has the form:

$$
f(x, y) = C
$$

where $C$ is a constant.

::: notes
so the this is a function of two variables, x, y.
:::

## Cartesian Line Equation {data-auto-animate="true"}

There is also an **explicit** algebraic equation of the form:

$$
y = f(x)
$$

::: notes
so the this is a function of x, x is an independent variable, y is a dependent variable.
:::

## Cartesian Line Equation {data-auto-animate="true"}

From:

$$
\begin{aligned}
ax + by + c =& ~0 \\
\Rightarrow y =&  - \frac{a}{b}x - \frac{c}{b} \\
\Rightarrow y =& mx + d
\end{aligned}
$$

where:

$$
m = - \frac{a}{b}~, ~ d = - \frac{c}{b}
$$

::: notes
note the difference between big C and small c.
:::

## Cartesian Line Equation {data-auto-animate="true"}

Although the explicit equation $y = mx + c$ may be familiar, for computer graphics it is inconvenient, since for vertical lines $m = \infty$.

# Scan Conversion

Lines in mathematics are continuous and have _infinite_ resolution.

A computer screen has finite resolution using discrete picture elements, or **pixels**.

::: notes
we may be rendering to screen, or rendering to an image file.
:::

## Scan Conversion {data-auto-animate="true"}

For rendering, we will discretise the line equation using finite deltas.

$$
y = m x + c \Rightarrow \delta y = \delta m x + c
$$

::: notes
finite differences...
:::

## Scan Conversion {data-auto-animate="true"}

- We always render line **segments**.
- Line segments have a defined start and end point.
- Hence, we can derive the slope and intercept of our line.

$$
\begin{aligned}
m &= \frac{y_{end} - y_0}{x_{end} - x_0} \\
c &= y_0 - m x_0
\end{aligned}
$$

::: notes
you can clearly see here the danger of division by zero.
:::

## Scan Conversion {data-auto-animate="true"}

**NB:** We will ignore the intercept $c$ for the following derivations.

- it should be added to the right-hand side of the equation for lines with $c \neq 0$

::: notes
for our algorithms under discussion, we will ignore the intercept $c$ for now.
so, all our discussion will be about lines that pass through the origin.
:::

# Digital Differential Analyser (DDA)

The digital differential analyser (DDA) is a scan-conversion line algorithm based on calculating either $\delta y$ or $\delta x$

::: notes
and as I have said previously we will ignore the intercept $c$ for now.
:::

## Digital Differential Analyser (DDA) {data-auto-animate="true"}

Calculating $\delta x$.
Since the distance between points is measured in pixels;
if we move pixel by pixel along the positive $x$ axis, we have:

$$
\delta x = x_{i+1} - x_i = 1
$$

::: notes
we just step right, one pixel at a time...
:::

## Digital Differential Analyser (DDA) {data-auto-animate="true"}

Calculating $\delta y$.

$$
\begin{aligned}
\delta y &= m \delta x \\
y_{i+1} - y_i &= m (x_{i+1} - x_i)
\end{aligned}
$$

Where $i$ is a grid position of a discreet point on the line,
and $i + 1$ is an immediate neighbour on the grid.

::: notes
grid positions are pixels on the screen or image
:::

## Digital Differential Analyser (DDA) {data-auto-animate="true"}

Given $\delta x = x_{i+1} - x_i = 1$:

$$
y_{i+1} = y_i + m
$$

Specifically for:

$$
0 \leq |m| \leq 1
$$

::: notes
be careful here, we have stated x increases by one to the right...
so for lines steeper than m = 1, we will have gaps between pixels.
:::

## Digital Differential Analyser (DDA) {data-auto-animate="true"}

::: columns
::::: column
![render octants](assets/svg/octants.svg)
:::::
::::: column
So far, our algorithm will draw lines when:

$$
0 \leq |m| \leq 1~ \text{and} ~ x \geq 0
$$

:::::
:::

## Digital Differential Analyser (DDA) {data-auto-animate="true"}

```{.c}
#include <stdlib.h>
#include <math.h>

inline int round (const float a) {
    return int (a + 0.5);
    }

// Assume a function setPixel exists.
...
```

::: notes
before we look at pseudo code for DDA , we need a couple of helper functions...
:::

## Digital Differential Analyser (DDA) {data-auto-animate="true"}

```{.c data-line-numbers="1-9|1|2-4|6-8"}
void naiveDDA (int x0, int y0, int xEnd, int yEnd){
    int x = x0;
    float y = float (y0);
    float m = float (yEnd - y0) / float (xEnd - x0);

   for (x = x0; x <= xEnd; x++) {
        setPixel (x, round (y));
        y += m;
} }
```

::: notes
our naive version of DDA that just draws in the right hand octants.
:::

## Digital Differential Analyser (DDA) {data-auto-animate="true"}

How do we draw in the other octants?

::: notes
or - what goes wrong for lines that are steep?
anyone have any suggestions?
:::

## Digital Differential Analyser (DDA) {data-auto-animate="true"}

For lines with an absolute positive slope greater than 1.0, we reverse the roles of $x$ and $y$.

That is, we sample at unit $y$ intervals, $\delta y = 1$, and calculate consecutive x values as:

$$
x_{i+1} = x_i + \frac{1}{m}
$$

## Digital Differential Analyser (DDA) {data-auto-animate="true"}

To cover the remaining octants, we _decrement_ $x$ and $y$.

Hence, for top, right, left and bottom octants, we have:

$$
\begin{aligned}
|m| > 1~&,~           ~\delta y =~~1,& x_{i+1} &= x_i + \frac{1}{m} \\
0 \leq |m| \leq 1~&,~ ~\delta x =~~1,& y_{i+1} &= y_i + m \\
0 \leq |m| \leq 1~&,~ ~\delta x = -1,& y_{i+1} &= y_i + m \\
|m| > 1~&,~           ~\delta y = -1,& x_{i+1} &= x_i + \frac{1}{m}
\end{aligned}
$$

::: notes
this now covers all octants.
:::

---

![all octants](assets/svg/all-octants.svg){width="65%"}

---

```{.c data-line-numbers="1-18"}
void lineDDA (int x0, int y0, int xEnd, int yEnd){
    int dx=xEnd-x0, dy=yEnd-y0, steps, k;
    float xIncrement, yIncrement, x = x0, y = y0;

   if (fabs (dx) > fabs (dy))
      steps = fabs (dx);
   else
      steps = fabs (dy);

   xIncrement = float (dx) / float (steps);
   yIncrement = float (dy) / float (steps);

   setPixel (round (x), round (y));
   for (k = 0; k < steps; k++) {
        x += xIncrement;
        y += yIncrement;
        setPixel (round (x), round (y));
} }
```

::: notes
code from the course text
:::

## Digital Differential Analyser (DDA) {data-auto-animate="true"}

DDA has a few problems:

::: incremental

- fails to take advantage of the integral nature of pixels
- floating point variables to store the slope.
- costly division operations to calculate the slope.

:::

::: notes
not only that we store the slope as a floating point number, but we cast back to int to draw the line.
:::

## Digital Differential Analyser (DDA) {data-auto-animate="true"}

The algorithm has a few problems:

- fails to take advantage of the integral nature of pixels
- floating point variables to store the slope.
- costly division operations to calculate the slope.

We will address these short comings in the next lecture.

# Summary

- Theory and Concepts
- Scan Conversion
- Digital Differential Analyser (DDA)

Reading:

- Hearn & Baker, _Computer Graphics with OpenGL_, 4th Edition, Chapter 5
