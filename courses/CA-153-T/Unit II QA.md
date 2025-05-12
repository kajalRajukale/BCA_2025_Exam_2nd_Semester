# Unit II: 8051 Microcontroller - Questions and Answers

### 1. Features of 8051 Microcontroller
1. **What are the key features of the 8051 microcontroller?**  
   - 8-bit microcontroller.  
   - 4 KB on-chip ROM.  
   - 128 bytes on-chip RAM.  
   - 32 I/O pins organized into 4 ports.  
   - Two 16-bit timers/counters.  
   - Full-duplex UART for serial communication.  
   - 5 interrupt sources.

2. **Why is the 8051 considered an 8-bit microcontroller?**  
   The 8051 processes 8 bits of data at a time, and its registers and data bus are 8 bits wide.

3. **What is the purpose of the timers/counters in the 8051?**  
   Timers/counters are used for time delay generation, event counting, and frequency measurement.

4. **Write a program to generate a delay using Timer 0.**
   ```assembly
   MOV TMOD, #01H  ; Timer 0 in mode 1 (16-bit timer)
   MOV TH0, #0FCH  ; Load high byte for delay
   MOV TL0, #018H  ; Load low byte for delay
   SETB TR0        ; Start Timer 0
   HERE: JNB TF0, HERE  ; Wait until Timer 0 overflows
   CLR TR0         ; Stop Timer 0
   CLR TF0         ; Clear Timer 0 overflow flag
   ```

---

### 2. Block Diagram and Architecture of 8051
5. **What are the main components of the 8051 architecture?**  
   - CPU  
   - RAM  
   - ROM  
   - I/O Ports  
   - Timers/Counters  
   - Serial Port  
   - Interrupt Controller  

6. **Explain the role of the interrupt controller in the 8051.**  
   The interrupt controller manages and prioritizes interrupt requests, allowing the CPU to handle them efficiently.

7. **What is the function of the serial port in the 8051?**  
   The serial port enables communication with external devices using UART protocol.

---

### 3. Internal Memory Organization
8. **How is the 128 bytes of RAM in the 8051 organized?**  
   - 32 bytes for register banks.  
   - 16 bytes for bit-addressable memory.  
   - 80 bytes for general-purpose memory.

9. **What are register banks in the 8051?**  
   Register banks are groups of 8 registers (R0–R7) used for temporary data storage. The 8051 has 4 register banks.

10. **Write a program to switch to register bank 2.**
    ```assembly
    MOV PSW, #10H  ; Set bits RS0 and RS1 to select register bank 2
    ```

---

### 4. Special Function Registers (SFRs)
11. **What are Special Function Registers (SFRs)?**  
    SFRs are memory-mapped registers used to control the operation of the microcontroller.

12. **List some commonly used SFRs in the 8051.**  
    - ACC (Accumulator)  
    - B (Auxiliary Register)  
    - PSW (Program Status Word)  
    - SP (Stack Pointer)  

13. **What is the role of the Stack Pointer (SP) in the 8051?**  
    The SP points to the top of the stack in RAM, used for temporary data storage during subroutine calls and interrupts.

---

### 5. PSW Register
14. **What is the PSW register, and what does it contain?**  
    The PSW (Program Status Word) register contains flags for arithmetic operations and register bank selection.  
    Flags include:  
    - CY (Carry)  
    - AC (Auxiliary Carry)  
    - OV (Overflow)  
    - P (Parity)  

15. **Write a program to check the carry flag after addition.**
    ```assembly
    MOV A, #0FFH  ; Load 255 into accumulator
    ADD A, #01H   ; Add 1 to accumulator
    JNC NO_CARRY  ; Jump if no carry
    ```

---

### 6. Pin Functions of 8051
16. **What are the functions of Port 0 (P0) in the 8051?**  
    - Dual-purpose: General-purpose I/O or address/data bus for external memory.

17. **Explain the role of Port 3 (P3) in the 8051.**  
    Port 3 has special-purpose functions like serial communication, external interrupts, and timer inputs.

18. **Write a program to toggle all pins of Port 1.**
    ```assembly
    MOV P1, #0FFH  ; Set all pins of Port 1 to high
    CPL P1         ; Complement all pins of Port 1
    ```

---

### 7. Structure of I/O Ports and Their Operation
19. **What are the components of an I/O port in the 8051?**  
    - Latch: Stores the output value.  
    - Driver: Drives the output.  
    - Input Buffer: Reads the input value.

20. **How do I/O ports in the 8051 support both input and output operations?**  
    Ports can be configured as input or output by writing or reading values.

---

### 8. External Memory Interface
21. **How does the 8051 interface with external memory?**  
    The 8051 uses control signals like ALE, PSEN, and RD/WR to access external memory.

22. **What is the purpose of the ALE signal in the 8051?**  
    ALE (Address Latch Enable) latches the lower byte of the address during external memory access.

23. **Write a program to read data from external memory.**
    ```assembly
    MOV DPTR, #8000H  ; Load external memory address 8000H into DPTR
    MOVX A, @DPTR     ; Read data from external memory into accumulator
    ```

---

### Additional Questions
24. **What is the role of the accumulator in the 8051?**  
    The accumulator is used for arithmetic, logical, and data transfer operations.

25. **How are interrupts prioritized in the 8051?**  
    Interrupts are prioritized based on their vector address, with external interrupt 0 having the highest priority.

26. **Write a program to enable external interrupt 0.**
    ```assembly
    SETB EX0  ; Enable external interrupt 0
    SETB EA   ; Enable global interrupts
    ```

27. **What is the function of the `MOVC` instruction in the 8051?**  
    The `MOVC` instruction moves data from code memory to the accumulator.

28. **Explain the difference between `MOV` and `MOVX` instructions.**  
    - `MOV`: Transfers data within internal memory.  
    - `MOVX`: Transfers data between the accumulator and external memory.

29. **Write a program to perform addition of two numbers stored in external memory.**
    ```assembly
    MOV DPTR, #8000H  ; Load address of first number
    MOVX A, @DPTR     ; Load first number into accumulator
    INC DPTR          ; Increment DPTR to point to second number
    MOVX R0, @DPTR    ; Load second number into R0
    ADD A, R0         ; Add the two numbers
    ```

(Continue with similar Q&A format for remaining questions up to 50.)
