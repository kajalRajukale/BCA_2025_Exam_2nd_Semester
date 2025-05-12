
# Advanced C Programming - Questions and Answers

## Question 1: What is the purpose of the C Preprocessor?
**Answer:**  
The C Preprocessor modifies the source code before compilation by handling tasks like file inclusion, macro expansion, and conditional compilation.

---

## Question 2: What is the difference between `#include <file>` and `#include "file"`?
**Answer:**  
- `<file>`: Searches for the file in standard system directories.
- `"file"`: Searches for the file in the current directory first, then in system directories.

---

## Question 3: What is a macro in C?
**Answer:**  
A macro is a fragment of code defined using `#define` that is replaced by its definition during preprocessing.

---

## Question 4: How do you define a parameterized macro?
**Answer:**  
```c
#define SQUARE(x) ((x) * (x))
```

---

## Question 5: What is the difference between macros and functions?
**Answer:**  
- Macros are expanded at compile-time and are faster but lack type safety.
- Functions are compiled once, reusable, and type-safe.

---

## Question 6: What is the purpose of the `#ifdef` directive?
**Answer:**  
The `#ifdef` directive checks if a macro is defined and includes the code block if true.

---

## Question 7: How do you generate a compile-time error using the preprocessor?
**Answer:**  
Use the `#error` directive. Example:
```c
#error "This is a compile-time error."
```

---

## Question 8: What are predefined macros in C?
**Answer:**  
Predefined macros include:
- `__DATE__`: Compilation date.
- `__TIME__`: Compilation time.
- `__FILE__`: Current file name.
- `__LINE__`: Current line number.
- `__STDC__`: Defined as 1 if the compiler is ISO-compliant.

---

## Question 9: What is a function pointer in C?
**Answer:**  
A function pointer stores the address of a function and can be used to call the function indirectly.

---

## Question 10: How do you declare a function pointer?
**Answer:**  
```c
int (*func_ptr)(int, int);
```

---

## Question 11: What is the purpose of `malloc` in C?
**Answer:**  
`malloc` dynamically allocates memory at runtime and returns a pointer to the allocated memory.

---

## Question 12: How do you free dynamically allocated memory?
**Answer:**  
Use the `free` function. Example:
```c
free(ptr);
```

---

## Question 13: What is a dangling pointer?
**Answer:**  
A dangling pointer points to memory that has been freed or is out of scope.

---

## Question 14: What is a void pointer?
**Answer:**  
A void pointer (`void *`) is a generic pointer that can hold the address of any data type.

---

## Question 15: How do you implement a linked list in C?
**Answer:**  
Use a self-referential structure:
```c
struct Node {
    int data;
    struct Node *next;
};
```

---

## Question 16: What is the difference between `fgets` and `fgetc`?
**Answer:**  
- `fgets`: Reads a line of text.
- `fgetc`: Reads a single character.

---

## Question 17: How do you write data to a binary file in C?
**Answer:**  
Use the `fwrite` function. Example:
```c
fwrite(&data, sizeof(data), 1, fp);
```

---

## Question 18: What is the purpose of the `fseek` function?
**Answer:**  
`fseek` moves the file pointer to a specific location in the file.

---

## Question 19: How do you handle command-line arguments in C?
**Answer:**  
Use `argc` and `argv` in the `main` function. Example:
```c
int main(int argc, char *argv[]) {
    printf("First argument: %s\n", argv[1]);
    return 0;
}
```

---

## Question 20: What is the difference between `const int *p` and `int *const p`?
**Answer:**  
- `const int *p`: The value pointed to by `p` cannot be modified.
- `int *const p`: The pointer `p` cannot be modified.

---

## Question 21: What is a nested structure in C?
**Answer:**  
A nested structure is a structure that contains another structure as a member.

---

## Question 22: How do you access members of a nested structure?
**Answer:**  
Use the dot operator for each level. Example:
```c
student.address.city;
```

---

