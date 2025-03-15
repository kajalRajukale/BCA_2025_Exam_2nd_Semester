## Unit I: Preprocessor (06 Hrs)  
- Concept
- Format of preprocessor directives
- File inclusion directives (#include)
- Macro substitution directives (#define)
- nested macros
- parameterized macros, 
- Macros versus functions
  - #error / #pragma directives
  - Conditional compilation (#if/#ifdef/#else/#elif/#endif)
  - Predefined macros (_DATE_ / _TIME_ /_FILE_ /_LINE_/ _STDC_)  

---

# 1: C Preprocessor

The C Preprocessor is a powerful tool that modifies your program **before** the actual compilation step. It helps manage code inclusion, macro expansion, conditional compilation, and more. Below is a structured study guide covering the **C Preprocessor** in depth, along with explanations, code examples, practice exercises, and a single end-of-chapter question.

---

## 1. Introduction to the C Preprocessor

The C Preprocessor works on your source code before the compiler translates it to machine code. It performs tasks like:
- Including header files (e.g., standard library headers)
- Expanding macros
- Enabling conditional compilation
- Generating errors or warnings

This step happens *textually*, which means the preprocessor edits the code in memory, substituting or removing text based on various directives you write.

Key Preprocessor Directives include:
- `#include`
- `#define`
- `#if`, `#ifdef`, `#ifndef`, `#else`, `#elif`, `#endif`
- `#error`
- `#pragma`
- Predefined macros (`__DATE__`, `__TIME__`, `__FILE__`, `__LINE__`, `__STDC__`)

---

## 2. Format of Preprocessor Directives

All preprocessor directives in C:
1. Begin with a **hash** symbol (`#`) in the first column.
2. May have zero or more spaces after the hash.
3. Are *not* terminated by a semicolon.

Common forms:
```c
#include <header_file>   // For system headers
#include "header_file"   // For user-defined headers

#define MACRO_NAME replacement_text
#define MACRO_FUNC(arg)  (some_expression)

#if CONDITION
   // code
#endif
```

Preprocessor directives may appear anywhere in your code, though conventionally they appear near the top of a file.

## 3. File Inclusion Directives: #include

### 3.1 Concept

The #include directive inserts the contents of another file into the source code.
Often used to include library headers (stdio.h, stdlib.h, etc.).

#### 3.2 Two Main Forms

Angle Brackets – #include <stdio.h>

Tells the compiler to look in the system’s standard include path.
Double Quotes – #include "myheader.h"
Tells the compiler to look in the current directory first, then system directories.

### 3.3 Example

```c
#include <stdio.h>
#include "myutils.h" // Suppose this is a custom header in your project

int main(void) {
    printf("Hello from #include demo!\n");
    return 0;
}
```

## 4. Macro Substitution Directives: #define
A macro is a fragment of code or text that the preprocessor will replace wherever it finds that macro’s name in the source.

### 4.1 Simple Object-like Macros

```c
#define PI 3.14159
#define HELLO "Hello, World!"

int main(void) {
    printf("%s\n", HELLO);
    printf("The value of PI is %f\n", PI);
    return 0;
}
```

In this code, PI and HELLO are replaced by their definitions before compilation.

### 4.2 Nested Macros
Macros can expand to other macros. Careful usage is important to avoid confusion.

```c
#define SIZE 10
#define LENGTH SIZE

int arr[LENGTH]; // arr[10]
4.3 Parameterized Macros (Function-like Macros)
Macros can take arguments:

```c
#define SQUARE(x) ((x) * (x))

int main(void) {
    int num = 5;
    printf("Square of %d is %d\n", num, SQUARE(num));
    return 0;
}
```

Warning: Macros do not perform type-checking, and parentheses in the definition help avoid precedence bugs.

## 4.4 Macros vs. Functions

Macros are expanded at compile-time (textual replacement) and can make code faster but can bloat size and lose type safety.
Functions are compiled once and can be used repeatedly without duplicating code, but they incur a function call overhead.

## 5. Other Directives

### 5.1 #error

Generates a compiler error message:

```c
#if !defined(PLATFORM)
    #error "PLATFORM not defined. Please define PLATFORM before compiling."
#endif
```

This stops compilation with the error message shown.

### 5.2 #pragma

A compiler-specific directive often used to enable or disable certain features or warnings. Common usage:

```c
#pragma warning(disable : 4996)  // Example (MSVC) to disable specific warnings
Exact behavior depends on the compiler implementation.
```

## 6. Conditional Compilation
Conditional directives allow parts of your program to compile only if certain conditions are met. They are extremely helpful for:

Cross-platform code
Enabling or disabling debug features

### 6.1 Basic Directives

#if / #endif
#ifdef / #endif
#ifndef / #endif
#else
#elif

#### Example:

```c
#include <stdio.h>

#define DEBUG 1

int main(void) {
#if DEBUG
    printf("Debug build. Extra logging enabled.\n");
#else
    printf("Release build. Logging disabled.\n");
#endif
    return 0;
}
```

### 6.2 Another Example with #ifdef

```c
#ifdef PI
#undef PI
#endif
#define PI 3.14
```

If PI was previously defined, undefine it.
Then define it as 3.14.

## 7. Predefined Macros
The C compiler supplies several macros by default:

__DATE__ – The compilation date (in "Mmm dd yyyy" format).
__TIME__ – The compilation time (in "hh:mm:ss" format).
__FILE__ – The current filename as a string.
__LINE__ – The current line number as a decimal constant.
__STDC__ – Defined as 1 if the implementation is ISO-compliant.


### Example

```c
#include <stdio.h>

int main(void) {
    printf("This code is compiled on %s at %s\n", __DATE__, __TIME__);
    printf("File name: %s\n", __FILE__);
    printf("Line: %d\n", __LINE__);
#ifdef __STDC__
    printf("This compiler is compliant with ANSI C.\n");
#endif
    return 0;
}
```

## 8. Code Examples

Below are a few short examples demonstrating preprocessor concepts.

### Example 1: Conditional Compilation with Debug Logging

```c
#include <stdio.h>

//#define ENABLE_DEBUG

int main(void) {
#ifdef ENABLE_DEBUG
    printf("Debug: Starting main function...\n");
#endif

    printf("Hello, preprocessor!\n");

#ifdef ENABLE_DEBUG
    printf("Debug: Exiting main function...\n");
#endif

    return 0;
}
```

Compile once with #define ENABLE_DEBUG to enable logs, or comment it out to disable logs.

### Example 2: Using Function-Like Macro vs. Inline Function
```c
#include <stdio.h>

#define CUBE_MACRO(x) ((x)*(x)*(x))

inline int cube_function(int x) {
    return x * x * x;
}

int main(void) {
    int n = 3;
    // Macro
    printf("Macro: %d cubed = %d\n", n, CUBE_MACRO(n));
    // Function
    printf("Function: %d cubed = %d\n", n, cube_function(n));
    return 0;
}
```

Observe that both produce the same result. However, the macro is expanded textually, whereas the inline function is subject to the compiler’s inline expansion.

### Example 3: Generating Errors with #error
```c
#if defined(_WIN32) || defined(_WIN64)
  // Windows-specific code
#elif defined(__linux__)
  // Linux-specific code
#else
#error "Unsupported platform. Only Windows or Linux supported."
#endif
```

### Example 4: Macro with Multiple Arguments
```c
#include <stdio.h>

#define MIN(a,b) ((a)<(b)?(a):(b))

int main(void) {
    int x = 10, y = 20;
    printf("Minimum is %d\n", MIN(x,y));
    return 0;
}
```

## 9. Practice Exercises

Try the following short programming exercises to reinforce these concepts:

### Header File Creation

Create a custom header file named mathutils.h that has a macro for computing the product of two numbers. Write a C program to test it.

### Nested Macros

Define two macros ONE and TWO, then define a third macro that uses the first two macros. Print out their expanded values to ensure they are replaced correctly.

### Parameterized Macro

Write a macro ABS(x) that returns the absolute value of x. Demonstrate how parentheses are crucial to avoid errors.

### Macro vs. Function

Implement a parameterized macro and a function that both calculate the average of two integers. Compare how each is used, and see if any type-related issues arise.

### Conditional Compilation

Create a program that prints “Testing Mode” if a certain macro is defined, otherwise prints “Production Mode.”

### Predefined Macros

Print the file name, line number, current date, and time in a short program. Observe how these values change or remain the same in multiple runs.

## 10. End-of-Chapter Question

Discuss how the C Preprocessor can help in creating platform-independent code. Illustrate with a short example that demonstrates using conditional compilation for multiple operating systems.

Think about how different platforms (Windows, Linux, macOS) might require different library functions or system calls, and how #if, #ifdef, etc. can selectively compile each block.

## Key Takeaways
Preprocessing occurs before compilation, transforming source code based on your directives.

Macros can simplify code, but can also introduce subtle errors if not carefully designed.

Conditional Compilation is extremely helpful for managing debugging code or platform-dependent sections.

Predefined Macros provide helpful metadata about your build environment.

By mastering the C Preprocessor, you gain control over compilation, enabling more flexible and maintainable code.
