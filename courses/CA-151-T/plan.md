# Advanced C Programming Study Plan

This document is a structured study guide based on **CA–151–T: Advanced C Programming**. It covers major topics such as Preprocessor directives, pointers, strings, structures, and file handling in C. Each chapter provides explanations, code samples, exercises, and a comprehension question.

---

## Chapter 1: Preprocessor

### 1.1 Overview of the C Preprocessor

- **Definition**: The C preprocessor is a text substitution tool that modifies the source code before compilation.
- **Role**: It handles directives (e.g., `#include`, `#define`) and prepares the code for the compiler.

### 1.2 Format of Preprocessor Directives

- **File Inclusion** (`#include`):
  - `#include <stdio.h>` vs. `#include "myheader.h"`.
  
- **Macro Substitution** (`#define`):
  - Object-like macros (simple replacement).
  - Function-like (parameterized) macros.
  - Nested macros.

- **Macros vs. Functions**:
  - Macros are replaced textually at compile time, while functions are type-checked and compiled.

- **Conditional Compilation**:
  - `#if`, `#ifdef`, `#else`, `#elif`, `#endif`.
  - Controlling compilation paths.

- **Predefined Macros**:
  - `__DATE__`, `__TIME__`, `__FILE__`, `__LINE__`, `__STDC__`.

### 1.3 Conditional Compilation and Predefined Macros

- **Use Cases**: Feature toggling, debugging, platform-specific code.

- **Other Directives**: `#error`, `#pragma`.

### Example 1: Basic Macro and Conditional Compilation

````c
#include <stdio.h>

// Macro for PI
#define PI 3.14159

// Parameterized Macro for area of a circle
#define AREA_CIRCLE(r) (PI * (r) * (r))

// Conditional compilation to check for DEBUG
#ifdef DEBUG
  #define LOG(msg) printf("DEBUG: %s\n", msg)
#else
  #define LOG(msg)
#endif

int main() {
    double radius = 2.5;
    double area = AREA_CIRCLE(radius);

    LOG("Calculating circle area");
    printf("Area = %f\n", area);

    return 0;
}

Explanation:

We define macros for PI and for calculating a circle’s area.
LOG(msg) only prints if DEBUG is defined.
Example 2: Predefined Macros

```c
#include <stdio.h>

int main() {
    printf("File: %s\n", __FILE__);
    printf("Date: %s\n", __DATE__);
    printf("Time: %s\n", __TIME__);
    printf("Line: %d\n", __LINE__);
    printf("STDC: %d\n", __STDC__);
    return 0;
}
````

Explanation:

Demonstrates usage of macros that embed file name, date/time, etc.
Exercises
Define a macro MAX(a,b) that returns the maximum of two numbers.
Write a macro IS_UPPER(c) to check if a character is uppercase.
Use #ifdef to compile different branches for Windows vs. Linux environments (simulate with a macro).

### End-of-Chapter Question

Q1: What is the difference between an object-like macro and a function-like macro in C, and in which scenarios would you choose one over the other?

## Chapter 2: Pointers

### 2.1 Concept of Pointers

Pointers: Variables holding memory addresses.
Operators: * (dereference) and & (address of).
Declaration & Initialization: int *p;, setting to NULL.

### 2.2 Pointer Arithmetic

Increment/decrement a pointer, difference of pointers, adding an integer to a pointer.

### 2.3 Parameter Passing

Call by Value vs. Call by Reference:
Using pointers can modify the original variable directly.

### 2.4 Pointers and Arrays

Array decays to a pointer; can have pointer to array or array of pointers.

### 2.5 Functions & Pointers

Pass pointers to functions.
Return pointers from functions (avoid returning local addresses).
Function Pointers:
Store addresses of functions for callbacks or plug-in modules.

### 2.6 Dynamic Memory Management

malloc, calloc, realloc, and free.
Avoid memory leaks and dangling pointers.

#### Example 3: Swapping Two Variables (Call by Reference)

```c
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 10, y = 20;
    printf("Before swap: x=%d, y=%d\n", x, y);
    swap(&x, &y);
    printf("After swap : x=%d, y=%d\n", x, y);
    return 0;
}
```

Explanation:

Swapping uses pointers to modify the original variables directly.

#### Example 4: Dynamic Array Creation and Usage

```c
#include <stdio.h>
#include <stdlib.h> // For malloc, free

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    // Allocate memory for array of n integers
    int *arr = (int*)malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // Initialize array
    for(int i = 0; i < n; i++) {
        arr[i] = i + 1;
    }

    // Print array elements
    printf("Array elements: ");
    for(int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    free(arr);     // Release memory
    arr = NULL;    // Avoid dangling pointer

    return 0;
}
```

**Explanation:**

Demonstrates dynamic memory allocation and proper cleanup.

### Exercises

- Write a program that reads an integer array dynamically, then prints it in reverse using pointer notation.
- Use function pointers in a menu-driven calculator (add, subtract, multiply, divide).
- Demonstrate a pointer to pointer to swap two strings.

### End-of-Chapter Question

Q2: In what scenarios would you choose to use a pointer to a pointer, and what additional considerations must you handle with such usage?

## Chapter 3: Strings

### 3.1 Introduction to Strings in C

Character arrays vs. string literals.
Null Terminator '\0' is crucial.

### 3.2 Reading and Writing Strings

scanf, gets, fgets, printf, puts.
Handling buffer size and newlines.

### 3.3 Strings and Pointers

Arrays of characters vs. pointers to characters.
Arrays of strings vs. array of character pointers.

### 3.4 String Functions in <string.h>

strlen, strcpy, strcat, strcmp, strrev, strlwr, strupr, etc.
strtok for tokenizing strings.

### 3.5 Command-Line Arguments

int main(int argc, char \*argv[])
Access arguments for text processing or configurations.

#### Example 5: Basic String Manipulations

```c
#include <stdio.h>
#include <string.h>

