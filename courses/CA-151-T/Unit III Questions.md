
# Unit III: Strings - Questions and Answers

## Question 1: What is a string in C?
**Answer:**  
A string in C is an array of characters terminated by a null character (`'\0'`).

---

## Question 2: How do you declare a string in C?
**Answer:**  
You declare a string as a character array. Example:
```c
char str[10];
```

---

## Question 3: What is the importance of the null character in strings?
**Answer:**  
The null character (`'\0'`) marks the end of a string, allowing functions like `strlen` to determine its length.

---

## Question 4: How do you initialize a string in C?
**Answer:**  
You can initialize a string during declaration. Example:
```c
char str[] = "Hello";
```

---

## Question 5: What is the difference between `char str[]` and `char *str`?
**Answer:**  
- `char str[]`: Allocates memory for the string and stores it in the array.
- `char *str`: Points to a string literal stored in read-only memory.

---

## Question 6: How do you read a string from the console?
**Answer:**  
You can use `scanf` or `gets` (not recommended due to buffer overflow risks). Example:
```c
char str[20];
scanf("%19s", str);
```

---

## Question 7: How do you print a string in C?
**Answer:**  
You can use `printf` with the `%s` format specifier. Example:
```c
printf("%s", str);
```

---

## Question 8: What is the difference between a string literal and a string variable?
**Answer:**  
- A string literal is a constant string stored in read-only memory.
- A string variable is a modifiable array of characters.

---

## Question 9: How do you find the length of a string in C?
**Answer:**  
You use the `strlen` function from `<string.h>`. Example:
```c
int len = strlen(str);
```

---

## Question 10: How do you copy one string to another in C?
**Answer:**  
You use the `strcpy` function. Example:
```c
strcpy(dest, src);
```

---

## Question 11: How do you concatenate two strings in C?
**Answer:**  
You use the `strcat` function. Example:
```c
strcat(dest, src);
```

---

## Question 12: How do you compare two strings in C?
**Answer:**  
You use the `strcmp` function. Example:
```c
int result = strcmp(str1, str2);
```

---

## Question 13: What is the difference between `strcmp` and `strncmp`?
**Answer:**  
- `strcmp`: Compares entire strings.
- `strncmp`: Compares up to `n` characters of two strings.

---

## Question 14: How do you reverse a string in C?
**Answer:**  
You can use the `strrev` function (compiler-specific) or write a custom loop.

---

## Question 15: How do you convert a string to lowercase in C?
**Answer:**  
You can use the `strlwr` function (compiler-specific) or iterate through the string and use `tolower`.

---

## Question 16: How do you convert a string to uppercase in C?
**Answer:**  
You can use the `strupr` function (compiler-specific) or iterate through the string and use `toupper`.

---

## Question 17: How do you find the first occurrence of a character in a string?
**Answer:**  
You use the `strchr` function. Example:
```c
char *pos = strchr(str, 'a');
```

---

## Question 18: How do you find the last occurrence of a character in a string?
**Answer:**  
You use the `strrchr` function. Example:
```c
char *pos = strrchr(str, 'a');
```

---

## Question 19: How do you find a substring in a string?
**Answer:**  
You use the `strstr` function. Example:
```c
char *pos = strstr(str, "sub");
```

---

## Question 20: How do you tokenize a string in C?
**Answer:**  
You use the `strtok` function. Example:
```c
char *token = strtok(str, " ");
```

---

## Question 21: What is the difference between `strcpy` and `strncpy`?
**Answer:**  
- `strcpy`: Copies the entire string.
- `strncpy`: Copies up to `n` characters.

---

## Question 22: What is the difference between `strcat` and `strncat`?
**Answer:**  
- `strcat`: Concatenates the entire string.
- `strncat`: Concatenates up to `n` characters.

---

## Question 23: How do you compare strings case-insensitively?
**Answer:**  
You use `strcmpi` or `_stricmp` (compiler-specific).

---

