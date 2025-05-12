# Unit V: Applications of Linear Algebra - Questions and Answers

### 1. Linear Algebra in Computer Graphics
1. **How is linear algebra used in computer graphics?**  
   Linear algebra is used in computer graphics for transformations such as scaling, rotation, translation, and projection of objects.

2. **What is a transformation matrix?**  
   A transformation matrix is a matrix used to perform linear transformations on vectors, such as scaling, rotation, or translation.

3. **Write a Python function to perform 2D rotation of a point.**
   ```python
   import numpy as np

   def rotate_point(point, angle):
       angle_rad = np.radians(angle)
       rotation_matrix = np.array([
           [np.cos(angle_rad), -np.sin(angle_rad)],
           [np.sin(angle_rad), np.cos(angle_rad)]
       ])
       return np.dot(rotation_matrix, point)

   # Example usage
   point = np.array([1, 0])
   rotated_point = rotate_point(point, 90)
   print("Rotated Point:", rotated_point)
   ```

---

### 2. Linear Algebra in Machine Learning
4. **How is linear algebra used in machine learning?**  
   Linear algebra is used in machine learning for operations such as matrix multiplication, gradient computation, and optimization.

5. **What is the role of eigenvalues in Principal Component Analysis (PCA)?**  
   Eigenvalues represent the variance captured by each principal component in PCA.

6. **Write a Python function to compute the principal components of a dataset.**
   ```python
   def principal_components(data):
       data_mean = np.mean(data, axis=0)
       centered_data = data - data_mean
       covariance_matrix = np.cov(centered_data, rowvar=False)
       eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
       return eigenvalues, eigenvectors

   # Example usage
   data = np.array([[2.5, 2.4], [0.5, 0.7], [2.2, 2.9], [1.9, 2.2], [3.1, 3.0]])
   eigenvalues, eigenvectors = principal_components(data)
   print("Eigenvalues:", eigenvalues)
   print("Eigenvectors:\n", eigenvectors)
   ```

---

### 3. Linear Algebra in Cryptography
7. **How is linear algebra used in cryptography?**  
   Linear algebra is used in cryptography for encoding and decoding messages using matrix transformations.

8. **What is the Hill cipher?**  
   The Hill cipher is a polygraphic substitution cipher that uses matrix multiplication to encrypt and decrypt messages.

9. **Write a Python function to encrypt a message using the Hill cipher.**
   ```python
   def hill_encrypt(message, key):
       message_vector = np.array([ord(char) - ord('A') for char in message])
       key_matrix = np.array(key)
       encrypted_vector = np.dot(key_matrix, message_vector) % 26
       encrypted_message = ''.join(chr(int(num) + ord('A')) for num in encrypted_vector)
       return encrypted_message

   # Example usage
   key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
   message = "ACT"
   encrypted_message = hill_encrypt(message, key)
   print("Encrypted Message:", encrypted_message)
   ```

---

### 4. Linear Algebra in Network Analysis
10. **How is linear algebra used in network analysis?**  
    Linear algebra is used in network analysis to compute centrality measures, such as eigenvector centrality, which identifies important nodes in a network.

11. **What is the adjacency matrix of a graph?**  
    The adjacency matrix is a square matrix used to represent a graph, where each element indicates whether pairs of vertices are adjacent.

12. **Write a Python function to compute eigenvector centrality of a graph.**
    ```python
    def eigenvector_centrality(adjacency_matrix):
        eigenvalues, eigenvectors = np.linalg.eig(adjacency_matrix)
        max_index = np.argmax(eigenvalues)
        centrality = eigenvectors[:, max_index]
        return centrality / np.sum(centrality)

    # Example usage
    adjacency_matrix = np.array([
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ])
    centrality = eigenvector_centrality(adjacency_matrix)
    print("Eigenvector Centrality:", centrality)
    ```

---

### 5. Linear Algebra in Optimization
13. **How is linear algebra used in optimization problems?**  
    Linear algebra is used to solve systems of linear equations and inequalities in optimization problems, such as linear programming.

14. **What is the simplex method?**  
    The simplex method is an algorithm for solving linear programming problems by moving along the edges of the feasible region to find the optimal solution.

15. **Write a Python function to solve a linear programming problem using SciPy.**
    ```python
    from scipy.optimize import linprog

    def solve_linear_program(c, A, b):
        result = linprog(c, A_ub=A, b_ub=b, method='highs')
        return result.x, result.fun

    # Example usage
    c = [-1, -2]  # Coefficients of the objective function
    A = [[2, 1], [1, 1], [1, 0]]
    b = [20, 16, 8]
    solution, objective_value = solve_linear_program(c, A, b)
    print("Solution:", solution)
    print("Objective Value:", objective_value)
    ```

---

### Practice Problems
16. **2D Transformation**  
    Rotate the point \( (1, 0) \) by 45 degrees using a transformation matrix.

17. **Principal Component Analysis**  
    Compute the principal components of the dataset:
    \[
    \text{Data} = \begin{pmatrix}
    2.5 & 2.4 \\
    0.5 & 0.7 \\
    2.2 & 2.9 \\
    1.9 & 2.2 \\
    3.1 & 3.0
    \end{pmatrix}.
    \]

18. **Hill Cipher**  
    Encrypt the message "HELLO" using the Hill cipher with the key:
    \[
    \text{Key} = \begin{pmatrix}
    6 & 24 & 1 \\
    13 & 16 & 10 \\
    20 & 17 & 15
    \end{pmatrix}.
    \]

19. **Network Analysis**  
    Compute the eigenvector centrality of the graph represented by the adjacency matrix:
    \[
    \text{Adjacency Matrix} = \begin{pmatrix}
    0 & 1 & 1 \\
    1 & 0 & 1 \\
    1 & 1 & 0
    \end{pmatrix}.
    \]

20. **Linear Programming**  
    Solve the linear programming problem:
    \[
    \text{Maximize } z = x_1 + 2x_2
    \]
    Subject to:
    \[
    2x_1 + x_2 \leq 20, \quad x_1 + x_2 \leq 16, \quad x_1 \leq 8.
    \]

---

(Continue with similar Q&A format for remaining questions up to 50.)