int main() {
    char name[50];
    printf("Enter your name: ");
    fgets(name, 50, stdin);

    // Remove trailing newline
    name[strcspn(name, "\n")] = '\0';

    printf("Length of name: %lu\n", strlen(name));

    // Convert to uppercase
    strupr(name);
    printf("Name in uppercase: %s\n", name);

    return 0;
}
```

**Explanation:**

Demonstrates reading input with fgets, removing the newline, and using strupr.

#### Example 6: Command-line Argument Usage

```c
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <word>\n", argv[0]);
        return 1;
    }

    char temp[100];
    strcpy(temp, argv[1]);
    strrev(temp);

    printf("Original: %s\n", argv[1]);
    printf("Reversed: %s\n", temp);

    return 0;
}
```

**Explanation:**

Demonstrates usage of command-line arguments to manipulate a string.

### Exercises

- Write a program to split a sentence into tokens using strtok.
- Check if two strings are anagrams (case-insensitive).
- Create a command-line program that counts vowels, consonants, and digits from the user input.

### End-of-Chapter Question

Q3: Explain the differences between using a character array (e.g., char str[50]) and a character pointer (e.g., char \*str) for storing strings. How does memory allocation differ?

## Chapter 4: Structures

### 4.1 Introduction to Structures

Group multiple data types under one name.
Declaration: struct student { ... };

### 4.2 Array of Structures

Example: struct student students[30];
Useful for lists/records.

### 4.3 Pointers to Structures

struct student *ptr;
Access via ptr->member or (*ptr).member.

### 4.4 Structures and Functions

Pass structures to functions by value or by pointer (address).
Large structures are typically passed by pointer for efficiency.

### 4.5 Nested Structures, typedef, and Union

Nested Structures: struct inside another struct.
typedef: Simplifies struct usage.
Union: Shares memory among members.
Example 7: Array of Structures

```c
#include <stdio.h>
#include <string.h>

struct Student {
    int rollNo;
    char name[50];
    float marks;
};

int main() {
    struct Student sArr[3];

    // Input
    for(int i = 0; i < 3; i++) {
        printf("Enter rollNo, name, and marks for student %d:\n", i+1);
        scanf("%d", &sArr[i].rollNo);

        getchar(); // consume leftover newline
        fgets(sArr[i].name, 50, stdin);
        sArr[i].name[strcspn(sArr[i].name, "\n")] = '\0';

        scanf("%f", &sArr[i].marks);
    }

    // Output
    printf("\nStudent Details:\n");
    for(int i = 0; i < 3; i++) {
        printf("Roll: %d, Name: %s, Marks: %.2f\n",
               sArr[i].rollNo, sArr[i].name, sArr[i].marks);
    }

    return 0;
}
```

**Explanation:**

Demonstrates how to read and store multiple student records.

#### Example 8: Using typedef and Union

```c
#include <stdio.h>

