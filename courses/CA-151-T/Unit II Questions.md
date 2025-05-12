
# Unit II: Pointers - Questions and Answers

## Question 1: What is a pointer in C?
**Answer:**  
A pointer is a variable that stores the memory address of another variable.

---

## Question 2: How do you declare a pointer in C?
**Answer:**  
You declare a pointer using the `*` symbol. Example:
```c
int *ptr;
```

---

## Question 3: What is the difference between referencing and dereferencing?
**Answer:**  
- Referencing (`&`): Obtains the address of a variable.
- Dereferencing (`*`): Accesses the value at the address stored in a pointer.

---

## Question 4: What is a null pointer?
**Answer:**  
A null pointer is a pointer that does not point to any valid memory location. It is typically assigned the value `NULL`.

---

## Question 5: What is a dangling pointer?
**Answer:**  
A dangling pointer is a pointer that points to memory that has been freed or is out of scope.

---

## Question 6: What is a void pointer?
**Answer:**  
A void pointer (`void *`) is a generic pointer that can hold the address of any data type.

---

## Question 7: How do you initialize a pointer?
**Answer:**  
You initialize a pointer by assigning it the address of a variable. Example:
```c
int x = 10;
int *ptr = &x;
```

---

## Question 8: What is pointer arithmetic?
**Answer:**  
Pointer arithmetic involves operations like incrementing, decrementing, or adding/subtracting integers to/from pointers.

---

## Question 9: How does pointer arithmetic work with arrays?
**Answer:**  
Pointer arithmetic allows you to traverse an array by incrementing or decrementing the pointer.

---

## Question 10: What is the difference between `int *p` and `int p[]`?
**Answer:**  
- `int *p`: A pointer to an integer.
- `int p[]`: An array of integers.

---

## Question 11: What is a pointer to a pointer?
**Answer:**  
A pointer to a pointer is a variable that stores the address of another pointer. Example:
```c
int **ptr2;
```

---

## Question 12: How do you pass a pointer to a function?
**Answer:**  
You pass a pointer to a function by specifying the pointer type in the function parameter. Example:
```c
void func(int *ptr);
```

---

## Question 13: How do you return a pointer from a function?
**Answer:**  
You return a pointer from a function by specifying the pointer type as the return type. Example:
```c
int* func();
```

---

## Question 14: What is a function pointer?
**Answer:**  
A function pointer is a pointer that stores the address of a function.

---

## Question 15: How do you declare a function pointer?
**Answer:**  
You declare a function pointer using the following syntax:
```c
return_type (*func_ptr)(parameter_types);
```

---

## Question 16: What is the difference between `const int *p` and `int *const p`?
**Answer:**  
- `const int *p`: The value pointed to by `p` cannot be modified.
- `int *const p`: The pointer `p` cannot be modified.

---

## Question 17: What is dynamic memory allocation?
**Answer:**  
Dynamic memory allocation is the process of allocating memory at runtime using functions like `malloc`, `calloc`, and `realloc`.

---

## Question 18: How do you allocate memory using `malloc`?
**Answer:**  
You use `malloc` to allocate memory. Example:
```c
int *ptr = (int *)malloc(sizeof(int) * 5);
```

---

## Question 19: What is the difference between `malloc` and `calloc`?
**Answer:**  
- `malloc`: Allocates uninitialized memory.
- `calloc`: Allocates memory and initializes it to zero.

---

## Question 20: How do you resize memory using `realloc`?
**Answer:**  
You use `realloc` to resize previously allocated memory. Example:
```c
ptr = (int *)realloc(ptr, sizeof(int) * 10);
```

---

## Question 21: How do you free dynamically allocated memory?
**Answer:**  
You use the `free` function to release dynamically allocated memory. Example:
```c
free(ptr);
```

---

## Question 22: What is a memory leak?
**Answer:**  
A memory leak occurs when dynamically allocated memory is not freed, leading to wasted memory.

---

## Question 23: What is the difference between call by value and call by reference?
**Answer:**  
- Call by value: Passes a copy of the variable.
- Call by reference: Passes the address of the variable.

---

## Question 24: How do you implement call by reference in C?
**Answer:**  
You implement call by reference using pointers. Example:
```c
void func(int *ptr);
```

---

## Question 25: What is a pointer to an array?
**Answer:**  
A pointer to an array stores the address of the first element of the array.

---

