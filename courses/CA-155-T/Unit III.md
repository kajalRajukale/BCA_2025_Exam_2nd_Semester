### Unit III: Vector Spaces - II (06 Hrs)

3.1 Dimension of a vector space
3.2 Row Space, Column Space, and Null Space of a matrix
3.3 Definition: Rank and Nullity

---

# Chapter 3: Vector Spaces – II

Building on the basics of vector spaces, this chapter delves into the notion of dimension and explores row space, column space, null space, rank, and nullity for matrices.

---

## 3.1 Dimension of a Vector Space

- **Definition of Dimension:**  
  The **dimension** of a finite-dimensional vector space $V$ is the number of vectors in any basis of $V$.

  **Examples**

  - $\dim(\mathbb{R}^n) = n$.
  - $\dim\bigl(\text{the space of polynomials of degree} \leq n\bigr) = n+1$.

- **Key Property:**  
  If $\{\mathbf{v}\_1, \mathbf{v}\_2, \dots, \mathbf{v}\_k\}$ is a basis for $V$, then every other basis of $V$ must also contain exactly $k$ vectors.

---

## 3.2 Row Space, Column Space, and Null Space of a Matrix

Consider a matrix $A$ of size $m \times n$.

1. **Row Space (RS)**  
   The **row space** of $A$ is the set of all linear combinations of the row vectors of $A$. Equivalently, if you think of each row as a vector in $\mathbb{R}^n$, the row space is the subspace spanned by these row vectors.

2. **Column Space (CS)**  
   The **column space** of $A$ is the set of all linear combinations of the column vectors of $A$. Each column is considered a vector in $\mathbb{R}^m$.

   **Note:** The dimension of the row space always equals the dimension of the column space (this common dimension is the rank of $A$).

3. **Null Space (or Kernel, NS)**  
   The **null space** (sometimes called the **kernel**) of $A$ is the set of all vectors $\mathbf{x}$ such that
   $$
   A \mathbf{x} = \mathbf{0}.
   $$
   It represents all solutions to the homogeneous system $A\mathbf{x} = \mathbf{0}$.

---

## 3.3 Rank and Nullity

1. **Rank of a Matrix**  
   The **rank** of $A$ is the dimension of its column space (which is also equal to the dimension of its row space). It corresponds to the number of leading pivots when $A$ is transformed into its row echelon form (REF or RREF).

2. **Nullity of a Matrix**  
   The **nullity** of $A$ is the dimension of its null space. It tells you how many free variables you have when solving $A\mathbf{x} = \mathbf{0}$.

3. **Rank-Nullity Theorem**  
   For an $m \times n$ matrix $A$,

   $$
   \text{rank}(A) + \text{nullity}(A) = n.
   $$

   This theorem is an important link between the row/column space (rank) and the null space (nullity).

---

## Code Example: Finding Row Space, Column Space, and Null Space

Below is a Python snippet (using Sympy) to compute the row space, column space, and null space.

```python
import sympy

# Define the matrix A as a list of lists
A_list = [
    [2, 1, 0],
    [0, 1, 3],
    [1, 0, 0]
]
A = sympy.Matrix(A_list)

# Row Space
row_space = A.rowspace()
print("Row Space:")
for vec in row_space:
    print(vec)

# Column Space
col_space = A.columnspace()
print("\nColumn Space:")
for vec in col_space:
    print(vec)

# Null Space
null_space = A.nullspace()
print("\nNull Space (Kernel):")
for vec in null_space:
    print(vec)

# Rank and Nullity
print("\nRank of A:", A.rank())
print("Nullity of A:", A.shape[1] - A.rank())
```

### Explanation

- **rowspace()** returns a list of row vectors (in reduced form) that form a basis for the row space.
- **columnspace()** returns a list of column vectors that form a basis for the column space.
- **nullspace()** provides a basis for all vectors $\mathbf{x}$ where $A\mathbf{x} = 0$.

### Practice Exercises

1. **Dimension and Rank**  
   Take a $3 \times 3$ matrix of rank 2. Show how you identify the rank by reducing it to row echelon form. Indicate which rows (or columns) are linearly independent.

2. **Row Space vs. Column Space**  
   Give an example of a $2 \times 3$ matrix. Compute its row space and column space. Confirm they have the same dimension. Briefly explain why this is so.

3. **Nullity and Free Variables**  
   Construct a $4 \times 3$ matrix where the nullity is 2. Solve the homogeneous system $A\mathbf{x} = 0$ and interpret the free variables in your solution.

### End-of-Chapter Question

**Q1.** Provide a concise definition of rank and nullity for a given matrix $A$. Then restate the rank-nullity theorem in your own words, and briefly discuss its significance in solving linear systems.
