### Unit V: Linear Transformations (06 Hrs)

5.1 Definition and Examples, Properties, Equality  
5.2 Kernel and range of a linear Transformation  
5.3 Rank-Nullity theorem (Statement only)  
5.4 Matrix representation of Linear Transformation

---

# Chapter 5: Linear Transformations

This chapter introduces **linear transformations** between vector spaces, covering their definitions, properties, kernels, ranges, the Rank-Nullity theorem, and how these transformations can be represented by matrices.

---

## 5.1 Definition, Examples, and Properties

A **linear transformation** $T$ from a vector space $V$ to another vector space $W$ (over the same field) is a function satisfying:

1. **Additivity**: $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ for all $\mathbf{u}, \mathbf{v} \in V$.
2. **Homogeneity**: $T(c \mathbf{v}) = c \, T(\mathbf{v})$ for all $\mathbf{v} \in V$ and scalars $c$.

**Examples**

- The **zero transformation** $T(\mathbf{v}) = \mathbf{0}$ for all $\mathbf{v} \in V$.
- Any **matrix multiplication** $T(\mathbf{v}) = A\mathbf{v}$ where $A$ is an $m \times n$ matrix and $\mathbf{v} \in \mathbb{R}^n$.
- The **identity transformation** $T(\mathbf{v}) = \mathbf{v}$.

**Equality of Transformations**  
Two transformations $T_1$ and $T_2$ from $V$ to $W$ are equal if $T_1(\mathbf{v}) = T_2(\mathbf{v})$ for every $\mathbf{v} \in V$.

---

## 5.2 Kernel and Range

For a linear transformation $T: V \to W$:

- **Kernel (or Null Space):**

  $$
  \ker(T) = \{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}\}.
  $$

  The kernel captures all vectors in $V$ that map to the zero vector in $W$.

- **Range (or Image):**
  $$
  \text{range}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in V\}.
  $$
  The range is the set of all output vectors in $W$.

---

## 5.3 Rank-Nullity Theorem (Statement Only)

For a linear transformation $T: V \to W$ where $V$ is finite-dimensional, the **Rank-Nullity Theorem** states:

$$
\dim(\ker(T)) + \dim(\text{range}(T)) = \dim(V).
$$

- $\dim(\ker(T))$ is called the **nullity** of $T$.
- $\dim(\text{range}(T))$ is called the **rank** of $T$.

---

## 5.4 Matrix Representation of a Linear Transformation

If $V$ and $W$ are finite-dimensional vector spaces with ordered bases

$$
\mathcal{B}_V = \{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n\}
\quad \text{and} \quad
\mathcal{B}_W = \{\mathbf{w}_1, \mathbf{w}_2, \dots, \mathbf{w}_m\},
$$

then any linear transformation $T: V \to W$ can be represented by an $m \times n$ matrix $A$ such that:

$$
T(\mathbf{v}_j) \quad \longleftrightarrow \quad \text{the } j\text{th column of } A.
$$

To find the matrix representation:

1. Compute $T(\mathbf{v}_j)$ for each basis vector $\mathbf{v}_j$.
2. Express $T(\mathbf{v}_j)$ in terms of the basis $\mathcal{B}_W$.
3. The coordinates become the columns of the matrix $A$.

---

## Code Example: Finding Matrix Representation in Python

Below is a conceptual example using Python (and a symbolic library like Sympy) to represent a linear transformation given by $T(x, y, z) = (x + y, 2y + 3z)$ from $\mathbb{R}^3$ to $\mathbb{R}^2$.

```python
import sympy

# Symbolic variables
x, y, z = sympy.symbols('x y z')

# Define the transformation T
# T(x, y, z) -> (x + y, 2y + 3z)
T = sympy.Matrix([[x + y], [2*y + 3*z]])

# Suppose the domain basis is e1=(1,0,0), e2=(0,1,0), e3=(0,0,1).
e1 = sympy.Matrix([1, 0, 0])
e2 = sympy.Matrix([0, 1, 0])
e3 = sympy.Matrix([0, 0, 1])

# Apply T to each basis vector
T_e1 = T.subs({x: 1, y: 0, z: 0})  # T(e1)
T_e2 = T.subs({x: 0, y: 1, z: 0})  # T(e2)
T_e3 = T.subs({x: 0, y: 0, z: 1})  # T(e3)

# Form the matrix (in the standard basis for R^2)
A = T_e1.row_join(T_e2).row_join(T_e3)
print("Matrix representation of T:\n", A)
```

### Practice Exercises

1. **Kernel and Range**  
   Define a linear transformation $T: \mathbb{R}^2 \to \mathbb{R}^2$ by

   $$
   T(x,y) = (x - y, x).
   $$

   Find $\ker(T)$ and $\text{range}(T)$.  
   Verify the rank-nullity theorem for this transformation.

2. **Matrix Representation**  
   Let $T: \mathbb{R}^3 \to \mathbb{R}^2$ be given by

   $$
   T(x,y,z) = (x + 2y,\, y - z).
   $$

   Find the matrix representation of $T$ with respect to the standard bases of $\mathbb{R}^3$ and $\mathbb{R}^2$.  
   Confirm that applying the matrix to a vector $(x,y,z)$ in coordinate form gives the same result as applying $T$ directly.

3. **Rank-Nullity**  
   Provide a linear transformation $T: \mathbb{R}^3 \to \mathbb{R}^3$ whose nullity is 1 and whose rank is 2.  
   Show all the work leading to your conclusion, including the matrix form and the basis for the kernel.

---

### End-of-Chapter Question

**Q1.** In your own words, restate the Rank-Nullity theorem and discuss its interpretation in terms of transformations. Why is the kernel crucial in understanding whether a linear transformation is injective?