## Question 26: What is an array of pointers?
**Answer:**  
An array of pointers is an array where each element is a pointer.

---

## Question 27: How do you access elements of an array using a pointer?
**Answer:**  
You access elements using pointer arithmetic. Example:
```c
*(ptr + i);
```

---

## Question 28: How do you pass an array to a function using a pointer?
**Answer:**  
You pass the array's address to the function. Example:
```c
void func(int *arr);
```

---

## Question 29: What is a dangling pointer?
**Answer:**  
A dangling pointer points to memory that has been freed or is out of scope.

---

## Question 30: How do you avoid dangling pointers?
**Answer:**  
You avoid dangling pointers by setting the pointer to `NULL` after freeing it.

---

## Question 31: What is a function pointer used for?
**Answer:**  
Function pointers are used for callbacks, state machines, and dynamic function calls.

---

## Question 32: How do you declare a pointer to a function that takes two integers and returns an integer?
**Answer:**  
```c
int (*func_ptr)(int, int);
```

---

## Question 33: How do you use a function pointer to call a function?
**Answer:**  
You use the function pointer like this:
```c
result = func_ptr(arg1, arg2);
```

---

## Question 34: What is the purpose of `const` with pointers?
**Answer:**  
`const` can restrict modification of the pointer or the value it points to.

---

## Question 35: How do you create a 2D array using pointers?
**Answer:**  
You create a 2D array using pointers to pointers. Example:
```c
int **arr = (int **)malloc(rows * sizeof(int *));
for (int i = 0; i < rows; i++) {
    arr[i] = (int *)malloc(cols * sizeof(int));
}
```

---

## Question 36: What is the difference between `int *p[10]` and `int (*p)[10]`?
**Answer:**  
- `int *p[10]`: An array of 10 pointers to integers.
- `int (*p)[10]`: A pointer to an array of 10 integers.

---

## Question 37: How do you reverse an array using pointers?
**Answer:**  
You reverse an array by swapping elements using two pointers:
```c
void reverse(int *arr, int size) {
    int *start = arr, *end = arr + size - 1;
    while (start < end) {
        int temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }
}
```

---

## Question 38: What is a pointer to a constant?
**Answer:**  
A pointer to a constant is a pointer that cannot modify the value it points to. Example:
```c
const int *ptr;
```

---

## Question 39: What is a constant pointer?
**Answer:**  
A constant pointer is a pointer that cannot change the address it holds. Example:
```c
int *const ptr;
```

---

## Question 40: What is a constant pointer to a constant?
**Answer:**  
A constant pointer to a constant cannot modify the value it points to or the address it holds. Example:
```c
const int *const ptr;
```

---

## Question 41: How do you allocate memory for a string dynamically?
**Answer:**  
You allocate memory for a string using `malloc`. Example:
```c
char *str = (char *)malloc(50 * sizeof(char));
```

---

## Question 42: How do you pass a string to a function using a pointer?
**Answer:**  
You pass the string's address to the function. Example:
```c
void func(char *str);
```

---

## Question 43: How do you use a pointer to traverse a string?
**Answer:**  
You use a pointer to iterate through each character. Example:
```c
for (char *p = str; *p != '\0'; p++) {
    printf("%c", *p);
}
```

---

## Question 44: What is the difference between `char *str` and `char str[]`?
**Answer:**  
- `char *str`: A pointer to a character.
- `char str[]`: An array of characters.

---

## Question 45: How do you detect a memory leak in C?
**Answer:**  
You use tools like Valgrind to detect memory leaks.

---

## Question 46: What is the purpose of `sizeof` with pointers?
**Answer:**  
`sizeof` returns the size of the pointer type, not the size of the data it points to.

---

## Question 47: How do you implement a linked list using pointers?
**Answer:**  
You use pointers to create nodes and link them. Example:
```c
struct Node {
    int data;
    struct Node *next;
};
```

---

## Question 48: How do you implement a dynamic array using pointers?
**Answer:**  
You use `malloc` and `realloc` to manage the array size dynamically.

---

## Question 49: What is the difference between stack and heap memory?
**Answer:**  
- Stack: Memory is allocated automatically and has limited size.
- Heap: Memory is allocated dynamically and has a larger size.

---

## Question 50: How do you avoid memory leaks in C?
**Answer:**  
You avoid memory leaks by freeing all dynamically allocated memory using `free`.
