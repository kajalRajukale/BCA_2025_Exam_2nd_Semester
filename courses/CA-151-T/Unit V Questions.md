
# Unit V: File Handling - Questions and Answers

## Question 1: What is a file in C?
**Answer:**  
A file in C is a collection of data stored on a disk that can be read or written by a program.

---

## Question 2: What are the types of files in C?
**Answer:**  
- Text files: Store data in human-readable format.
- Binary files: Store data in binary format, which is not human-readable.

---

## Question 3: What is the purpose of file handling in C?
**Answer:**  
File handling allows programs to store, retrieve, and manipulate data in files for long-term storage.

---

## Question 4: What is a stream in C?
**Answer:**  
A stream is an abstraction that represents a sequence of bytes for input or output operations.

---

## Question 5: What are the standard streams in C?
**Answer:**  
- `stdin`: Standard input (keyboard).
- `stdout`: Standard output (console).
- `stderr`: Standard error (console).

---

## Question 6: How do you open a file in C?
**Answer:**  
You use the `fopen` function. Example:
```c
FILE *fp = fopen("file.txt", "r");
```

---

## Question 7: What are the modes available in `fopen`?
**Answer:**  
- `"r"`: Read mode.
- `"w"`: Write mode.
- `"a"`: Append mode.
- `"r+"`: Read and write mode.
- `"w+"`: Write and read mode.
- `"a+"`: Append and read mode.

---

## Question 8: How do you close a file in C?
**Answer:**  
You use the `fclose` function. Example:
```c
fclose(fp);
```

---

## Question 9: What is the purpose of the `FILE` pointer in C?
**Answer:**  
The `FILE` pointer is used to manage and access file operations.

---

## Question 10: How do you write data to a file in C?
**Answer:**  
You use functions like `fprintf`, `fputs`, or `fwrite`. Example:
```c
fprintf(fp, "Hello, World!");
```

---

## Question 11: How do you read data from a file in C?
**Answer:**  
You use functions like `fscanf`, `fgets`, or `fread`. Example:
```c
fgets(buffer, sizeof(buffer), fp);
```

---

## Question 12: What is the difference between `fgets` and `fgetc`?
**Answer:**  
- `fgets`: Reads a line of text.
- `fgetc`: Reads a single character.

---

## Question 13: How do you check for the end of a file?
**Answer:**  
You use the `feof` function. Example:
```c
while (!feof(fp)) {
    // Read data
}
```

---

## Question 14: What is the difference between text and binary files?
**Answer:**  
- Text files store data in human-readable format.
- Binary files store data in machine-readable format.

---

## Question 15: How do you write to a binary file in C?
**Answer:**  
You use the `fwrite` function. Example:
```c
fwrite(&data, sizeof(data), 1, fp);
```

---

## Question 16: How do you read from a binary file in C?
**Answer:**  
You use the `fread` function. Example:
```c
fread(&data, sizeof(data), 1, fp);
```

---

## Question 17: What is the purpose of the `fseek` function?
**Answer:**  
The `fseek` function moves the file pointer to a specific location in the file.

---

## Question 18: What are the arguments of `fseek`?
**Answer:**  
- `fp`: File pointer.
- `offset`: Number of bytes to move.
- `origin`: Starting point (`SEEK_SET`, `SEEK_CUR`, `SEEK_END`).

---

## Question 19: How do you get the current position of the file pointer?
**Answer:**  
You use the `ftell` function. Example:
```c
long pos = ftell(fp);
```

---

## Question 20: How do you rewind a file pointer to the beginning?
**Answer:**  
You use the `rewind` function. Example:
```c
rewind(fp);
```

---

## Question 21: What is the difference between `fscanf` and `fgets`?
**Answer:**  
- `fscanf`: Reads formatted input.
- `fgets`: Reads a line of text.

---

## Question 22: How do you append data to a file in C?
**Answer:**  
You open the file in append mode (`"a"` or `"a+"`) and write data.