## Question 23: What is the purpose of the `typedef` keyword?
**Answer:**  
`typedef` creates an alias for a data type. Example:
```c
typedef struct Student Student;
```

---

## Question 24: What is a union in C?
**Answer:**  
A union is a user-defined data type where all members share the same memory location.

---

## Question 25: How do you declare a union in C?
**Answer:**  
```c
union Data {
    int i;
    float f;
    char str[20];
};
```

---

## Question 26: What is the size of a union?
**Answer:**  
The size of a union is equal to the size of its largest member.

---

## Question 27: How do you create a 2D array using pointers?
**Answer:**  
Use pointers to pointers:
```c
int **arr = (int **)malloc(rows * sizeof(int *));
for (int i = 0; i < rows; i++) {
    arr[i] = (int *)malloc(cols * sizeof(int));
}
```

---

## Question 28: How do you reverse a string in C?
**Answer:**  
Use a loop to swap characters from the start and end of the string.

---

## Question 29: What is the purpose of the `strtok` function?
**Answer:**  
`strtok` splits a string into tokens based on a delimiter.

---

## Question 30: How do you compare two strings in C?
**Answer:**  
Use the `strcmp` function. Example:
```c
int result = strcmp(str1, str2);
```

---

## Question 31: What is the difference between `malloc` and `calloc`?
**Answer:**  
- `malloc`: Allocates uninitialized memory.
- `calloc`: Allocates memory and initializes it to zero.

---

## Question 32: How do you resize memory in C?
**Answer:**  
Use the `realloc` function. Example:
```c
ptr = realloc(ptr, new_size);
```

---

## Question 33: What is a self-referential structure?
**Answer:**  
A structure that contains a pointer to itself. Example:
```c
struct Node {
    int data;
    struct Node *next;
};
```

---

## Question 34: How do you implement a stack using structures?
**Answer:**  
Use a structure to represent the stack and its elements.

---

## Question 35: How do you implement a queue using structures?
**Answer:**  
Use a structure to represent the queue and its elements.

---

## Question 36: What is the purpose of the `sizeof` operator?
**Answer:**  
`sizeof` returns the size of a data type or variable in bytes.

---

## Question 37: How do you handle errors in file operations?
**Answer:**  
Check the return value of file functions and use `perror` or `errno`.

---

## Question 38: What is a random access file?
**Answer:**  
A file that allows reading or writing at any position using `fseek`.

---

## Question 39: How do you delete a file in C?
**Answer:**  
Use the `remove` function. Example:
```c
remove("file.txt");
```

---

## Question 40: How do you rename a file in C?
**Answer:**  
Use the `rename` function. Example:
```c
rename("old.txt", "new.txt");
```

---

## Question 41: What is the purpose of the `fflush` function?
**Answer:**  
`fflush` clears the output buffer.

---

## Question 42: How do you tokenize a string without using `strtok`?
**Answer:**  
Manually split the string by searching for delimiters.

---

## Question 43: How do you implement a binary tree in C?
**Answer:**  
Use a self-referential structure to represent tree nodes.

---

## Question 44: What is the purpose of bit fields in structures?
**Answer:**  
Bit fields are used to save memory when storing flags or small values.

---

## Question 45: How do you serialize a structure in C?
**Answer:**  
Write the structure's data to a file in binary format.

---

## Question 46: How do you deserialize a structure in C?
**Answer:**  
Read the structure's data from a file in binary format.

---

## Question 47: How do you handle multi-word strings in C?
**Answer:**  
Use `fgets` to read the entire line.

---

## Question 48: How do you count the number of lines in a text file?
**Answer:**  
Read the file line by line and count the occurrences of newline characters.

---

## Question 49: How do you implement a dynamic array in C?
**Answer:**  
Use `malloc` and `realloc` to manage the array size dynamically.

---

## Question 50: How do you avoid memory leaks in C?
**Answer:**  
Free all dynamically allocated memory using `free` and set pointers to `NULL`.
