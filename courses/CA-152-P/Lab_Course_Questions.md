
# Lab Course on CA-151-T - Questions and Answers

## Question 1: What is the purpose of preprocessor directives in C?
**Answer:**  
Preprocessor directives modify the source code before compilation. They handle tasks like file inclusion, macro expansion, and conditional compilation.

---

## Question 2: How do you use `#define` to create a macro in C?
**Answer:**  
You use `#define` to define a macro. Example:
```c
#define PI 3.14159
```

---

## Question 3: How do you include a custom header file in a C program?
**Answer:**  
Use `#include "filename.h"` to include a custom header file.

---

## Question 4: How do you demonstrate the use of `#ifdef` in a program?
**Answer:**  
```c
#ifdef DEBUG
    printf("Debug mode enabled.\n");
#endif
```

---

## Question 5: How do you write a program to swap two numbers using pointers?
**Answer:**  
```c
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
```

---

## Question 6: How do you dynamically allocate memory for an integer array in C?
**Answer:**  
Use `malloc`. Example:
```c
int *arr = (int *)malloc(5 * sizeof(int));
```

---

## Question 7: How do you free dynamically allocated memory in C?
**Answer:**  
Use the `free` function. Example:
```c
free(arr);
```

---

## Question 8: How do you demonstrate the use of a function pointer in C?
**Answer:**  
```c
int add(int a, int b) {
    return a + b;
}

int (*func_ptr)(int, int) = add;
```

---

## Question 9: How do you implement a linked list in C?
**Answer:**  
Use a self-referential structure:
```c
struct Node {
    int data;
    struct Node *next;
};
```

---

## Question 10: How do you reverse a string using pointers in C?
**Answer:**  
Use two pointers to swap characters from the start and end of the string.

---

## Question 11: How do you read a string from the console in C?
**Answer:**  
Use `fgets`. Example:
```c
fgets(str, sizeof(str), stdin);
```

---

## Question 12: How do you concatenate two strings in C?
**Answer:**  
Use the `strcat` function. Example:
```c
strcat(dest, src);
```

---

## Question 13: How do you compare two strings in C?
**Answer:**  
Use the `strcmp` function. Example:
```c
int result = strcmp(str1, str2);
```

---

## Question 14: How do you tokenize a string in C?
**Answer:**  
Use the `strtok` function. Example:
```c
char *token = strtok(str, " ");
```

---

## Question 15: How do you demonstrate the use of command-line arguments in C?
**Answer:**  
```c
int main(int argc, char *argv[]) {
    printf("First argument: %s\n", argv[1]);
    return 0;
}
```

---

## Question 16: How do you declare and initialize a structure in C?
**Answer:**  
```c
struct Student {
    int id;
    char name[50];
};

struct Student s1 = {1, "John"};
```

---

## Question 17: How do you pass a structure to a function in C?
**Answer:**  
Pass by value or by reference:
```c
void display(struct Student s);
void display(struct Student *s);
```

---

## Question 18: How do you access structure members using a pointer?
**Answer:**  
Use the arrow operator (`->`). Example:
```c
printf("ID: %d\n", ptr->id);
```

---

## Question 19: How do you demonstrate the use of a union in C?
**Answer:**  
```c
union Data {
    int i;
    float f;
};

union Data d;
d.i = 10;
```

---

## Question 20: How do you write data to a text file in C?
**Answer:**  
Use `fprintf`. Example:
```c
fprintf(fp, "Hello, World!");
```

---

## Question 21: How do you read data from a text file in C?
**Answer:**  
Use `fgets`. Example:
```c
fgets(buffer, sizeof(buffer), fp);
```

---

## Question 22: How do you write data to a binary file in C?
**Answer:**  
Use `fwrite`. Example:
```c
fwrite(&data, sizeof(data), 1, fp);
```

---

## Question 23: How do you read data from a binary file in C?
**Answer:**  
Use `fread`. Example:
```c
fread(&data, sizeof(data), 1, fp);
```

