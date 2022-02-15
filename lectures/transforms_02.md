---
title: Further Transformations
subtitle: Graphics 1 CMP-5010B
author: Dr. David Greenwood
date: \today
---

# Content

- Inverse Rotations
- Scaling and Shearing
- Homogeneous Coordinates

# Inverse Rotations

::: {style="font-size: 2.5em"}

$$R^{-1}$$

:::

## Inverse Rotations

We commonly need to compute the inverse of a rotation, for example, in the hierarchical transformations in character animation skeletons.

## Inverse Rotations

$$
\begin{aligned}
v' &= R v \\
v  &= R^{-1} v'
\end{aligned}
$$

Where $R$ is the rotation matrix and $v$ is a vertex.

## Properties of Rotation Matrices {data-auto-animate="true"}

- Rotation matrices are square

::: notes
square means the dimensions are nxn.
BUT not all square matrices are rotation matrices.
We can represent rotations with alternate entities, but they are not rotation matrices.
:::

## Properties of Rotation Matrices {data-auto-animate="true"}

The determinant of a rotation matrix is 1

- because: $\cos^2(\theta) + \sin^2(\theta) = 1$
- hint: think about the radius in the unit circle

::: notes
Pythagoras' theorem
:::

## Properties of Rotation Matrices {data-auto-animate="true"}

Rotation matrices are orthonormal

- column vectors are orthogonal
- column vectors are unit
- hint: think about the radius in the unit circle
- exercise: plot the column vectors

::: notes
orthogonal means the vectors are perpendicular to each other.
unit means the vectors have a magnitude of 1.
:::

## Properties of Rotation Matrices {data-auto-animate="true"}

$$
R^TR = I, RR^T = I
$$

Where $I$ is the identity matrix.

::: notes
The transpose of a matrix is to write the columns of the matrix as rows.
:::

## Properties of Rotation Matrices {data-auto-animate="true"}

We can use all these properties to test if a matrix is a rotation matrix.

::: notes
This can be really useful in debugging your code.
:::

## Inverse Rotation Matrices {data-auto-animate="true"}

Therefore the _inverse_ of a rotation matrix **is** the _transpose_ of the rotation matrix.

$$
R^{-1} = R^T
$$

## Inverse Rotation Matrices {data-auto-animate="true"}

Therefore the _inverse_ of a rotation matrix **is** the _transpose_ of the rotation matrix.

$$
\begin{bmatrix}
\cos \alpha &-\sin \alpha \\
\sin \alpha &~\cos \alpha
\end{bmatrix}^{-1} =
\begin{bmatrix}
\cos \alpha &-\sin \alpha \\
\sin \alpha &~\cos \alpha
\end{bmatrix}^T =
\begin{bmatrix}
~\cos \alpha &\sin \alpha \\
-\sin \alpha &\cos \alpha
\end{bmatrix}
$$

::: notes
You can see this is also equivalent to rotating in the opposite direction.
This is trivial in 2D, but in 3D, it is not.
:::