---

## Question 23: What is a random access file?
**Answer:**  
A random access file allows you to read or write data at any position in the file.

---

## Question 24: How do you delete a file in C?
**Answer:**  
You use the `remove` function. Example:
```c
remove("file.txt");
```

---

## Question 25: How do you rename a file in C?
**Answer:**  
You use the `rename` function. Example:
```c
rename("old.txt", "new.txt");
```

---

## Question 26: What is the purpose of the `perror` function?
**Answer:**  
The `perror` function prints an error message related to the last file operation.

---

## Question 27: How do you check if a file exists in C?
**Answer:**  
You use the `fopen` function and check if the returned pointer is `NULL`.

---

## Question 28: What is the difference between `fputc` and `fputs`?
**Answer:**  
- `fputc`: Writes a single character.
- `fputs`: Writes a string.

---

## Question 29: How do you handle errors in file operations?
**Answer:**  
You check the return value of file functions and use `perror` or `errno`.

---

## Question 30: How do you count the number of lines in a text file?
**Answer:**  
You read the file line by line and count the occurrences of newline characters.

---

## Question 31: How do you copy the contents of one file to another?
**Answer:**  
You read from the source file and write to the destination file.

---

## Question 32: How do you read a file character by character?
**Answer:**  
You use the `fgetc` function in a loop.

---

## Question 33: How do you write a structure to a binary file?
**Answer:**  
You use the `fwrite` function. Example:
```c
fwrite(&structVar, sizeof(structVar), 1, fp);
```

---

## Question 34: How do you read a structure from a binary file?
**Answer:**  
You use the `fread` function. Example:
```c
fread(&structVar, sizeof(structVar), 1, fp);
```

---

## Question 35: How do you check if a file is open?
**Answer:**  
You check if the `FILE` pointer is `NULL`.

---

## Question 36: What is the purpose of the `fflush` function?
**Answer:**  
The `fflush` function clears the output buffer.

---

## Question 37: How do you write formatted data to a file?
**Answer:**  
You use the `fprintf` function. Example:
```c
fprintf(fp, "Name: %s, Age: %d\n", name, age);
```

---

## Question 38: How do you read formatted data from a file?
**Answer:**  
You use the `fscanf` function. Example:
```c
fscanf(fp, "%s %d", name, &age);
```

---

## Question 39: How do you count the number of words in a text file?
**Answer:**  
You read the file word by word and count the occurrences.

---

## Question 40: How do you count the number of characters in a text file?
**Answer:**  
You read the file character by character and count the occurrences.

---

## Question 41: How do you handle binary files in C?
**Answer:**  
You use `fread` and `fwrite` for reading and writing binary data.

---

## Question 42: How do you truncate a file in C?
**Answer:**  
You open the file in write mode (`"w"`) to clear its contents.

---

## Question 43: How do you check the size of a file in C?
**Answer:**  
You use `fseek` and `ftell` to determine the file size.

---

## Question 44: How do you read a file line by line?
**Answer:**  
You use the `fgets` function in a loop.

---

## Question 45: How do you handle file permissions in C?
**Answer:**  
You use system calls like `chmod` or check permissions using `access`.

---

## Question 46: How do you create a temporary file in C?
**Answer:**  
You use the `tmpfile` function.

---

## Question 47: How do you write an array to a binary file?
**Answer:**  
You use the `fwrite` function. Example:
```c
fwrite(array, sizeof(int), size, fp);
```

---

## Question 48: How do you read an array from a binary file?
**Answer:**  
You use the `fread` function. Example:
```c
fread(array, sizeof(int), size, fp);
```

---

## Question 49: How do you handle file paths in C?
**Answer:**  
You use relative or absolute paths in the `fopen` function.

---

## Question 50: How do you handle multiple files in C?
**Answer:**  
You use multiple `FILE` pointers to manage multiple files simultaneously.
