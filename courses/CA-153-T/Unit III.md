
# Unit III: 8051 Programmer's Model (09 Hrs)

## Topics Covered:
1. Introduction to Assembly Programming  
2. Compilers and Assemblers  
3. Instruction Classification and Instruction Set  
4. Addressing Modes: Immediate, Register, Direct, Indirect, and Relative  
5. Assembler Directives (ORG, END)  
6. Features with Examples  
7. Introduction to 8051 Programming in C  

---

## 1. Introduction to Assembly Programming

Assembly programming involves writing low-level code that directly interacts with the hardware. It uses mnemonics to represent machine instructions.

### Example:
```asm
MOV A, #55H  ; Load immediate value 55H into accumulator A
ADD A, #0AH  ; Add immediate value 0AH to A
```

---

## 2. Compilers and Assemblers

- **Compiler**: Converts high-level language (e.g., C) into machine code.
- **Assembler**: Converts assembly language into machine code.

---

## 3. Instruction Classification and Instruction Set

### Instruction Classification:
1. **Data Transfer Instructions**: MOV, PUSH, POP.
2. **Arithmetic Instructions**: ADD, SUBB, MUL, DIV.
3. **Logical Instructions**: ANL, ORL, XRL.
4. **Branching Instructions**: SJMP, LJMP, AJMP, JZ, JNZ.

### Example:
```asm
MOV A, #0AH  ; Load 0AH into A
ADD A, #05H  ; Add 05H to A
```

---

## 4. Addressing Modes

### Immediate Addressing:
The operand is a constant value.
```asm
MOV A, #55H  ; Load 55H into A
```

### Register Addressing:
The operand is a register.
```asm
MOV A, R0  ; Copy the value of R0 into A
```

### Direct Addressing:
The operand is a memory address.
```asm
MOV A, 30H  ; Copy the value at memory address 30H into A
```

### Indirect Addressing:
The operand is a memory address pointed to by a register.
```asm
MOV A, @R0  ; Copy the value at the address in R0 into A
```

### Relative Addressing:
Used in branching instructions.
```asm
SJMP LABEL  ; Jump to LABEL
```

---

## 5. Assembler Directives

### ORG:
Defines the starting address of the program.
```asm
ORG 0000H
```

### END:
Indicates the end of the program.
```asm
END
```

---

## 6. Features with Examples

### Example: Add Two Numbers
```asm
ORG 0000H
MOV A, #0AH  ; Load 10 into A
ADD A, #05H  ; Add 5 to A
END
```

---

## 7. Introduction to 8051 Programming in C

### Example: Toggle an LED
```c
#include <reg51.h>

sbit LED = P1^0;  // Define LED at Port 1, Pin 0

void delay() {
    int i, j;
    for (i = 0; i < 1000; i++) {
        for (j = 0; j < 100; j++);
    }
}

void main() {
    while (1) {
        LED = ~LED;  // Toggle LED
        delay();
    }
}
```

This program toggles an LED connected to Port 1, Pin 0 of the 8051 microcontroller.
