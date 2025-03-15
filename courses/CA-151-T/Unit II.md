## Unit II: Pointers (07 Hrs)

- Concept – reference & dereference, Declaration, definition, initialization & use, Types of pointers,
- Pointer Arithmetic, Multiple indirection, parameter passing – call by value and call by reference
- Arrays & Pointers - Pointer to array, Array of pointers,
- Functions & pointers - Passing pointer to function, Returning pointer from function, Function pointer, Pointers & const
- Dynamic memory management, Allocation, Resizing, Releasing, Memory leak / dangling pointers

---

# Chapter 2: Pointers

Pointers are one of the most powerful and distinctive features of the C language. They allow direct memory manipulation, more efficient parameter passing, and dynamic memory allocation. By understanding pointers thoroughly, you gain the ability to write more flexible and optimized programs. This chapter explores pointer fundamentals and their advanced usage.

---

## 1. Concept of Pointers

### 1.1 Reference and Dereference

- A **pointer** is a variable whose value is the **address** of another variable.
- In C, you declare a pointer by using the asterisk (`*`) symbol after the type, for example:
  ```c
  int *ptr;
  This means ptr can hold the address of an int variable.
  ```

Referencing (the “address-of” operator, &):
If you have an integer variable x, &x is the address of x.

Dereferencing (the “value-at” operator, *):
If ptr stores the address of x, then *ptr is the value inside that address (i.e., the value of x).

Illustration
Let’s say we have:

```c
int x = 10;
int *p = &x;  // p now contains the address of x
x has a value of 10 (and some address in memory).
p has the address of x.
*p gives 10, the value at that memory location.
1.2 Declaration, Definition, Initialization, and Use
Declaration: Tells the compiler the pointer's type.
```

````c
int *p;
Definition: Actually allocates space for the pointer variable p.
Often declaration and definition appear together in C. For example:
```c
int *p = NULL;
Initialization: Assign a valid address or NULL to the pointer.
int x = 5;
int *p = &x; // initialization with address of x
````

Usage:
Dereference to read or write the target variable: _p = 12;
1.3 Types of Pointers
Null Pointer: A pointer that doesn't point to any valid memory location. (Typically NULL in C.)
Dangling Pointer: A pointer that points to memory which has already been freed or is out of scope.
Void Pointer (void _): A generic pointer that can hold the address of any data type. Often used in library functions like malloc.
Function Pointer: A pointer that holds the address of a function. 2. Pointer Arithmetic
Pointer arithmetic allows you to manipulate the address stored in a pointer. Some key concepts:

Increment/Decrement:

p++ moves the pointer to the “next” element of its base type.
If p is of type int\*, incrementing p by 1 jumps forward by sizeof(int) bytes in memory.
Addition/Subtraction:

p + n moves the pointer n elements ahead.
p - n moves the pointer n elements backward.
Difference of Two Pointers:

If p and q point into the same array, p - q gives the number of elements between them.
Important: Pointer arithmetic is only valid within an array’s bounds or just past the last element (one-past-the-end pointer).

Example: Pointer Arithmetic

```c
#include <stdio.h>

int main(void) {
    int arr[] = {10, 20, 30, 40, 50};
    int *p = arr;       // Points to arr[0]
    int *q = &arr[4];   // Points to arr[4]

    printf("Value at p: %d\n", *p);       // 10
    p++;  // Move to arr[1]
    printf("Value at p: %d\n", *p);       // 20

    int diff = q - p;   // Number of elements between q and p
    printf("Elements between q and p: %d\n", diff);

    return 0;
}
```

3. Multiple Indirection
   Multiple indirection means having pointers to pointers (or even deeper levels). For example:

int \*\*ptr2; is a pointer to a pointer to an int.
Usage scenario: 2D arrays, arrays of strings, or dynamic data structures (linked lists, etc.).

```c
#include <stdio.h>

int main(void) {
    int x = 100;
    int *p = &x;    // p is pointer to int
    int **q = &p;   // q is pointer to pointer-to-int

    printf("x = %d\n", x);         // 100
    printf("*p = %d\n", *p);       // 100
    printf("**q = %d\n", **q);     // 100

    // Modify x via q
    **q = 200;
    printf("x after **q = 200 -> %d\n", x);   // 200

    return 0;
}
```

# 4. Parameter Passing: Call by Value vs. Call by Reference

## 4.1 Call by Value

In call by value, a copy of the actual parameter is passed to the function. Any modifications inside the function do not affect the original.

```c
void swapWrong(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    // This won't affect the original variables
}
```

## 4.2 Call by Reference

In call by reference, you pass the address of the variable to the function, so the function can modify the original variable.

```c
#include <stdio.h>

void swapCorrect(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void) {
    int x = 10, y = 20;
    printf("Before swap: x=%d, y=%d\n", x, y);
    swapCorrect(&x, &y);
    printf("After swap: x=%d, y=%d\n", x, y);
    return 0;
}
```

# 5. Arrays and Pointers

## 5.1 Pointer to an Array

When you declare an array int arr[5];, the array’s name (arr) can act like a pointer to its first element.

````c
int arr[3] = {1,2,3};
int *p = arr;   // p points to arr[0]
Accessing elements:

*(p + i) is equivalent to arr[i]
p[i] is also valid notation (p[i] == arr[i])
5.2 Array of Pointers
You can have arrays whose elements are themselves pointers.

```c
#include <stdio.h>

