## Unit III: Strings (05 Hrs)

- Concept, Declaration, definition, initialization, format specifiers, String literals/ constants & variables – reading & writing from & to console, Importance of terminating NULL character, Strings & pointers
- Array of strings & array of character pointers, User defined functions, predefined functions in string.h - strlen, strcpy, strcat, strcmp, strcmpi, strrev, strlwr, strupr, strset, strchr, strrchr, strstr, strncpy, strncat, strncmp, strncmpi, strnset, strtok, Command line arguments – argc and argv

---

# Chapter 3: Strings

Strings in C are arrays of characters terminated by a special character called the **null terminator** (`'\0'`). This chapter introduces the declaration, definition, and usage of strings in C, the relevant library functions from `string.h`, and how to handle command-line arguments.

---

## 1. Concept of Strings in C

1. **Definition**:

   - A string in C is essentially a sequence of characters ending with a null character `'\0'`.
   - For example, the string literal `"Hello"` actually occupies 6 characters in memory: `'H'`, `'e'`, `'l'`, `'l'`, `'o'`, and `'\0'`.

2. **String Literals**:

   - These are constant character arrays, e.g. `"Hello World"`.
   - Stored typically in a read-only segment of memory.

3. **Importance of the Null Character**:
   - `'\0'` (ASCII code `0`) signifies the end of a string. Functions in `string.h` rely on finding this character to know where the string ends.

---

## 2. Declaration, Definition, and Initialization

1. **Declaration**:
   ```c
   char str[10]; // can hold up to 9 characters + '\0'
   ```

Definition:
You allocate actual memory for str (e.g., char str[10] = "Hello";).
Initialization:
Compile-time:

```c
char greet[] = "Hello";
// greet has space for 'H', 'e', 'l', 'l', 'o', '\0'
Run-time (reading from console):
```

```c
char name[20];
printf("Enter name: ");
scanf("%19s", name); // safe: ensures no overflow beyond 19 chars + '\0'
```

Format Specifiers
For string input and output, use %s with scanf and printf.
Make sure the destination array is large enough to hold the string and the terminating null character.

# 3. Strings & Pointers

Strings as Arrays:
A string can be manipulated through array notation: str[i].

Strings as Pointers:

```c
char *p = "Hello";
// p points to the first character 'H', stored in read-only memory
```

You cannot modify the contents of "Hello" through p in most compilers (undefined behavior), but p itself can be changed to point elsewhere.

Pointer Arithmetic:

If p points to a string, _(p + i) accesses the i-th character.
Example: p[i] and _(p + i) are equivalent.

# 4. Array of Strings & Array of Character Pointers

Array of Strings:

```
char arr[3][10] = {"One", "Two", "Three"};
// Memory is allocated contiguously for 3 strings, each up to 9 chars + '\0'
```

Array of Character Pointers:

```c
char *cities[] = {"Delhi", "Mumbai", "Chennai"};
// Each element is a pointer to a string literal
```

Here each pointer in cities[i] points to string constants that could be stored in read-only memory.

# 5. Predefined Functions in <string.h>

C provides numerous useful functions for string manipulation:

## Function Description

- strlen(s) Returns length of s (not counting '\0')
- strcpy(d, s) Copies string s into d (assumes d is large enough)
- strcat(d, s) Appends s to the end of d
- strcmp(a, b) Compares a and b lexicographically (<0, 0, or >0)
- strcmpi(a,b) 
- - stricmp(a,b) Compares case-insensitively (non-standard on some compilers; might be \_stricmp in others)
- strrev(s) Reverses string s (compiler-specific, not standard C)
- strlwr(s) Converts string s to lowercase (compiler-specific, not standard C)
- strupr(s) Converts string s to uppercase (compiler-specific, not standard C)
- strset(s, c) Sets all characters in s to c (compiler-specific)
- strchr(s, c) Returns pointer to the first occurrence of c in s, or NULL if not found
- strrchr(s,c) Returns pointer to the last occurrence of c in s
- strstr(a, b) Returns pointer to first occurrence of substring b in a, or NULL if absent
- strncpy(d,s,n) Copies up to n characters from s to d
- strncat(d,s,n) Appends up to n characters of s onto d
- strncmp(a,b,n) Compares up to n characters of a and b
- strncmpi(a,b,n) Case-insensitive variant, compiler-specific
- strnset(s,c,n) Sets first n characters of s to c, non-standard library function
- strtok(s, del) Splits string s into tokens using del (delimiter string)

## Implementation notes:

Some functions like stricmp, strupr, strlwr, etc., may not be part of the ISO C standard but are often available in common C compilers.
Always ensure the destination buffer is big enough for the resulting string plus the null terminator.

# 6. Command-Line Arguments: argc and argv

In C, you can handle command-line arguments via main(int argc, char \*argv[]):

argc: Argument Count, the number of arguments passed to the program (including the program name itself).
argv: Argument Vector, an array of C-strings containing each argument.
For example, if you run the program:

```
./a.out Hello 123
```

argc will be 3.
argv[0] = "./a.out", argv[1] = "Hello", argv[2] = "123".
Example

```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("Number of arguments: %d\n", argc);
    for(int i = 0; i < argc; i++) {
        printf("argv[%d] = %s\n", i, argv[i]);
    }
    return 0;
}
```

# 7. Code Examples

Example 1: String Copy and Concatenate

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char first[20] = "Hello";
    char second[20] = "World";
    char combined[40];

    // Copy first to combined
    strcpy(combined, first);
    // Append space and then second
    strcat(combined, " ");
    strcat(combined, second);

    printf("Combined: %s\n", combined);  // "Hello World"
    return 0;
}
```

Example 2: Using strtok to Split a String

````c
#include <stdio.h>
#include <string.h>

int main(void) {
    char line[50] = "apple,banana,orange";
    char *token = strtok(line, ",");

    while(token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, ",");
    }
    return 0;
}
Splits line by the delimiter , and prints each fruit on a new line.

Example 3: Command Line Argument Usage
```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    if(argc < 2) {
        printf("Usage: %s <some string>\n", argv[0]);
        return 1;
    }
    printf("You entered: %s\n", argv[1]);
    return 0;
}
````

# 8. Practice Exercises

## Reading and Writing Strings

Write a program that asks the user for a string (up to 30 characters) and prints it backward. Use strlen and array notation to accomplish this.

## Case Conversion

Prompt the user for a string, then convert it to uppercase (if your compiler provides strupr). If not, write your own loop to convert each character manually.

## String Compare

Write a function compareStrings(const char *a, const char *b) that mimics strcmp. It should return negative, zero, or positive depending on how a and b compare lexicographically.

## Substring Search

Accept two strings from the user, str1 and str2. Use strstr to check if str2 is a substring of str1. Print the position if found, otherwise a message saying it’s not found.

## Tokenizing a Sentence

Read a sentence from the user, then split it into words using strtok. Print each word on a separate line.

## Command Line Calculator

Using command-line arguments, build a program that does ./calc <num1> <num2> and prints their sum or product (you decide). Make sure to handle error cases (like not enough arguments).

# 9. End-of-Chapter Question

Question:

Explain the importance of the null terminator in C strings. What would happen if a string did not contain '\0'?

Consider how the '\0' is used by standard library functions, including potential issues like buffer overflows or reading uninitialized memory.
