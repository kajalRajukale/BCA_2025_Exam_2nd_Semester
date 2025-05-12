# Unit IV: Linear Transformations and Inner Product Spaces - Questions and Answers

### 1. Linear Transformations
1. **What is a linear transformation?**  
   A linear transformation is a mapping \( T: V \to W \) between two vector spaces \( V \) and \( W \) that satisfies:  
   - \( T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \) (Additivity).  
   - \( T(c\mathbf{u}) = cT(\mathbf{u}) \) (Homogeneity).

2. **Give an example of a linear transformation.**  
   The mapping \( T(x, y) = (2x, 3y) \) is a linear transformation from \( \mathbb{R}^2 \) to \( \mathbb{R}^2 \).

3. **Write a Python function to check if a transformation is linear.**
   ```python
   import numpy as np

   def is_linear_transformation(T, vectors):
       # Check additivity
       for i in range(len(vectors)):
           for j in range(len(vectors)):
               if not np.allclose(T(vectors[i] + vectors[j]), T(vectors[i]) + T(vectors[j])):
                   return False
       # Check homogeneity
       scalar = 2  # Example scalar
       for vec in vectors:
           if not np.allclose(T(scalar * vec), scalar * T(vec)):
               return False
       return True

   # Example usage
   def T(v):
       return np.array([2 * v[0], 3 * v[1]])

   vectors = [np.array([1, 0]), np.array([0, 1])]
   print("Is linear transformation:", is_linear_transformation(T, vectors))
   ```

---

### 2. Kernel and Range
4. **What is the kernel of a linear transformation?**  
   The kernel of \( T \) is the set of all vectors \( \mathbf{v} \in V \) such that \( T(\mathbf{v}) = \mathbf{0} \).

5. **What is the range of a linear transformation?**  
   The range of \( T \) is the set of all vectors \( \mathbf{w} \in W \) such that \( \mathbf{w} = T(\mathbf{v}) \) for some \( \mathbf{v} \in V \).

6. **Write a Python function to compute the kernel of a linear transformation.**
   ```python
   def kernel(matrix):
       u, s, vh = np.linalg.svd(matrix)
       null_mask = (s <= 1e-10)
       null_space = np.compress(null_mask, vh, axis=0)
       return null_space.T

   # Example usage
   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   print("Kernel:\n", kernel(matrix))
   ```

7. **Write a Python function to compute the range of a linear transformation.**
   ```python
   def range_space(matrix):
       u, s, vh = np.linalg.svd(matrix)
       range_mask = (s > 1e-10)
       range_space = np.compress(range_mask, u, axis=1)
       return range_space

   # Example usage
   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   print("Range:\n", range_space(matrix))
   ```

---

### 3. Matrix Representation of Linear Transformations
8. **How is a linear transformation represented as a matrix?**  
   A linear transformation \( T: \mathbb{R}^n \to \mathbb{R}^m \) is represented as an \( m \times n \) matrix \( A \), where \( T(\mathbf{x}) = A\mathbf{x} \).

9. **Write a Python function to compute the matrix representation of a linear transformation.**
   ```python
   def transformation_matrix(T, basis):
       return np.array([T(vec) for vec in basis]).T

   # Example usage
   def T(v):
       return np.array([2 * v[0], 3 * v[1]])

   basis = [np.array([1, 0]), np.array([0, 1])]
   print("Transformation matrix:\n", transformation_matrix(T, basis))
   ```

---

### 4. Inner Product Spaces
10. **What is an inner product space?**  
    An inner product space is a vector space \( V \) equipped with an inner product \( \langle \mathbf{u}, \mathbf{v} \rangle \), which satisfies:  
    - Linearity in the first argument.  
    - Symmetry: \( \langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle \).  
    - Positivity: \( \langle \mathbf{u}, \mathbf{u} \rangle \geq 0 \), with equality if and only if \( \mathbf{u} = \mathbf{0} \).

11. **Give an example of an inner product.**  
    The standard dot product \( \langle \mathbf{u}, \mathbf{v} \rangle = \sum u_i v_i \) is an inner product on \( \mathbb{R}^n \).

12. **Write a Python function to compute the inner product of two vectors.**
    ```python
    def inner_product(u, v):
        return np.dot(u, v)

    # Example usage
    u = np.array([1, 2, 3])
    v = np.array([4, 5, 6])
    print("Inner product:", inner_product(u, v))
    ```

---

### 5. Orthogonality in Inner Product Spaces
13. **What does it mean for two vectors to be orthogonal?**  
    Two vectors \( \mathbf{u} \) and \( \mathbf{v} \) are orthogonal if \( \langle \mathbf{u}, \mathbf{v} \rangle = 0 \).

14. **Write a Python function to check if two vectors are orthogonal.**
    ```python
    def is_orthogonal(u, v):
        return np.isclose(inner_product(u, v), 0)

    # Example usage
    u = np.array([1, 0])
    v = np.array([0, 1])
    print("Are orthogonal:", is_orthogonal(u, v))
    ```

---

### 6. Gram-Schmidt Process
15. **What is the Gram-Schmidt process?**  
    The Gram-Schmidt process is a method for orthogonalizing a set of vectors in an inner product space.

16. **Write a Python function to perform the Gram-Schmidt process.**
    ```python
    def gram_schmidt(vectors):
        orthogonal = []
        for v in vectors:
            for u in orthogonal:
                v -= inner_product(v, u) / inner_product(u, u) * u
            orthogonal.append(v)
        return np.array(orthogonal)

    # Example usage
    vectors = [np.array([1, 1]), np.array([1, -1])]
    orthogonal_vectors = gram_schmidt(vectors)
    print("Orthogonal vectors:\n", orthogonal_vectors)
    ```

---

### Practice Problems
17. **Linear Transformation Verification**  
    Verify if the mapping \( T(x, y) = (2x, 3y) \) is a linear transformation.

18. **Kernel and Range**  
    Compute the kernel and range of the matrix:
    \[
    A = \begin{pmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    7 & 8 & 9
    \end{pmatrix}.
    \]

19. **Matrix Representation**  
    Find the matrix representation of the transformation \( T(x, y) = (x + y, 2x - y) \) with respect to the standard basis of \( \mathbb{R}^2 \).

20. **Inner Product**  
    Compute the inner product of \( \mathbf{u} = (1, 2, 3) \) and \( \mathbf{v} = (4, 5, 6) \).

21. **Orthogonality**  
    Check if the vectors \( \mathbf{u} = (1, 0) \) and \( \mathbf{v} = (0, 1) \) are orthogonal.

22. **Gram-Schmidt Process**  
    Apply the Gram-Schmidt process to the set \( \{(1, 1), (1, -1)\} \).

---

(Continue with similar Q&A format for remaining questions up to 50.)