typedef struct {
    char title[30];
    float price;
} Book;

union Data {
    int i;
    float f;
    char str[20];
};

int main() {
    Book b = {"C Programming", 299.0f};
    printf("Book: %s, Price: %.2f\n", b.title, b.price);

    union Data data;
    data.i = 10;
    printf("Union Data (int): %d\n", data.i);

    data.f = 10.5;
    printf("Union Data (float): %.2f\n", data.f);
    // Overwrites the memory used by 'i'

    return 0;
}
```

**Explanation:**

typedef renames a struct to Book.
union demonstrates shared memory usage.

#### Exercises

- Write a program to sort an array of structures (e.g. employees) by salary.
- Create a nested structure (employee record with struct date for joining date).
- Demonstrate how union members share memory by storing different types.

### End-of-Chapter Question

Q4: When passing a structure to a function, what are the trade-offs between passing it by value vs. by address?

Chapter 5: File Handling
5.1 Introduction to File Handling
Streams: Logical interface to file data.
Need: Persistent data storage, handling large data.
5.2 Types of Files
Text Files: Character-based, readable.
Binary Files: Stores raw memory representations.
5.3 File Operations
fopen, fclose.
fgetc, fputc, fgets, fputs, fread, fwrite, fprintf, fscanf.
Random Access: fseek, ftell, rewind.
Example 9: Writing and Reading Text Files

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    fp = fopen("data.txt", "w");
    if(!fp) {
        printf("Cannot open file.\n");
        return 1;
    }

    // Write to file
    fprintf(fp, "Hello, world!\n");
    fclose(fp);

    // Read the same file
    fp = fopen("data.txt", "r");
    if(!fp) {
        printf("Cannot open file.\n");
        return 1;
    }

    char line[100];
    while(fgets(line, 100, fp) != NULL) {
        printf("%s", line);
    }
    fclose(fp);

    return 0;
}
```

**Explanation:**

Demonstrates writing to and reading from a text file.
Example 10: Reading & Writing a Binary File

```c
#include <stdio.h>
#include <stdlib.h>

struct Record {
    int id;
    float value;
};

int main() {
    struct Record rec1 = {1001, 55.75f}, rec2;
    FILE *fp = fopen("data.bin", "wb");
    if(!fp) {
        printf("Cannot open file.\n");
        return 1;
    }

    fwrite(&rec1, sizeof(struct Record), 1, fp);
    fclose(fp);

    fp = fopen("data.bin", "rb");
    if(!fp) {
        printf("Cannot open file.\n");
        return 1;
    }

    fread(&rec2, sizeof(struct Record), 1, fp);
    fclose(fp);

    printf("Read from file: ID=%d, Value=%.2f\n", rec2.id, rec2.value);

    return 0;
}
```

**Explanation:**

Demonstrates binary read/write for a structure.

### Exercises

- Write a program to append text at the end of an existing file, then display its new contents.
- Implement a menu-driven program to store student records in a binary file (add/search/display).
- Use fseek to randomly access and read a record from a binary file.

### End-of-Chapter Question

Q5: Explain how random access (fseek, ftell) can be used to efficiently update a single record in a large binary file without reading the entire file.

## Practice, Review, and Further Reading

Putting It All Together
Combine pointers, structures, and file handling:

### Example: Student management System

A student management system that uses dynamic arrays (pointers), stores data in a binary file, and uses a structure to define records.

#### Additional Exercises

- File Encryption

  Read from a text file, shift each character by some key, and write to a new file.

- Sorting a Large File

  Store numeric data in a binary file; implement an external sorting algorithm using partial reads/writes.

- Advanced Macros

  Create debug macros to log current line, file, and function name in an error log.

## Recommended Reading

- The C Programming Language (2nd Edition) – B.W. Kernighan & D.M. Ritchie
- Programming in C – A Practical Approach – Ajay Mittal (Pearson)
- Programming with C – Byron S. Gottfried (Schaum’s Outlines)
- A Structured Programming Approach using C – Behrouz Forouzan & Richard Gilberg
- Let Us C – Yashwant Kanetkar (BPB Publications)
