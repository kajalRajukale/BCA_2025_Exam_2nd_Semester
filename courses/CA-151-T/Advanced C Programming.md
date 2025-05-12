# BCA Content: CA – 151 - T Advanced C Programming

| Scheme          |                                 |                        |
| --------------- | ------------------------------- | ---------------------- |
| **Teaching**    | Theory: 02 Hrs/Week             | Credits: 02            |
| **Examination** | Continuous Evaluation: 15 Marks | End-Semester: 35 Marks |

**Course Objectives:**

- To learn advanced features in C Programming
- To study advanced data types
- To understand built-in library functions

**Course Outcomes:**  
On completion of the course, student will be able to:

- Write programs using pointers and structures
- Use Pre-processor directives
- Manipulate strings using library functions
- Write programs to perform operations on Files

**Course Contents**

## Unit I: Preprocessor (06 Hrs)

- Concept, Format of preprocessor directives, File inclusion directives (#include), Macro substitution directives (#define), nested macros, parameterized macros,
- Macros versus functions, #error / #pragma directives, Conditional compilation (#if/#ifdef/#else/#elif/#endif), Predefined macros (_DATE_ / _TIME_ /_FILE_ /_LINE_/ _STDC_)

## Unit II: Pointers (07 Hrs)

- Concept – reference & dereference, Declaration, definition, initialization & use, Types of pointers,
- Pointer Arithmetic, Multiple indirection, parameter passing – call by value and call by reference
- Arrays & Pointers - Pointer to array, Array of pointers,
- Functions & pointers - Passing pointer to function, Returning pointer from function, Function pointer, Pointers & const
- Dynamic memory management, Allocation, Resizing, Releasing, Memory leak / dangling pointers

## Unit III: Strings (05 Hrs)

- Concept, Declaration, definition, initialization, format specifiers, String literals/ constants & variables – reading & writing from & to console, Importance of terminating NULL character, Strings & pointers
- Array of strings & array of character pointers, User defined functions, predefined functions in string.h - strlen, strcpy, strcat, strcmp, strcmpi, strrev, strlwr, strupr, strset, strchr, strrchr, strstr, strncpy, strncat, strncmp, strncmpi, strnset, strtok, Command line arguments – argc and argv

## Unit IV: Structures (06 Hrs)

- Concept, Declaration, definition, initialization, accessing structure members (. operator), Array of structures, Pointers to structures, Declaring pointer to structure
- Accessing structure members via pointer to structure, Structures & functions, Passing each member of structure as a separate argument, Passing structure by value / address
- Nested structures, typedef & structures, Concept of Union

## Unit V: File Handling (06 Hrs)

- Concept of streams, need, Types of files, Operations on text & binary files, Random access file, library functions for file handling – fopen, fclose, fgetc, fseek, fgets, fputc etc

**Reference Books:**

1. The C Programming Language (Second Edition) – By B. W. Kernighan & D. M. Ritchie
2. Programming in C – A Practical Approach – By Ajay Mittal (Pearson Publications)
3. Programming with C – By Byron S Gottfried (Schaum’s Outlines)
4. A structural Programming Approach using C – By Behrouz Forouzan & Richard Gilberg
5. Y S Kanetkar, “Let Us C”, BPB Publications

# Content

- [BCA Content: CA – 151 - T Advanced C Programming](#bca-content-ca--151---t-advanced-c-programming)
  - [Unit I: Preprocessor (06 Hrs)](#unit-i-preprocessor-06-hrs)
  - [Unit II: Pointers (07 Hrs)](#unit-ii-pointers-07-hrs)
  - [Unit III: Strings (05 Hrs)](#unit-iii-strings-05-hrs)
  - [Unit IV: Structures (06 Hrs)](#unit-iv-structures-06-hrs)
  - [Unit V: File Handling (06 Hrs)](#unit-v-file-handling-06-hrs)
- [Content](#content)
- [Chapter 1: Preprocessor](#chapter-1-preprocessor)
  - [1.1 Concept and Format of Preprocessor Directives](#11-concept-and-format-of-preprocessor-directives)
  - [1.2 File Inclusion Directives (`#include`)](#12-file-inclusion-directives-include)
  - [1.3 Macro Substitution Directives (`#define`), Nested Macros, Parameterized Macros](#13-macro-substitution-directives-define-nested-macros-parameterized-macros)
  - [1.4 Macros vs Functions](#14-macros-vs-functions)
  - [1.5 Conditional Compilation (`#if`, `#ifdef`, `#else`, `#elif`, `#endif`)](#15-conditional-compilation-if-ifdef-else-elif-endif)
  - [1.6 Other Directives](#16-other-directives)
  - [Chapter 1: Sample Programs (10)](#chapter-1-sample-programs-10)
  - [Chapter 1: Exercises (10)](#chapter-1-exercises-10)
- [Chapter 2: Pointers](#chapter-2-pointers)
  - [Chapter 2: Exercises (10)](#chapter-2-exercises-10)
- [Chapter 3: Strings](#chapter-3-strings)
  - [3.1 Concept, Declaration, Definition, Initialization](#31-concept-declaration-definition-initialization)
  - [3.2 String Literals/Constants \& Variables](#32-string-literalsconstants--variables)
  - [3.3 Reading and Writing Strings](#33-reading-and-writing-strings)
  - [3.5 Array of Strings \& Array of Character Pointers](#35-array-of-strings--array-of-character-pointers)
  - [3.6 User Defined String Functions](#36-user-defined-string-functions)
  - [3.7 Predefined Functions in \<string.h\>](#37-predefined-functions-in-stringh)
  - [3.8 Command-Line Arguments (argc and argv)](#38-command-line-arguments-argc-and-argv)
  - [Chapter 3: Sample Programs (10)](#chapter-3-sample-programs-10)
  - [Chapter 4: Exercises (10)](#chapter-4-exercises-10)

---

# Chapter 1: Preprocessor

## 1.1 Concept and Format of Preprocessor Directives

**Description:**  
The C preprocessor is a text-substitution tool that modifies your source code before compilation. It handles directives such as macro expansions, file inclusions, and conditional compilations.

**Key Points:**

- Preprocessor runs before the compiler’s translation phase.
- Syntax typically begins with `#` (e.g., `#define`, `#include`).

## 1.2 File Inclusion Directives (`#include`)

**Description:**

- `#include <stdio.h>` or `#include "filename.h"` inserts the entire contents of the specified file into your source code.
- Angle brackets (`< >`) typically search standard library directories, while double quotes (`" "`) search local directories.

## 1.3 Macro Substitution Directives (`#define`), Nested Macros, Parameterized Macros

**Description:**

- `#define` creates symbolic constants or macros that can substitute expressions in code.
- Macros can also take parameters (function-like macros).
- Nested macros occur when macros call other macros.

## 1.4 Macros vs Functions

**Description:**

- Macros are expanded at preprocess time, so they can be faster but less type-safe.
- Functions are compiled once, can be type-checked, and are typically safer.

## 1.5 Conditional Compilation (`#if`, `#ifdef`, `#else`, `#elif`, `#endif`)

**Description:**

- Enables inclusion/exclusion of code based on certain conditions (e.g., checking if a macro is defined).
- Useful for cross-platform code or debugging sections.

## 1.6 Other Directives

**Description:**

- `#error` directive can generate a compilation error with a custom message.
- `#pragma` handles compiler-specific directives.
- Predefined macros (e.g. `__DATE__`, `__TIME__`, `__LINE__`, `__FILE__`, `__STDC__`).

---

## Chapter 1: Sample Programs (10)

1. **Basic Macro Definition**

   ```c
   #include <stdio.h>
   #define PI 3.14159

   int main() {
       printf("Value of PI: %f\n", PI);
       return 0;
   }
   ```

````

Parameterized Macro

```c
#include <stdio.h>
#define SQUARE(x) ((x) * (x))

int main() {
    int num = 5;
    printf("Square of %d is %d\n", num, SQUARE(num));
    return 0;
}
````

````

Nested Macro

```c
#include <stdio.h>
#define DOUBLE(x) ((x) + (x))
#define QUADRUPLE(x) DOUBLE(DOUBLE(x))

int main() {
    printf("Quadruple of 3: %d\n", QUADRUPLE(3));
    return 0;
}
````

````
Macro vs. Inline Function Speed Check (Conceptual snippet)

```c
#include <stdio.h>
#define MUL(a, b) ((a) * (b))

inline int mul_func(int a, int b) {
    return a * b;
}
````

int main() {
printf("Macro: %d\n", MUL(2,3));
printf("Function: %d\n", mul_func(2,3));
return 0;
}

```

```

Simple Conditional Compilation

```c
#include <stdio.h>
#define DEBUG 1

int main() {
#ifdef DEBUG
    printf("Debug mode is ON.\n");
#endif
    printf("Program running...\n");
    return 0;
}
```

Using #if/#else Directives

```c
#include <stdio.h>
#define PLATFORM 2  // 1 for Windows, 2 for Linux, etc.

int main() {
#if PLATFORM == 1
    printf("Running on Windows.\n");
#elif PLATFORM == 2
    printf("Running on Linux.\n");
#else
    printf("Unknown platform.\n");
#endif
    return 0;
}
```

Using #pragma

```c
#include <stdio.h>
#pragma message("Compiling " __FILE__ )

int main() {
    printf("Hello with a #pragma.\n");
    return 0;
}
```

Predefined Macros Demonstration

```c
#include <stdio.h>

int main() {
    printf("File: %s\n", __FILE__);
    printf("Date: %s\n", __DATE__);
    printf("Time: %s\n", __TIME__);
    printf("Line: %d\n", __LINE__);
    return 0;
}
```

Generate a Custom Compile-Time Error

```c
#if !defined(SOME_REQUIRED_MACRO)
#error "SOME_REQUIRED_MACRO is not defined!"
#endif

int main() {
    return 0;
}
```

Using #include from a Custom Header

myheader.h:

````c
#define GREETING "Hello from myheader!"
main.c:
```c
#include <stdio.h>
#include "myheader.h"

int main() {
    printf("%s\n", GREETING);
    return 0;
}
````

## Chapter 1: Exercises (10)

Define a macro MAX that takes two parameters and returns the larger of the two.
Write a C code that uses nested macros to compute x^4.
Demonstrate conditional compilation to compile code only when a “DEBUG” flag is defined.
Create a custom header file mathutils.h for constants and macros, then include it in a main program.
Use the predefined macros **DATE** and **TIME** to print the build timestamp.
Write a program that checks if a macro VERSION is defined, and if not, throws a compile-time error using #error.
Compare an inline function vs. macro performance for a loop calculating factorial (high-level analysis).
Implement a parameterized macro that swaps two variables of type int.
Use #ifdef to include a piece of code that prints “Beta Feature” only if BETA is defined.
Explore how #undef works by first defining a macro, then undefining it, and verifying that usage throws an error.

# Chapter 2: Pointers

2.1 Concept – Reference & Dereference
Description:

A pointer is a variable holding a memory address.
“Referencing” gets a variable’s address; “dereferencing” accesses the data at that address.
2.2 Declaration, Definition, Initialization & Use
Description:

Syntax: int \*ptr;
Must assign address of a valid variable (e.g., ptr = &x;).
2.3 Types of Pointers
Description:

Null pointer, Void pointer, Wild pointer, Dangling pointer, Function pointer.
2.4 Pointer Arithmetic
Description:

Operations on pointers: increment, decrement, subtraction, etc.
Depends on the data type size.
2.5 Multiple Indirection (Pointers to Pointers)
Description:

A pointer holding the address of another pointer (e.g., int \*\*pp).
2.6 Parameter Passing – Call by Value vs Call by Reference
Description:

In call-by-reference, the function can modify the caller’s variable via a pointer.
2.7 Arrays & Pointers
Description:

“Array of pointers” vs. “pointer to an array.”
2.8 Functions & Pointers
Description:

Passing pointer to function, returning pointer from function, function pointer usage.
2.9 Dynamic Memory Management
Description:

malloc, calloc, realloc, free, memory leaks, dangling pointers, best practices.
Chapter 2: Sample Programs (10)
Basic Pointer Declaration and Dereference

```c
#include <stdio.h>

int main() {
    int x = 10;
    int *ptr = &x;
    printf("Value of x via pointer: %d\n", *ptr);
    return 0;
}
```

Pointer Arithmetic

```c
#include <stdio.h>

int main() {
    int arr[3] = {10, 20, 30};

    int *p = arr;  // points to arr[0]
    printf("First element: %d\n", *p);
    p++; // moves to arr[1]
    printf("Second element: %d\n", *p);
    return 0;
}
```

Call by Value vs. Call by Reference

```c
#include <stdio.h>

void swapByValue(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}

void swapByRef(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x=5, y=10;
    swapByValue(x, y);  // won't affect the original
    printf("After swapByValue: x=%d y=%d\n", x, y);

    swapByRef(&x, &y);  // modifies original variables
    printf("After swapByRef: x=%d y=%d\n", x, y);
    return 0;
}
```

Pointer to Pointer

```c
#include <stdio.h>

int main() {
    int x = 50;
    int *p = &x;
    int **pp = &p;
    printf("Value of x using **pp: %d\n", **pp);
    return 0;
}
```

Array of Pointers

```c
#include <stdio.h>

int main() {
    char *colors[] = {"Red","Green","Blue"};

    for(int i=0; i<3; i++) {
        printf("%s\n", colors[i]);
    }

    return 0;
}
```

Pointer to an Array

```c
#include <stdio.h>

int main() {
    int arr[5] = {1,2,3,4,5};

    int (*ptr)[5] = &arr; // pointer to array of 5 ints
    for(int i=0; i<5; i++) {
        printf("%d ", (*ptr)[i]);
    }

    return 0;
}
```

Returning a Pointer from a Function

```c
#include <stdio.h>

int* getArray() {
    static int arr[3] = {11,22,33};

    return arr;
}

int main() {
    int *p = getArray();
    for(int i=0; i<3; i++){
        printf("%d ", p[i]);
    }

    return 0;
}
```

Function Pointer

```c
#include <stdio.h>

int add(int a, int b) { return a + b; }


int main() {
    int (*funcPtr)(int,int) = add;
    printf("Sum: %d\n", funcPtr(5, 7));
    return 0;
}
```

Dynamic Memory Allocation Using malloc

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n=5;
    int *p = (int*)malloc(n*sizeof(int));
    for(int i=0; i<n; i++){
        p[i] = i+1;
    }

    for(int i=0; i<n; i++){
        printf("%d ", p[i]);
    }

    free(p);
    return 0;
}
```

Using realloc

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p = (int*)malloc(3*sizeof(int));
    p[0] = 10;
    p[1] = 20;
    p[2] = 30;

    p = (int*)realloc(p, 5*sizeof(int));
    p[3] = 40;
    p[4] = 50;

    for(int i=0; i<5; i++){
        printf("%d ", p[i]);
    }

    free(p);
    return 0;
}
```

## Chapter 2: Exercises (10)

Write a program to sum the elements of an integer array using pointer arithmetic.
Create an array of pointers to strings and print them in reverse order.
Implement a function that returns a dynamically allocated array of prime numbers up to a limit.
Practice call by reference by creating a reverseDigits() function that reverses an integer in place.
Write a function pointer that points to different arithmetic operations (add, subtract, multiply, divide) and let the user choose.
Demonstrate pointer to pointer by creating a double pointer that modifies the original integer.
Implement a small memory leak scenario and show how to fix it with free().
Create a function returning pointer to float array that stores monthly rainfall. Print it in main().
Use calloc() to dynamically allocate an array of structures.
Write a program that resizes a dynamic array (using realloc) to add additional user inputs without losing old data.

# Chapter 3: Strings

## 3.1 Concept, Declaration, Definition, Initialization

Description:

Strings in C are arrays of characters ending with a null terminator \0.
Can be declared with fixed size (char str[20]) or as pointers (char \*p = "Hello";).

## 3.2 String Literals/Constants & Variables

Description:

String literal example: "Hello".
Stored typically in read-only memory; modifying them can cause errors.

## 3.3 Reading and Writing Strings

Description:

Functions like scanf("%s", str) or gets(str) (though gets() is unsafe).
Printing with printf("%s", str) or puts(str).
3.4 Strings & Pointers
Description:

char \*p = "Test"; pointer to literal vs. char arr[] = "Test"; array copy in local memory.

## 3.5 Array of Strings & Array of Character Pointers

Description:

E.g., char arr[5][10] vs. char \*strArr[5].

## 3.6 User Defined String Functions

Description:

E.g. int myStrlen(const char _), void myStrcpy(char _, const char \*), etc.

## 3.7 Predefined Functions in <string.h>

Description:

strlen, strcpy, strcat, strcmp, strcmpi, strrev, strlwr, strupr, strset, strchr, strrchr, strstr, strncpy, strncat, strncmp, strncmpi, strnset, strtok.

## 3.8 Command-Line Arguments (argc and argv)

Description:

argc gives number of arguments, argv is array of strings.
Used to read command-line parameters in main(int argc, char \*argv[]).

## Chapter 3: Sample Programs (10)

Basic String Initialization

```c
#include <stdio.h>

int main(){
    char str1[] = "Hello";
    char *str2 = "World";
    printf("%s %s\n", str1, str2);
    return 0;
}
```

Reading a String from User

```c
#include <stdio.h>

int main(){
    char name[50];
    printf("Enter your name: ");
    scanf("%49s", name); // limit input to avoid overflow
    printf("Hello %s\n", name);
    return 0;
}
```

Using strlen, strcpy, strcat

```c
#include <stdio.h>
#include <string.h>

int main(){
    char src[50] = "Hello";
    char dest[50] = "World";

    printf("Length of src: %lu\n", strlen(src));

    strcpy(dest, src);
    printf("After strcpy, dest: %s\n", dest);

    strcat(dest, " Everyone!");
    printf("After strcat, dest: %s\n", dest);

    return 0;
}
```

Comparing Strings (strcmp)

```c
#include <stdio.h>
#include <string.h>

int main(){
    char str1[] = "abc";
    char str2[] = "abd";
    int result = strcmp(str1, str2);

    if(result == 0) printf("Equal\n");
    else if(result < 0) printf("str1 < str2\n");
    else printf("str1 > str2\n");

    return 0;
}
```

Converting Case (strlwr, strupr)

```c
#include <stdio.h>
#include <string.h>

int main(){
    char text[] = "Hello C Language";

    printf("Lowercase: %s\n", strlwr(text));
    printf("Uppercase: %s\n", strupr(text));

    return 0;
}
```

Reverse a String (strrev)

```c
#include <stdio.h>
#include <string.h>

int main(){
    char word[] = "madam";
    strrev(word);
    printf("Reversed: %s\n", word);
    return 0;
}
```

Tokenizing a String (strtok)

```c
#include <stdio.h>
#include <string.h>

int main(){
    char input[] = "one,two,three";
    char *token = strtok(input, ",");

    while(token != NULL){
        printf("%s\n", token);
        token = strtok(NULL, ",");
    }
```

    return 0;

}

````

Find a Character in a String (strchr)

```c
#include <stdio.h>
#include <string.h>

int main(){
    char str[] = "Programming";
    char *pos = strchr(str, 'g');

    if(pos) {
        printf("First occurrence of 'g' found at index %ld\n", pos - str);
    }
````

    return 0;

}

````

Simple User-Defined myStrlen() Function

```c
#include <stdio.h>

int myStrlen(const char *str) {
    int count = 0;
    while(*str != '\0'){
        count++;
        str++;
    }
````

    return count;

}

```


int main(){
    char sample[] = "TestString";
    printf("Length: %d\n", myStrlen(sample));
    return 0;
}
```

Command-Line Arguments

```c
#include <stdio.h>

int main(int argc, char *argv[]){
    printf("Number of arguments: %d\n", argc);
    for(int i=0; i<argc; i++){
        printf("argv[%d] = %s\n", i, argv[i]);
    }
```

    return 0;

}

````

Chapter 3: Exercises (10)
Write a program to input a string and check if it is a palindrome (manually, without strrev).
Implement your own strcat function.
Convert the first letter of each word in a string to uppercase.
Count the occurrences of each vowel in a given string.
Split a string using a delimiter (e.g., |), then print tokens in reverse order.
Write a program to compare two strings ignoring case (implement your own strcmpi).
In a single string, replace all occurrences of a substring with another substring.
Read multiple lines of text from the user and store them in a two-dimensional character array. Print them.
Use command-line arguments to accept two numbers and print their sum, difference, and product.
Create a function that merges two sorted character arrays (like merging two sorted lists).

# Chapter 4: Structures
4.1 Concept, Declaration, Definition, Initialization
Description:

Structures (keyword struct) allow grouping of related variables (possibly of different types) under one name.
4.2 Accessing Structure Members
Description:

Use the dot operator (employee.id, student.name, etc.) to access members.
4.3 Array of Structures
Description:

E.g., struct Book library[100]; holds 100 Book records.
4.4 Pointers to Structures
Description:

struct Book *bptr; then bptr->price is used to access a member.
4.5 Structures & Functions
Description:

Pass a structure by value or by address.
Possible to return a structure from a function in C.
4.6 Nested Structures
Description:

A structure as a member of another structure.
4.7 typedef & Structures
Description:

Allows you to create an alias for a structure (e.g., typedef struct Book Book_t;).
4.8 Concept of Union
Description:

Similar syntax to structure but shares memory for all members.
Only one member is “active” at a time.

# Chapter 4: Sample Programs (10)
Basic Structure Declaration

```c
#include <stdio.h>

struct Student {
    int roll_no;
    float marks;
}
````

;

int main() {
struct Student s1 = {101, 88.5}

```
;
    printf("Roll no: %d, Marks: %.2f\n", s1.roll_no, s1.marks);
    return 0;
}
```

Array of Structures

```c
#include <stdio.h>

struct Employee {
    char name[50];
    float salary;
}
```

;

int main() {
struct Employee company[2] = {
{"Alice", 50000}

```
,
        {"Bob", 60000}
```

    }

```
;
    for(int i=0; i<2; i++){
        printf("Name: %s, Salary: %.2f\n", company[i].name, company[i].salary);
    }
```

    return 0;

}

````

Pointer to Structure

```c
#include <stdio.h>

struct Point {
    int x, y;
}
````

;

int main() {
struct Point p1 = {10, 20}

```
;
    struct Point *ptr = &p1;
    printf("Point via pointer: (%d, %d)\n", ptr->x, ptr->y);
    return 0;
}
```

Passing Structure by Value

```c
#include <stdio.h>

struct Rectangle {
    int length, width;
}
```

;

void printArea(struct Rectangle r){
printf("Area: %d\n", (r.length \* r.width));
}

```


int main(){
    struct Rectangle rect = {5, 10}
```

;
printArea(rect);
return 0;
}

````

Passing Structure by Reference

```c
#include <stdio.h>

struct Account {
    char owner[50];
    double balance;
}
````

;

void deposit(struct Account \*acc, double amount){
acc->balance += amount;
}

```


int main(){
    struct Account a = {"John Doe", 1000.0}
```

;
deposit(&a, 500.0);
printf("New balance: %.2f\n", a.balance);
return 0;
}

````

Returning a Structure from a Function

```c
#include <stdio.h>

struct Complex {
    float real, imag;
}
````

;

struct Complex createComplex(float r, float i){
struct Complex c;
c.real = r;
c.imag = i;
return c;
}

```


int main(){
    struct Complex num = createComplex(3.2, 4.5);
    printf("Complex number: %.2f + %.2fi\n", num.real, num.imag);
    return 0;
}
```

Nested Structure

```c
#include <stdio.h>

struct Date {
    int day, month, year;
}
```

;

struct Student {
char name[50];
struct Date dob;
}

```
;

int main(){
    struct Student s1 = {"Alice", {15, 8, 2002}
```

}

```
;
    printf("Name: %s, DOB: %d/%d/%d\n", s1.name, s1.dob.day, s1.dob.month, s1.dob.year);
    return 0;
}
```

typedef with Structure

```c
#include <stdio.h>

typedef struct {
    char title[50];
    char author[50];
    int pages;
}
```

Book;

int main(){
Book b1 = {"C Programming", "Dennis Ritchie", 250}

```
;
    printf("Title: %s, Author: %s, Pages: %d\n", b1.title, b1.author, b1.pages);
    return 0;
}
```

Union Example

```c
#include <stdio.h>

union Data {
    int i;
    float f;
    char str[20];
}
```

;

int main(){
union Data d;
d.i = 10;
printf("i: %d\n", d.i);

    d.f = 3.14;
    printf("f: %.2f\n", d.f);
    // here, d.i is overwritten by d.f
    return 0;

}

````

Structure vs. Union Memory Usage

```c
#include <stdio.h>

struct SData {
   int i;
   float f;
}
````

;

union UData {
int i;
float f;
}

```
;

int main(){
   printf("Size of struct: %lu\n", sizeof(struct SData));
   printf("Size of union: %lu\n", sizeof(union UData));
   return 0;
}
```

## Chapter 4: Exercises (10)

Create a struct Time with members (hours, minutes, seconds). Read two times from the user and add them.
Make an array of 5 student structures containing (rollNo, name, marks in 3 subjects). Print each student’s total and average.
Implement a program to compare two struct Complex numbers for equality.
Write a function to update an employee’s salary by reference.
Make a nested structure for struct Book containing another structure struct Author { name, country }

````
.
Demonstrate how typedef can simplify your program that uses multiple structures.
Create a union that holds multiple data types (int, float, and char array). Show how writing to one field can affect others.
Implement a small list of items for a store (id, name, price) in an array of structures. Write search logic by item name.
Return a structure from a function that calculates the rectangle’s perimeter and area (in a single struct).
Use pointers to structure to dynamically allocate memory for an array of N student records.

# Chapter 5: File Handling
5.1 Concept of Streams
Description:

A stream is an abstraction representing a device for I/O operations, e.g., reading/writing to a file or console.
5.2 Need and Types of Files
Description:

Text Files: Data stored in ASCII, human-readable.
Binary Files: Data stored in binary, smaller, faster but not human-readable.
5.3 Operations on Text & Binary Files
Description:

Opening, closing, reading, writing, appending, seeking, etc.
5.4 Random Access File
Description:

Access file contents at any position using fseek, ftell, rewind.
5.5 Library Functions for File Handling
Description:

fopen, fclose, fgetc, fgets, fputc, fputs, fread, fwrite, fseek, ftell, rewind, etc.
## Chapter 5: Sample Programs (10)
Writing to a Text File

```c
#include <stdio.h>

int main(){
    FILE *fp = fopen("test.txt", "w");
    if(fp == NULL){
        printf("Error opening file.\n");
        return 1;
    }
````

    fprintf(fp, "Hello file!\n");
    fclose(fp);
    return 0;

}

````

Reading from a Text File

```c
#include <stdio.h>

int main(){
    FILE *fp = fopen("test.txt", "r");
    if(!fp){
        printf("File not found!\n");
        return 1;
    }
````

    char line[100];
    while(fgets(line, sizeof(line), fp)){
        printf("%s", line);
    }

```

    fclose(fp);
    return 0;
}
```

Character-by-Character I/O (fgetc, fputc)

```c
#include <stdio.h>

int main(){
    FILE *fin = fopen("input.txt", "r");
    FILE *fout = fopen("output.txt", "w");
    int ch;

    while((ch = fgetc(fin)) != EOF){
        fputc(ch, fout);
    }
```

    fclose(fin);
    fclose(fout);
    return 0;

}

````

Appending to a File

```c
#include <stdio.h>

int main(){
    FILE *fp = fopen("data.log", "a");
    if(!fp){
        printf("Cannot open file.\n");
        return 1;
    }
````

    fprintf(fp, "New log entry.\n");
    fclose(fp);
    return 0;

}

````

Binary File Write (fwrite)

```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *fp = fopen("numbers.bin", "wb");
    if(!fp) return 1;
    int arr[5] = {1,2,3,4,5}
````

;
fwrite(arr, sizeof(int), 5, fp);
fclose(fp);
return 0;
}

````

Binary File Read (fread)

```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *fp = fopen("numbers.bin", "rb");
    if(!fp) return 1;
    int arr[5];
    fread(arr, sizeof(int), 5, fp);
    for(int i=0; i<5; i++){
        printf("%d ", arr[i]);
    }
````

    fclose(fp);
    return 0;

}

````

Using fseek and ftell

```c
#include <stdio.h>

int main(){
    FILE *fp = fopen("test.txt", "r");
    fseek(fp, 0, SEEK_END);
    long size = ftell(fp);
    printf("File size: %ld bytes\n", size);
    fclose(fp);
    return 0;
}
````

Inserting Data at a Specific Position (Random Access)

```c
#include <stdio.h>

int main(){
    FILE *fp = fopen("random.txt", "r+");
    // Move 10 bytes from the start
    fseek(fp, 10, SEEK_SET);
    fputs("INSERTED", fp);
    fclose(fp);
    return 0;
}
```

Reading and Writing a Structure

```c
#include <stdio.h>

struct Person {
    char name[50];
    int age;
}
```

;

int main() {
struct Person p1 = {"Alice", 25}

```
;

    FILE *fp = fopen("persons.dat", "wb");
    fwrite(&p1, sizeof(struct Person), 1, fp);
    fclose(fp);

    // Now read
    fp = fopen("persons.dat", "rb");
    struct Person p2;
    fread(&p2, sizeof(struct Person), 1, fp);
    printf("Name: %s, Age: %d\n", p2.name, p2.age);
    fclose(fp);

    return 0;
}
```

Copying Text File Lines to Another File with Line Numbers

```c
#include <stdio.h>

int main(){
   FILE *fin = fopen("source.txt", "r");
   FILE *fout = fopen("dest.txt", "w");
   if(!fin || !fout) return 1;

   char buffer[256];
   int lineNum = 1;
   while(fgets(buffer, sizeof(buffer), fin)){
       fprintf(fout, "%d: %s", lineNum++, buffer);
   }
```

fclose(fin);
fclose(fout);
return 0;
}

```


## Chapter 5: Exercises (10)

Write a program to count the number of lines, words, and characters in a text file.
Implement a program that takes a file name as command-line argument, reads the file, and displays it on the screen.
Create a text file “students.txt” that stores student records (rollNo, name, marks). Write a menu-based program to add and view records.
Convert a text file to uppercase by reading from one file and writing to another.
Append user-input lines to an existing file until the user enters “STOP”.
Create a binary file that stores an array of floats. Then read and print them.
Implement random access for a large text file: the user specifies a character position to jump to, and the program prints from that point onward.
Write a program that modifies the nth record in a binary file of structures.
Create an “encrypted” file by shifting each character by +2 in ASCII. Write a separate program to “decrypt” it.
Implement your own version of cp (copy) command that copies any file to another using fread and fwrite.
Review: 10 Questions and Answers
Below are some commonly asked questions covering the entire syllabus, with succinct answers.

Q: What is the purpose of the C preprocessor in a C program?
A: The C preprocessor handles macros, file inclusions, and conditional compilation before the main compilation process, transforming your source code into a modified form that the compiler then compiles.

Q: Differentiate between a macro and a function.
A: A macro is expanded inline by the preprocessor and can sometimes be faster but lacks type safety. A function has its own scope, is type-checked, and typically safer to debug.

Q: Explain pointer arithmetic.
A: Pointer arithmetic relies on the data type size. Incrementing a pointer moves it forward by the size (in bytes) of the data type it points to.

Q: How do you avoid a dangling pointer?
A: After freeing a pointer (or if a variable goes out of scope), do not use that pointer. You can set it to NULL to indicate it no longer points to valid data.

Q: What is the difference between an array of pointers and a pointer to an array?
A: An array of pointers is multiple pointer variables grouped together (char *arr[5]), while a pointer to an array is a single pointer that points to the entire array (int (*ptr)[5]).

Q: Why do we add a terminating '\0' in C strings?
A: C strings are null-terminated. The '\0' marks the end of the string in memory, so string-handling functions know where to stop.

Q: Explain how to pass a structure to a function by value vs. by reference.
A: By value copies the entire structure, meaning changes inside the function do not affect the original. By reference uses a pointer (struct MyStruct*), so changes inside do affect the original.

Q: What is a union, and how does it differ from a structure in memory usage?
A: A union overlays all members in the same memory space, so it only reserves memory equal to the size of its largest member. A structure allocates space for all members in sequence.

Q: How do you open a file for both reading and writing?
A: Use modes like "r+" or "w+". "r+" does not discard existing content and starts at the beginning, while "w+" overwrites the file or creates a new one if it doesn’t exist.

Q: What is the purpose of fseek and ftell?
A: fseek moves the file pointer to a specific location, while ftell returns the current position of the file pointer (in bytes from the start).
```
