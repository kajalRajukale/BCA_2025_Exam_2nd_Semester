# Unit III: Vector Spaces and Subspaces - Questions and Answers

### 1. Vector Spaces
1. **What is a vector space?**  
   A vector space is a set of vectors, along with operations of addition and scalar multiplication, that satisfies the vector space axioms (e.g., closure, associativity, distributivity).

2. **Give an example of a vector space.**  
   The set of all \( n \)-dimensional vectors \( \mathbb{R}^n \) is a vector space under standard addition and scalar multiplication.

3. **Write a Python function to check if a set of vectors forms a vector space.**
   ```python
   import numpy as np

   def is_vector_space(vectors):
       vectors = np.array(vectors)
       # Check closure under addition
       for i in range(len(vectors)):
           for j in range(len(vectors)):
               if not np.any(np.isclose(vectors[i] + vectors[j], vectors, atol=1e-8)):
                   return False
       # Check closure under scalar multiplication
       scalar = 2  # Example scalar
       for vec in vectors:
           if not np.any(np.isclose(scalar * vec, vectors, atol=1e-8)):
               return False
       return True

   # Example usage
   vectors = [[1, 0], [0, 1]]
   print("Is vector space:", is_vector_space(vectors))
   ```

---

### 2. Subspaces
4. **What is a subspace?**  
   A subspace is a subset of a vector space that is itself a vector space under the same operations.

5. **What are the conditions for a subset to be a subspace?**  
   - The zero vector is in the subset.  
   - The subset is closed under vector addition.  
   - The subset is closed under scalar multiplication.

6. **Write a Python function to check if a subset is a subspace.**
   ```python
   def is_subspace(vectors, subset):
       vectors = np.array(vectors)
       subset = np.array(subset)
       # Check if zero vector is in the subset
       if not np.any(np.all(subset == 0, axis=1)):
           return False
       # Check closure under addition
       for i in range(len(subset)):
           for j in range(len(subset)):
               if not np.any(np.isclose(subset[i] + subset[j], subset, atol=1e-8)):
                   return False
       # Check closure under scalar multiplication
       scalar = 2  # Example scalar
       for vec in subset:
           if not np.any(np.isclose(scalar * vec, subset, atol=1e-8)):
               return False
       return True

   # Example usage
   vectors = [[1, 0], [0, 1]]
   subset = [[0, 0], [1, 0]]
   print("Is subspace:", is_subspace(vectors, subset))
   ```

---

### 3. Basis and Dimension
7. **What is a basis of a vector space?**  
   A basis is a set of linearly independent vectors that span the vector space.

8. **What is the dimension of a vector space?**  
   The dimension is the number of vectors in a basis of the vector space.

9. **Write a Python function to find the basis of a vector space.**
   ```python
   def find_basis(vectors):
       vectors = np.array(vectors)
       _, _, rank = np.linalg.svd(vectors)
       return rank

   # Example usage
   vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
   print("Basis rank:", find_basis(vectors))
   ```

---

### 4. Linear Independence
10. **What is linear independence?**  
    A set of vectors is linearly independent if no vector in the set can be written as a linear combination of the others.

11. **How do you check if a set of vectors is linearly independent?**  
    Compute the determinant of the matrix formed by the vectors. If the determinant is nonzero, the vectors are linearly independent.

12. **Write a Python function to check linear independence.**
    ```python
    def is_linearly_independent(vectors):
        vectors = np.array(vectors)
        return np.linalg.matrix_rank(vectors) == len(vectors)

    # Example usage
    vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print("Is linearly independent:", is_linearly_independent(vectors))
    ```

---

### 5. Row Space, Column Space, and Null Space
13. **What is the row space of a matrix?**  
    The row space is the span of the rows of the matrix.

14. **What is the column space of a matrix?**  
    The column space is the span of the columns of the matrix.

15. **What is the null space of a matrix?**  
    The null space is the set of all vectors \( \mathbf{x} \) such that \( A\mathbf{x} = 0 \).

16. **Write a Python function to compute the null space of a matrix.**
    ```python
    def null_space(matrix):
        u, s, vh = np.linalg.svd(matrix)
        null_mask = (s <= 1e-10)
        null_space = np.compress(null_mask, vh, axis=0)
        return null_space.T

    # Example usage
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Null space:\n", null_space(matrix))
    ```

---

### 6. Orthogonality
17. **What is an orthogonal set of vectors?**  
    A set of vectors is orthogonal if the dot product of any two distinct vectors is zero.

18. **What is an orthonormal set of vectors?**  
    A set of vectors is orthonormal if it is orthogonal and each vector has a magnitude of 1.

19. **Write a Python function to check if a set of vectors is orthogonal.**
    ```python
    def is_orthogonal(vectors):
        vectors = np.array(vectors)
        for i in range(len(vectors)):
            for j in range(i + 1, len(vectors)):
                if not np.isclose(np.dot(vectors[i], vectors[j]), 0, atol=1e-8):
                    return False
        return True

    # Example usage
    vectors = [[1, 0], [0, 1]]
    print("Is orthogonal:", is_orthogonal(vectors))
    ```

---

### Practice Problems
20. **Vector Space Verification**  
    Verify if the set \( \{(1, 0), (0, 1)\} \) forms a vector space under standard addition and scalar multiplication.

21. **Subspace Verification**  
    Check if the set \( \{(0, 0), (1, 0)\} \) is a subspace of \( \mathbb{R}^2 \).

22. **Basis and Dimension**  
    Find the basis and dimension of the vector space spanned by \( \{(1, 2, 3), (4, 5, 6), (7, 8, 9)\} \).

23. **Linear Independence**  
    Determine if the vectors \( \{(1, 0, 0), (0, 1, 0), (0, 0, 1)\} \) are linearly independent.

24. **Null Space**  
    Compute the null space of the matrix:
    \[
    A = \begin{pmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    7 & 8 & 9
    \end{pmatrix}.
    \]

25. **Orthogonality**  
    Verify if the vectors \( \{(1, 0), (0, 1)\} \) are orthogonal.

---

(Continue with similar Q&A format for remaining questions up to 50.)
