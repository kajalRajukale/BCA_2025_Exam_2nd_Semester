### Unit I: Systems of Linear Equations and Matrices (06 Hrs)

1.1 Row echelon form of a matrix, reduced row echelon form of a matrix  
1.2 Definition of rank of a matrix using row echelon or row reduced echelon form  
1.3 System of linear equations - Introduction, matrix form of linear system, definition of row equivalent matrices  
1.4 Consistency of homogeneous and non-homogeneous system of linear equations using rank, condition for consistency  
1.5 Solution of System of Equations: Gauss elimination and Gauss-Jordan elimination method, examples

---

# Chapter 1: Systems of Linear Equations and Matrices

This chapter focuses on the fundamentals of solving systems of linear equations using matrix techniques. It covers concepts such as row echelon forms, the rank of a matrix, determining the consistency of linear systems, and applying Gauss and Gauss-Jordan elimination methods.

---

## 1.1 Row Echelon Form and Reduced Row Echelon Form

### Row Echelon Form (REF)

A matrix is in **Row Echelon Form (REF)** if:

1. All nonzero rows are above any rows of all zeros.
2. Each leading (nonzero) entry of a row is to the right of the leading entry of the row above it.
3. All entries in a column below a leading entry are zeros.

**Example**

$$
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 4 \\
0 & 0 & 5
\end{pmatrix}
$$

All leading entries move diagonally to the right and zeros appear below each leading entry.

### Reduced Row Echelon Form (RREF)

A matrix is in **Reduced Row Echelon Form (RREF)** if, in addition to the REF criteria:

1. All leading entries are 1.
2. Each leading 1 is the only nonzero entry in its column.

**Example**

$$
\begin{pmatrix}
1 & 0 & 2 \\
0 & 1 & -1 \\
0 & 0 & 1
\end{pmatrix}
$$

Each pivot is 1, and it is the only nonzero entry in its column.

---

## 1.2 Definition of Rank of a Matrix

The **rank** of a matrix $A$ is the number of leading 1s (pivots) in its RREF. Equivalently, it is the maximum number of linearly independent rows (or columns) of $A$.

- **Key Point:** To find the rank of a matrix, you can convert it to its REF or RREF and count the nonzero rows (or the pivot positions).

---

## 1.3 System of Linear Equations: Introduction, Matrix Form, and Row-Equivalent Matrices

A system of linear equations can be written as:

$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2 \\
\quad\quad \vdots \\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m
\end{cases}
$$

Using matrices, this becomes:

$$
A\,\mathbf{x} = \mathbf{b}
$$

where $A$ is the $m \times n$ coefficient matrix, $ \mathbf{x} $ is the $n \times 1$ column vector of unknowns, and $\mathbf{b}$ is the $m \times 1$ column vector of constants.

- **Row-Equivalent Matrices:** Two matrices are **row-equivalent** if one can be transformed into the other using elementary row operations (swapping rows, scaling rows, adding multiples of one row to another).

---

## 1.4 Consistency of Homogeneous and Non-Homogeneous Systems

1. **Homogeneous System $(A\mathbf{x} = \mathbf{0})$:**

   - Always consistent (the trivial solution $\mathbf{x} = \mathbf{0}$ exists).
   - May have infinitely many solutions if the rank of $A$ is less than the number of unknowns.

2. **Non-Homogeneous System $(A\mathbf{x} = \mathbf{b})$:**
   - **Consistent** if $\text{rank}(A) = \text{rank}([A|\mathbf{b}])$.
   - **Inconsistent** if $\text{rank}(A) < \text{rank}([A|\mathbf{b}])$. (Here, $[A|\mathbf{b}]$ is the augmented matrix formed by appending $\mathbf{b}$ to $A$.)

---

## 1.5 Gauss Elimination and Gauss-Jordan Elimination

### Gauss Elimination

1. **Goal:** Convert the matrix to an upper-triangular form.
2. **Steps:**
   - Use elementary row operations to eliminate variables below each leading pivot.
   - Perform back-substitution to solve for unknowns.

**Illustrative Example**

$$
\begin{aligned}
&\text{System:} \\
&\begin{cases}
2x + y - z = 8 \\
-3x - y + 2z = -11 \\
-2x + y + 2z = -3
\end{cases}
\end{aligned}
$$

1. Form the augmented matrix:
   $$
   \left[\begin{array}{ccc|c}
   2 & 1 & -1 & 8 \\
   -3 & -1 & 2 & -11 \\
   -2 & 1 & 2 & -3
   \end{array}\right]
   $$
2. Perform row operations to reach an upper-triangular form.
3. Back-substitute to find $(x, y, z)$.

### Gauss-Jordan Elimination

1. **Goal:** Convert directly to RREF.
2. **Steps:**
   - Eliminate coefficients below and above each pivot, ending with each pivot = 1 and as the sole nonzero entry in that column.
3. This method removes the need for separate back-substitution.

---

## Example Code: Gauss Elimination in Python

```python
def gauss_elimination(A, b):
    """
    Solve A*x = b using Gauss Elimination.
    A: list of lists (coefficient matrix)
    b: list (constant terms)
    Returns: list (solution vector)
    """
    import copy

    # Make a copy to avoid mutating the original lists
    A = copy.deepcopy(A)
    b = copy.deepcopy(b)

    n = len(A)

    # Forward elimination
    for i in range(n):
        # Pivot
        pivot = A[i][i]
        if pivot == 0:
            raise ValueError("Zero pivot encountered! Cannot proceed.")

        for j in range(i+1, n):
            factor = A[j][i] / pivot
            # Update row j
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Back-substitution
    x = [0]*n
    for i in range(n-1, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += A[i][j] * x[j]
        x[i] = (b[i] - sum_ax) / A[i][i]

    return x

# Sample usage:
A_matrix = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]
b_vector = [8, -11, -3]

solutions = gauss_elimination(A_matrix, b_vector)
print("Solutions:", solutions)
```

### Explanation of Code

- **Forward Elimination:** Eliminates variables below each pivot to form an upper-triangular matrix.  
- **Back-Substitution:** Solves for variables from the last equation back to the first.

---

### Practice Problems

1. **REF and RREF Conversion**  
   Convert the following matrix to REF and then to RREF:

   $$
   \begin{pmatrix}
   1 & 2 & 1 \\
   2 & 4 & -1 \\
   -1 & -2 & 3
   \end{pmatrix}.
   $$

   State the pivot positions at each step.

2. **Rank and Consistency**  
   Determine the rank of:

   $$
   A = \begin{pmatrix}
   3 & 1 & 2 \\
   6 & 2 & 4 \\
   0 & 1 & 1
   \end{pmatrix}.
   $$

   Append a vector \(\mathbf{b}\) of your choice. Check if the system \(A\mathbf{x} = \mathbf{b}\) is consistent.

3. **Homogeneous System**  
   Formulate a \(3 \times 3\) homogeneous system with infinitely many solutions. Show the RREF form and describe the solution set.

4. **Gauss Elimination**  
   Solve the system:
   $$
   \begin{cases}
   x + 2y - z = 1, \\
   2x + 5y + z = 5, \\
   3x + 8y + 2z = 9
   \end{cases}
   $$
   
   Verify your answers by substituting back into the original equations.

