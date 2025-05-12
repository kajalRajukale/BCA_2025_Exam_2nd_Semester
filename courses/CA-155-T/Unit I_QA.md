# Unit I: Systems of Linear Equations and Matrices - Questions and Answers

### 1. Row Echelon Form and Reduced Row Echelon Form
1. **What is Row Echelon Form (REF)?**  
   A matrix is in REF if all nonzero rows are above rows of all zeros, and each leading entry of a row is to the right of the leading entry of the row above it.

2. **What is Reduced Row Echelon Form (RREF)?**  
   A matrix is in RREF if it satisfies the REF criteria and all leading entries are 1, with each leading 1 being the only nonzero entry in its column.

3. **Write a Python function to convert a matrix to REF.**
   ```python
   import numpy as np

   def to_ref(matrix):
       mat = np.array(matrix, dtype=float)
       rows, cols = mat.shape
       for i in range(rows):
           if mat[i, i] == 0:
               for j in range(i + 1, rows):
                   if mat[j, i] != 0:
                       mat[[i, j]] = mat[[j, i]]
                       break
           mat[i] = mat[i] / mat[i, i]
           for j in range(i + 1, rows):
               mat[j] -= mat[j, i] * mat[i]
       return mat

   # Example usage
   matrix = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
   print(to_ref(matrix))
   ```

---

### 2. Rank of a Matrix
4. **What is the rank of a matrix?**  
   The rank of a matrix is the number of leading 1s (pivots) in its RREF or the maximum number of linearly independent rows or columns.

5. **How do you find the rank of a matrix using REF?**  
   Convert the matrix to REF and count the number of nonzero rows.

6. **Write a Python function to calculate the rank of a matrix.**
   ```python
   def matrix_rank(matrix):
       ref_matrix = to_ref(matrix)
       rank = sum([1 for row in ref_matrix if any(row)])
       return rank

   # Example usage
   matrix = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
   print("Rank:", matrix_rank(matrix))
   ```

---

### 3. System of Linear Equations
7. **What is a system of linear equations?**  
   A system of linear equations is a set of equations where each equation is linear in the unknowns.

8. **How can a system of linear equations be represented in matrix form?**  
   A system can be written as \( A\mathbf{x} = \mathbf{b} \), where \( A \) is the coefficient matrix, \( \mathbf{x} \) is the vector of unknowns, and \( \mathbf{b} \) is the constant vector.

9. **Write a Python function to solve a system of linear equations using NumPy.**
   ```python
   def solve_linear_system(A, b):
       A = np.array(A, dtype=float)
       b = np.array(b, dtype=float)
       return np.linalg.solve(A, b)

   # Example usage
   A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
   b = [8, -11, -3]
   print("Solution:", solve_linear_system(A, b))
   ```

---

### 4. Consistency of Systems
10. **What is a consistent system of linear equations?**  
    A system is consistent if it has at least one solution.

11. **What is the condition for consistency of a non-homogeneous system?**  
    A non-homogeneous system \( A\mathbf{x} = \mathbf{b} \) is consistent if \( \text{rank}(A) = \text{rank}([A|\mathbf{b}]) \), where \( [A|\mathbf{b}] \) is the augmented matrix.

12. **Write a Python function to check the consistency of a system.**
    ```python
    def is_consistent(A, b):
        augmented_matrix = np.hstack((A, np.array(b).reshape(-1, 1)))
        return matrix_rank(A) == matrix_rank(augmented_matrix)

    # Example usage
    A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    b = [8, -11, -3]
    print("Is consistent:", is_consistent(A, b))
    ```

---

### 5. Gauss Elimination and Gauss-Jordan Elimination
13. **What is Gauss Elimination?**  
    Gauss Elimination is a method to solve a system of linear equations by converting the matrix to an upper triangular form and then performing back-substitution.

14. **What is Gauss-Jordan Elimination?**  
    Gauss-Jordan Elimination extends Gauss Elimination by reducing the matrix to RREF, eliminating the need for back-substitution.

15. **Write a Python function to solve a system using Gauss Elimination.**
    ```python
    def gauss_elimination(A, b):
        A = np.array(A, dtype=float)
        b = np.array(b, dtype=float)
        n = len(A)

        for i in range(n):
            for j in range(i + 1, n):
                factor = A[j, i] / A[i, i]
                A[j] -= factor * A[i]
                b[j] -= factor * b[i]

        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
        return x

    # Example usage
    A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    b = [8, -11, -3]
    print("Solution:", gauss_elimination(A, b))
    ```

---

### Practice Problems
16. **REF and RREF Conversion**  
    Convert the following matrix to REF and RREF:
    $$
    \begin{pmatrix}
    1 & 2 & 1 \\
    2 & 4 & -1 \\
    -1 & -2 & 3
    \end{pmatrix}.
    $$

17. **Rank and Consistency**  
    Determine the rank of:
    $$
    A = \begin{pmatrix}
    3 & 1 & 2 \\
    6 & 2 & 4 \\
    0 & 1 & 1
    \end{pmatrix}.
    $$
    Append a vector \( \mathbf{b} \) of your choice. Check if the system \( A\mathbf{x} = \mathbf{b} \) is consistent.

18. **Gauss Elimination**  
    Solve the system:
    $$
    \begin{cases}
    x + 2y - z = 1, \\
    2x + 5y + z = 5, \\
    3x + 8y + 2z = 9
    \end{cases}.
    $$

19. **Homogeneous System**  
    Formulate a \( 3 \times 3 \) homogeneous system with infinitely many solutions. Show the RREF form and describe the solution set.

---

(Continue with similar Q&A format for remaining questions up to 50.)
