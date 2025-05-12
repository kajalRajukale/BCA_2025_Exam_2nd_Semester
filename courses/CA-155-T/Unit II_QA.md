# Unit II: Determinants and Eigenvalues - Questions and Answers

### 1. Determinants
1. **What is a determinant?**  
   A determinant is a scalar value that can be computed from the elements of a square matrix and provides important properties of the matrix, such as invertibility.

2. **What is the determinant of a 2x2 matrix?**  
   For a matrix \( A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \), the determinant is:  
   \[
   \text{det}(A) = ad - bc
   \]

3. **Write a Python function to calculate the determinant of a 2x2 matrix.**
   ```python
   def determinant_2x2(matrix):
       return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

   # Example usage
   matrix = [[3, 2], [1, 4]]
   print("Determinant:", determinant_2x2(matrix))
   ```

4. **What is the determinant of a 3x3 matrix?**  
   For a matrix \( A = \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix} \), the determinant is:  
   \[
   \text{det}(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
   \]

5. **Write a Python function to calculate the determinant of a 3x3 matrix.**
   ```python
   def determinant_3x3(matrix):
       a, b, c = matrix[0]
       d, e, f = matrix[1]
       g, h, i = matrix[2]
       return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

   # Example usage
   matrix = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
   print("Determinant:", determinant_3x3(matrix))
   ```

---

### 2. Properties of Determinants
6. **What happens to the determinant if two rows of a matrix are swapped?**  
   The determinant changes its sign.

7. **What is the determinant of a matrix with a row or column of zeros?**  
   The determinant is zero.

8. **What is the effect of multiplying a row of a matrix by a scalar on the determinant?**  
   The determinant is multiplied by the same scalar.

9. **Write a Python function to check if a matrix is singular.**
   ```python
   import numpy as np

   def is_singular(matrix):
       return np.linalg.det(matrix) == 0

   # Example usage
   matrix = [[1, 2], [2, 4]]
   print("Is singular:", is_singular(matrix))
   ```

---

### 3. Eigenvalues and Eigenvectors
10. **What are eigenvalues and eigenvectors?**  
    For a square matrix \( A \), an eigenvector \( \mathbf{v} \) and eigenvalue \( \lambda \) satisfy:  
    \[
    A\mathbf{v} = \lambda\mathbf{v}
    \]

11. **How do you compute eigenvalues of a matrix?**  
    Solve the characteristic equation \( \text{det}(A - \lambda I) = 0 \), where \( I \) is the identity matrix.

12. **Write a Python function to compute eigenvalues and eigenvectors.**
    ```python
    import numpy as np

    def compute_eigen(matrix):
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        return eigenvalues, eigenvectors

    # Example usage
    matrix = [[4, -2], [1, 1]]
    eigenvalues, eigenvectors = compute_eigen(matrix)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)
    ```

---

### 4. Diagonalization
13. **What is diagonalization?**  
    A matrix \( A \) is diagonalizable if it can be written as \( A = PDP^{-1} \), where \( P \) is the matrix of eigenvectors and \( D \) is the diagonal matrix of eigenvalues.

14. **Write a Python function to diagonalize a matrix.**
    ```python
    def diagonalize(matrix):
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        P = eigenvectors
        D = np.diag(eigenvalues)
        P_inv = np.linalg.inv(P)
        return P, D, P_inv

    # Example usage
    matrix = [[4, -2], [1, 1]]
    P, D, P_inv = diagonalize(matrix)
    print("P:\n", P)
    print("D:\n", D)
    print("P_inv:\n", P_inv)
    ```

---

### 5. Applications of Determinants and Eigenvalues
15. **How are determinants used to check matrix invertibility?**  
    A matrix is invertible if and only if its determinant is nonzero.

16. **What is the significance of eigenvalues in stability analysis?**  
    Eigenvalues determine the stability of a system. For example, in dynamic systems, if all eigenvalues have negative real parts, the system is stable.

17. **Write a Python function to compute the inverse of a matrix using determinants.**
    ```python
    def inverse_matrix(matrix):
        det = np.linalg.det(matrix)
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        return np.linalg.inv(matrix)

    # Example usage
    matrix = [[4, 7], [2, 6]]
    print("Inverse:\n", inverse_matrix(matrix))
    ```

---

### Practice Problems
18. **Determinant Calculation**  
    Compute the determinant of the following matrix:
    \[
    A = \begin{pmatrix}
    2 & 3 & 1 \\
    4 & 1 & -3 \\
    -1 & 2 & 5
    \end{pmatrix}.
    \]

19. **Eigenvalues and Eigenvectors**  
    Find the eigenvalues and eigenvectors of:
    \[
    A = \begin{pmatrix}
    6 & 2 \\
    2 & 3
    \end{pmatrix}.
    \]

20. **Diagonalization**  
    Diagonalize the matrix:
    \[
    A = \begin{pmatrix}
    5 & 4 \\
    1 & 2
    \end{pmatrix}.
    \]

21. **Invertibility Check**  
    Determine if the following matrix is invertible:
    \[
    A = \begin{pmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    7 & 8 & 9
    \end{pmatrix}.
    \]

22. **Stability Analysis**  
    Analyze the stability of the system with the matrix:
    \[
    A = \begin{pmatrix}
    -2 & 1 \\
    0 & -3
    \end{pmatrix}.
    \]

---

(Continue with similar Q&A format for remaining questions up to 50.)