---

## Question 24: How do you demonstrate the use of `fseek` in C?
**Answer:**  
```c
fseek(fp, 0, SEEK_END);
```

---

## Question 25: How do you demonstrate the use of `ftell` in C?
**Answer:**  
```c
long pos = ftell(fp);
```

---

## Question 26: How do you demonstrate the use of `rewind` in C?
**Answer:**  
```c
rewind(fp);
```

---

## Question 27: How do you delete a file in C?
**Answer:**  
Use the `remove` function. Example:
```c
remove("file.txt");
```

---

## Question 28: How do you rename a file in C?
**Answer:**  
Use the `rename` function. Example:
```c
rename("old.txt", "new.txt");
```

---

## Question 29: How do you demonstrate the use of `#pragma` in C?
**Answer:**  
```c
#pragma message("Compiling " __FILE__)
```

---

## Question 30: How do you demonstrate the use of `#error` in C?
**Answer:**  
```c
#error "This is a compile-time error."
```

---

## Question 31: How do you demonstrate the use of `#undef` in C?
**Answer:**  
```c
#undef PI
```

---

## Question 32: How do you demonstrate the use of a nested structure in C?
**Answer:**  
```c
struct Address {
    char city[50];
};

struct Student {
    int id;
    struct Address addr;
};
```

---

## Question 33: How do you demonstrate the use of a self-referential structure in C?
**Answer:**  
```c
struct Node {
    int data;
    struct Node *next;
};
```

---

## Question 34: How do you demonstrate the use of a constant pointer in C?
**Answer:**  
```c
int *const ptr = &x;
```

---

## Question 35: How do you demonstrate the use of a pointer to a constant in C?
**Answer:**  
```c
const int *ptr = &x;
```

---

## Question 36: How do you demonstrate the use of a constant pointer to a constant in C?
**Answer:**  
```c
const int *const ptr = &x;
```

---

## Question 37: How do you demonstrate the use of bit fields in a structure?
**Answer:**  
```c
struct Flags {
    unsigned int flag1 : 1;
    unsigned int flag2 : 1;
};
```

---

## Question 38: How do you demonstrate the use of a 2D array with pointers?
**Answer:**  
```c
int **arr = (int **)malloc(rows * sizeof(int *));
```

---

## Question 39: How do you demonstrate the use of a function returning a pointer?
**Answer:**  
```c
int* findMax(int *a, int *b) {
    return (*a > *b) ? a : b;
}
```

---

## Question 40: How do you demonstrate the use of a dynamic array in C?
**Answer:**  
```c
int *arr = (int *)malloc(n * sizeof(int));
```

---

## Question 41: How do you demonstrate the use of a stack using structures?
**Answer:**  
Use a structure to represent the stack and its elements.

---

## Question 42: How do you demonstrate the use of a queue using structures?
**Answer:**  
Use a structure to represent the queue and its elements.

---

## Question 43: How do you demonstrate the use of a binary tree using structures?
**Answer:**  
Use a self-referential structure to represent tree nodes.

---

## Question 44: How do you demonstrate the use of `strrev` in C?
**Answer:**  
```c
strrev(str);
```

---

## Question 45: How do you demonstrate the use of `strlwr` in C?
**Answer:**  
```c
strlwr(str);
```

---

## Question 46: How do you demonstrate the use of `strupr` in C?
**Answer:**  
```c
strupr(str);
```

---

## Question 47: How do you demonstrate the use of `strncpy` in C?
**Answer:**  
```c
strncpy(dest, src, n);
```

---

## Question 48: How do you demonstrate the use of `strncat` in C?
**Answer:**  
```c
strncat(dest, src, n);
```

---

## Question 49: How do you demonstrate the use of `strncmp` in C?
**Answer:**  
```c
strncmp(str1, str2, n);
```

---

## Question 50: How do you demonstrate the use of `strtok` with multiple delimiters?
**Answer:**  
```c
char *token = strtok(str, " ,;");
```
