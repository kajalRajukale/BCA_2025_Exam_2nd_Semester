```markdown
# Table of Contents

1. [Chapter 1: Preprocessor](#chapter-1-preprocessor)  
    1. [1.1 Concept and Format of Preprocessor Directives](#11-concept-and-format-of-preprocessor-directives)  
    2. [1.2 File Inclusion Directives](#12-file-inclusion-directives)  
    3. [1.3 Macro Substitution Directives](#13-macro-substitution-directives)  
    4. [1.4 Macros vs Functions](#14-macros-vs-functions)  
    5. [1.5 Conditional Compilation](#15-conditional-compilation)  
    6. [1.6 Other Directives](#16-other-directives)  
    7. [Chapter 1: Sample Programs (10)](#chapter-1-sample-programs-10)  
    8. [Chapter 1: Exercises (10)](#chapter-1-exercises-10)

2. [Chapter 2: Pointers](#chapter-2-pointers)  
    1. [2.1 Concept – Reference & Dereference](#21-concept--reference--dereference)  
    2. [2.2 Declaration, Definition, Initialization & Use](#22-declaration-definition-initialization--use)  
    3. [2.3 Types of Pointers](#23-types-of-pointers)  
    4. [2.4 Pointer Arithmetic](#24-pointer-arithmetic)  
    5. [2.5 Multiple Indirection (Pointers to Pointers)](#25-multiple-indirection-pointers-to-pointers)  
    6. [2.6 Parameter Passing – Call by Value vs Call by Reference](#26-parameter-passing--call-by-value-vs-call-by-reference)  
    7. [2.7 Arrays & Pointers](#27-arrays--pointers)  
    8. [2.8 Functions & Pointers](#28-functions--pointers)  
    9. [2.9 Dynamic Memory Management](#29-dynamic-memory-management)  
    10. [Chapter 2: Sample Programs (10)](#chapter-2-sample-programs-10)  
    11. [Chapter 2: Exercises (10)](#chapter-2-exercises-10)

3. [Chapter 3: Strings](#chapter-3-strings)  
    1. [3.1 Concept, Declaration, Definition, Initialization](#31-concept-declaration-definition-initialization)  
    2. [3.2 String Literals/Constants & Variables](#32-string-literalsconstants--variables)  
    3. [3.3 Reading and Writing Strings](#33-reading-and-writing-strings)  
    4. [3.4 Strings & Pointers](#34-strings--pointers)  
    5. [3.5 Array of Strings & Array of Character Pointers](#35-array-of-strings--array-of-character-pointers)  
    6. [3.6 User Defined String Functions](#36-user-defined-string-functions)  
    7. [3.7 Predefined Functions in `<string.h>`](#37-predefined-functions-in-stringh)  
    8. [3.8 Command-Line Arguments](#38-command-line-arguments)  
    9. [Chapter 3: Sample Programs (10)](#chapter-3-sample-programs-10)  
    10. [Chapter 3: Exercises (10)](#chapter-3-exercises-10)

4. [Chapter 4: Structures](#chapter-4-structures)  
    1. [4.1 Concept, Declaration, Definition, Initialization](#41-concept-declaration-definition-initialization)  
    2. [4.2 Accessing Structure Members](#42-accessing-structure-members)  
    3. [4.3 Array of Structures](#43-array-of-structures)  
    4. [4.4 Pointers to Structures](#44-pointers-to-structures)  
    5. [4.5 Structures & Functions](#45-structures--functions)  
    6. [4.6 Nested Structures](#46-nested-structures)  
    7. [4.7 `typedef` & Structures](#47-typedef--structures)  
    8. [4.8 Concept of Union](#48-concept-of-union)  
    9. [Chapter 4: Sample Programs (10)](#chapter-4-sample-programs-10)  
    10. [Chapter 4: Exercises (10)](#chapter-4-exercises-10)

5. [Chapter 5: File Handling](#chapter-5-file-handling)  
    1. [5.1 Concept of Streams](#51-concept-of-streams)  
    2. [5.2 Need and Types of Files](#52-need-and-types-of-files)  
    3. [5.3 Operations on Text & Binary Files](#53-operations-on-text--binary-files)  
    4. [5.4 Random Access File](#54-random-access-file)  
    5. [5.5 Library Functions for File Handling](#55-library-functions-for-file-handling)  
    6. [Chapter 5: Sample Programs (10)](#chapter-5-sample-programs-10)  
    7. [Chapter 5: Exercises (10)](#chapter-5-exercises-10)

6. [Review: 10 Questions and Answers](#review-10-questions-and-answers)

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
- Predefined macros (e.g., `__DATE__`, `__TIME__`, `__LINE__`, `__FILE__`, `__STDC__`).

---

## Chapter 1: Sample Programs (10)

### 1. Basic Macro Definition
```c
#include <stdio.h>
#define PI 3.14159

int main() {
     printf("Value of PI: %f\n", PI);
     return 0;
}
```

### 2. Parameterized Macro
```c
#include <stdio.h>
#define SQUARE(x) ((x) * (x))

int main() {
     int num = 5;
     printf("Square of %d is %d\n", num, SQUARE(num));
     return 0;
}
```

### 3. Nested Macro
```c
#include <stdio.h>
#define DOUBLE(x) ((x) + (x))
#define QUADRUPLE(x) DOUBLE(DOUBLE(x))

int main() {
     printf("Quadruple of 3: %d\n", QUADRUPLE(3));
     return 0;
}
```

### 4. Macro vs. Inline Function Speed Check (Conceptual snippet)
```c
#include <stdio.h>
#define MUL(a, b) ((a) * (b))

inline int mul_func(int a, int b) { 
     return a * b; 
}

int main() {
     printf("Macro: %d\n", MUL(2, 3));
     printf("Function: %d\n", mul_func(2, 3));
     return 0;
}
```

### 5. Simple Conditional Compilation
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

### 6. Using `#if/#else` Directives
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

### 7. Using `#pragma`
```c
#include <stdio.h>
#pragma message("Compiling " __FILE__ )

int main() {
     printf("Hello with a #pragma.\n");
     return 0;
}
```

### 8. Predefined Macros Demonstration
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

### 9. Generate a Custom Compile-Time Error
```c
#if !defined(SOME_REQUIRED_MACRO)
#error "SOME_REQUIRED_MACRO is not defined!"
#endif

int main() {
     return 0;
}
```

### 10. Using `#include` from a Custom Header
**myheader.h:**
```c
#define GREETING "Hello from myheader!"
```

**main.c:**
```c
#include <stdio.h>
#include "myheader.h"

int main() {
     printf("%s\n", GREETING);
     return 0;
}
```

---

## Chapter 1: Exercises (10)

1. Define a macro `MAX` that takes two parameters and returns the larger of the two.
2. Write a C code that uses nested macros to compute `x^4`.
3. Demonstrate conditional compilation to compile code only when a `DEBUG` flag is defined.
4. Create a custom header file `mathutils.h` for constants and macros, then include it in a main program.
5. Use the predefined macros `__DATE__` and `__TIME__` to print the build timestamp.
6. Write a program that checks if a macro `VERSION` is defined, and if not, throws a compile-time error using `#error`.
7. Compare an inline function vs. macro performance for a loop calculating factorial (high-level analysis).
8. Implement a parameterized macro that swaps two variables of type `int`.
9. Use `#ifdef` to include a piece of code that prints “Beta Feature” only if `BETA` is defined.
10. Explore how `#undef` works by first defining a macro, then undefining it, and verifying that usage throws an error.
```