## Question 24: How do you set all characters in a string to a specific character?
**Answer:**  
You use the `strset` function (compiler-specific). Example:
```c
strset(str, 'x');
```

---

## Question 25: How do you set the first `n` characters of a string to a specific character?
**Answer:**  
You use the `strnset` function (compiler-specific). Example:
```c
strnset(str, 'x', n);
```

---

## Question 26: How do you handle command-line arguments in C?
**Answer:**  
You use `argc` and `argv` in the `main` function. Example:
```c
int main(int argc, char *argv[]) {
    printf("First argument: %s\n", argv[1]);
    return 0;
}
```

---

## Question 27: What is `argc` in command-line arguments?
**Answer:**  
`argc` is the argument count, representing the number of arguments passed to the program.

---

## Question 28: What is `argv` in command-line arguments?
**Answer:**  
`argv` is the argument vector, an array of strings representing the arguments passed to the program.

---

## Question 29: How do you check if a string is a palindrome?
**Answer:**  
You compare the string with its reverse.

---

## Question 30: How do you convert a string to an integer in C?
**Answer:**  
You use the `atoi` function. Example:
```c
int num = atoi(str);
```

---

## Question 31: How do you convert a string to a floating-point number in C?
**Answer:**  
You use the `atof` function. Example:
```c
float num = atof(str);
```

---

## Question 32: How do you convert an integer to a string in C?
**Answer:**  
You use the `sprintf` function. Example:
```c
sprintf(str, "%d", num);
```

---

## Question 33: How do you convert a floating-point number to a string in C?
**Answer:**  
You use the `sprintf` function. Example:
```c
sprintf(str, "%f", num);
```

---

## Question 34: How do you find the length of a string without using `strlen`?
**Answer:**  
You iterate through the string until you encounter `'\0'`.

---

## Question 35: How do you copy a string without using `strcpy`?
**Answer:**  
You use a loop to copy each character until `'\0'`.

---

## Question 36: How do you concatenate strings without using `strcat`?
**Answer:**  
You use a loop to append characters from the second string to the first.

---

## Question 37: How do you compare strings without using `strcmp`?
**Answer:**  
You compare characters one by one until a difference is found or `'\0'` is reached.

---

## Question 38: How do you reverse a string without using `strrev`?
**Answer:**  
You swap characters from the start and end of the string moving toward the center.

---

## Question 39: How do you tokenize a string without using `strtok`?
**Answer:**  
You manually split the string by searching for delimiters.

---

## Question 40: How do you handle multi-word strings in C?
**Answer:**  
You use `fgets` to read the entire line. Example:
```c
fgets(str, sizeof(str), stdin);
```

---

## Question 41: How do you remove trailing newline characters from a string?
**Answer:**  
You check for `'\n'` at the end of the string and replace it with `'\0'`.

---

## Question 42: How do you count the number of vowels in a string?
**Answer:**  
You iterate through the string and check for vowels (`a, e, i, o, u`).

---

## Question 43: How do you count the number of words in a string?
**Answer:**  
You count spaces or use `strtok` to count tokens.

---

## Question 44: How do you find the frequency of characters in a string?
**Answer:**  
You use an array to count occurrences of each character.

---

## Question 45: How do you remove duplicate characters from a string?
**Answer:**  
You iterate through the string and remove duplicates by shifting characters.

---

## Question 46: How do you sort characters in a string?
**Answer:**  
You use a sorting algorithm like bubble sort or quicksort.

---

## Question 47: How do you find the longest word in a string?
**Answer:**  
You use `strtok` to split the string and compare word lengths.

---

## Question 48: How do you replace a substring in a string?
**Answer:**  
You search for the substring and replace it by shifting characters.

---

## Question 49: How do you split a string into lines?
**Answer:**  
You use `strtok` with `'\n'` as the delimiter.

---

## Question 50: How do you handle strings with dynamic memory allocation?
**Answer:**  
You use `malloc` to allocate memory for the string and `free` to release it.