int main(void) {
    const char *names[] = {"Alice", "Bob", "Carol"};
    // names[0] -> "Alice"
    // names[1] -> "Bob"
    // names[2] -> "Carol"

    for(int i = 0; i < 3; i++) {
        printf("names[%d] = %s\n", i, names[i]);
    }

    return 0;
}
````

In this case, each element of the array is a const char\*.

# 6. Functions and Pointers

## 6.1 Passing Pointers to Functions

You can pass pointers as arguments to functions, enabling:

Direct modification of data in the calling scope (call by reference).
Access to large data structures (like arrays) without copying them.
Example:

```c
#include <stdio.h>

void incrementArray(int *arr, int size) {
    for(int i = 0; i < size; i++) {
        arr[i]++;
    }
}

int main(void) {
    int nums[] = {1, 2, 3, 4, 5};
    incrementArray(nums, 5);  // Pass pointer to the first element of nums
    for(int i=0; i<5; i++){
        printf("%d ", nums[i]);  // Now prints: 2 3 4 5 6
    }
    return 0;
}
```

## 6.2 Returning a Pointer from a Function

A function can also return a pointer, but ensure that the pointer remains valid (i.e., do not return pointers to local variables on the stack).

Valid scenario:

```c
int* findMax(int *a, int *b) {
    if(*a > *b)
        return a;
    else
        return b;
}
```

## 6.3 Function Pointers

A function pointer stores the address of a function. This can be used for callbacks, state machines, or strategies.

Declaration

````c
return_type (*func_ptr)(type1, type2, ...);
Example
```c
#include <stdio.h>

// A function that matches the signature "int fn(int,int)"
int add(int a, int b) {
    return a + b;
}

int main(void) {
    // Declare a function pointer
    int (*fp)(int, int) = add;
    // Call the pointed function
    int result = fp(10, 20);
    printf("Result = %d\n", result);
    return 0;
}
````

# 7. Pointers and const

Pointers can be combined with const in various ways:

const int *p – You cannot modify the value pointed by p, but can change p.
int *const p – You cannot change p (it always points to the same address), but can modify the value pointed by p.
const int \*const p – You can neither change p nor the value it points to.

# 8. Dynamic Memory Management

In C, you can dynamically allocate memory during runtime using the standard library functions in <stdlib.h>:

malloc()
calloc()
realloc()
free()

## 8.1 Allocation

```c
int *p = (int *)malloc(sizeof(int) * 5);
if(p == NULL) {
    // allocation failed
}
```

Allocates enough space for 5 integers.
Returns a pointer of type void*, typically cast to (int*).

## 8.2 Resizing

```c
p = (int *)realloc(p, sizeof(int) * 10);
```

Changes the size of the memory block pointed by p to hold 10 integers now.

## 8.3 Releasing

```c
free(p);
p = NULL; // Good practice to set pointer to NULL after freeing
```

## 8.4 Memory Leak / Dangling Pointer

Memory leak: When allocated memory is never freed, leading to wasted memory.
Dangling pointer: When a pointer still points to memory that has been freed or gone out of scope.

# 9. Code Examples

Below are some short samples demonstrating pointers in various contexts.

Example 1: Call-by-Reference with Pointer

```c
#include <stdio.h>

void doubleValue(int *x) {
    *x *= 2;
}

int main(void) {
    int num = 10;
    printf("Before: %d\n", num);
    doubleValue(&num);
    printf("After: %d\n", num);
    return 0;
}
```

Example 2: Pointer to Pointer

```c
#include <stdio.h>

int main(void) {
    int x = 5;
    int *p = &x;
    int **pp = &p;

    printf("x = %d\n", x);
    printf("*p = %d\n", *p);
    printf("**pp = %d\n", **pp);
    return 0;
}
```

Example 3: Dynamic Allocation of an Integer Array

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n = 5;
    int *arr = (int *)malloc(n * sizeof(int));
    if(!arr) {
        printf("Memory allocation failed\n");
        return 1;
    }

    for(int i = 0; i < n; i++) {
        arr[i] = (i + 1) * 10;
    }

    // Resize to hold 8 integers
    arr = (int *)realloc(arr, 8 * sizeof(int));
    if(!arr) {
        printf("Memory reallocation failed\n");
        return 1;
    }
    // Initialize the new 3 elements
    for(int i = 5; i < 8; i++) {
        arr[i] = (i + 1) * 10;
    }

    for(int i = 0; i < 8; i++) {
        printf("%d ", arr[i]);
    }
    free(arr);
    arr = NULL; // Avoid dangling pointer

    return 0;
}
```

# 10. Practice Exercises

## Pointer Arithmetic

Write a C program that declares an integer array of size 5, initializes it, and uses pointer arithmetic to:

## Print each element of the array.

Compute the sum of all elements.
Pointer to Pointer
Using a pointer-to-pointer, modify the value of a variable two levels up. Print the initial and final values to see the effect.

## Passing Arrays by Reference

Write a function reverseArray(int \*arr, int size) that reverses the elements in an integer array using pointer arithmetic. Confirm that the changes reflect in main().

## Dynamic String Allocation

Prompt the user for a string length and allocate a character array dynamically. Fill it from user input, then print it out. Release the memory at the end.

## Function Pointer

Declare a function pointer for a function that takes two integers and returns their greatest common divisor (GCD). Implement the function, assign its address to the pointer, and call it.

# 11. End-of-Chapter Question

Question:

Discuss the difference between a pointer to an array and an array of pointers. Provide a situation where each would be more appropriate.

Think about memory layout, usage scenarios, and how references to data differ in each case.
