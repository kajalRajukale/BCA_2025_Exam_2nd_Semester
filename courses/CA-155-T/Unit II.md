Unit II: Vector Spaces - I
---

2.1 Definition and Examples
2.2 Subspaces
2.3 Linear Dependence and Independence
2.4 Basis of a Vector Space

---

# 2. Vector Spaces – I

This chapter introduces the fundamental ideas of vector spaces, subspaces, linear dependence and independence, and the concept of a basis.

---

## 2.1 Definition and Examples

A **vector space** over a field $\mathbb{F}$ (e.g., the real numbers $\mathbb{R}$) is a set $V$ equipped with two operations:
1. **Vector Addition**: $\mathbf{u} + \mathbf{v}$ for $\mathbf{u}, \mathbf{v} \in V$.
2. **Scalar Multiplication**: $c \mathbf{v}$ for a scalar $c \in \mathbb{F}$ and $\mathbf{v} \in V$.

These operations must satisfy certain axioms (commutativity, associativity, distributivity, etc.). Common examples include:
- $\mathbb{R}^n$: All $n$-tuples of real numbers.
- The space of all polynomials of degree $\leq n$, with standard polynomial addition and scalar multiplication.
- The space of all $m \times n$ real matrices.


## 2.2 Subspaces

A **subspace** of a vector space $V$ is a subset $W \subseteq V$ that is itself a vector space under the same operations. Equivalently, $W$ is a subspace if:
1. The zero vector of $V$ is in $W$.
2. $W$ is **closed under addition**: $\mathbf{u}, \mathbf{v} \in W$ implies $\mathbf{u} + \mathbf{v} \in W$.
3. $W$ is **closed under scalar multiplication**: $\mathbf{v} \in W$ and any scalar $c \in \mathbb{F}$ implies $c\,\mathbf{v} \in W$.

**Example**  
- In $\mathbb{R}^3$, the $xy$-plane (all vectors $(x,y,0)$) forms a subspace.
- The set of all polynomials with even degree is a subspace of the space of polynomials (because 0 is even degree, sums and scalar multiples of even-degree polynomials stay in even degree).


## 2.3 Linear Dependence and Independence

A set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k\}$ is **linearly dependent** if there exist scalars $c_1, c_2, \ldots, c_k$, not all zero, such that
\[
c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \dots + c_k \mathbf{v}_k = \mathbf{0}.
\]
If the only solution is $c_1 = c_2 = \cdots = c_k = 0$, then $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ is **linearly independent**.

**Examples**  
- In $\mathbb{R}^2$, the vectors $\{(1,2), (2,4)\}$ are dependent because $(2,4) = 2 \cdot (1,2)$.
- In $\mathbb{R}^2$, the vectors $\{(1,0), (0,1)\}$ are independent (no scalar multiple of one equals the other).

---

## 2.4 Basis of a Vector Space

A **basis** of a vector space $V$ is a linearly independent set of vectors that **spans** $V$. To say that a set of vectors $\{\mathbf{b}_1, \ldots, \mathbf{b}_m\}$ spans $V$ means any vector $\mathbf{v} \in V$ can be written as:
\[
\mathbf{v} = c_1 \mathbf{b}_1 + c_2 \mathbf{b}_2 + \dots + c_m \mathbf{b}_m
\]
for some scalars $c_1, \dots, c_m$.

**Key Points**  
- Basis vectors are linearly independent.
- Every vector in $V$ can be expressed as a linear combination of the basis vectors.
- Once a basis is chosen, every vector in $V$ has a unique coordinate representation with respect to that basis.

---

## Code Example: Checking Linear Independence in $\mathbb{R}^3$

Below is a small Python snippet using NumPy to check if a set of three vectors in $\mathbb{R}^3$ is linearly independent. It does this by forming a matrix with the vectors as rows (or columns) and then computing its rank.

```python
import numpy as np

def check_linear_independence_3d(v1, v2, v3):
    """
    Checks if v1, v2, v3 in R^3 are linearly independent.
    v1, v2, v3: tuples/lists of length 3
    Returns True if linearly independent, else False.
    """
    # Form a 3x3 matrix using the vectors as rows
    A = np.array([v1, v2, v3], dtype=float)
    # Compute the rank
    rank_A = np.linalg.matrix_rank(A)
    # If the rank is 3, the vectors are linearly independent
    return rank_A == 3

# Example usage
v1 = (1, 0, 2)
v2 = (0, 1, 3)
v3 = (1, 1, 5)  # (1,1,5) = (1,0,2) + (0,1,3)?
is_independent = check_linear_independence_3d(v1, v2, v3)
print("Are v1, v2, v3 linearly independent?", is_independent)
```

## Practice Exercises

1. **Subspace Check**  
   Show that the set of all $2 \times 2$ diagonal matrices forms a subspace of the space of all $2 \times 2$ matrices (under standard matrix addition and scalar multiplication). Explicitly verify closure properties and the zero vector condition.

2. **Linear Dependence Example**  
   In $\mathbb{R}^2$, consider vectors $\mathbf{v}_1 = (2,6)$ and $\mathbf{v}_2 = (1,3)$. Show that these vectors are linearly dependent.  
   Find scalars $c_1, c_2$ (not both zero) to prove it.

3. **Constructing a Basis**  
   Find a basis for the vector space spanned by $\{(1,1,0), (2,2,0), (0,0,1)\}$ in $\mathbb{R}^3$. Explain each step clearly.

---

## End-of-Chapter Question

**Q1.** State why every subspace must contain the zero vector of the parent space. Additionally, explain how the concept of linear independence is used to determine a basis for a given subspace.
