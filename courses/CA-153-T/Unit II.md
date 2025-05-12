
# Unit II: 8051 Microcontroller (04 Hrs)

## Topics Covered:
1. Features of 8051 Microcontroller  
2. Block Diagram and Architecture of 8051  
3. Internal Memory Organization  
4. Special Function Registers (SFRs)  
5. PSW Register  
6. Pin Functions of 8051  
7. Structure of I/O Ports and Their Operation  
8. External Memory Interface  

---

## 1. Features of 8051 Microcontroller

- 8-bit microcontroller.
- 4 KB on-chip ROM.
- 128 bytes on-chip RAM.
- 32 I/O pins organized into 4 ports (P0–P3).
- Two 16-bit timers/counters.
- Full-duplex UART for serial communication.
- 5 interrupt sources.

---

## 2. Block Diagram and Architecture of 8051

The 8051 architecture includes:
- **CPU**: Executes instructions.
- **RAM**: Temporary data storage.
- **ROM**: Stores program code.
- **I/O Ports**: For interfacing external devices.
- **Timers/Counters**: For time-based operations.
- **Serial Port**: For communication.
- **Interrupt Controller**: Handles interrupts.

---

## 3. Internal Memory Organization

- **128 Bytes of RAM**:
  - 32 bytes for register banks.
  - 16 bytes for bit-addressable memory.
  - 80 bytes for general-purpose memory.

---

## 4. Special Function Registers (SFRs)

SFRs are used to control the operation of the microcontroller. Examples:
- **ACC**: Accumulator.
- **B**: Auxiliary register.
- **PSW**: Program Status Word.
- **SP**: Stack Pointer.

---

## 5. PSW Register

The PSW register contains flags for arithmetic operations:
- **CY**: Carry flag.
- **AC**: Auxiliary carry flag.
- **OV**: Overflow flag.
- **P**: Parity flag.

---

## 6. Pin Functions of 8051

- **Port 0 (P0)**: Dual-purpose (I/O or address/data bus).
- **Port 1 (P1)**: General-purpose I/O.
- **Port 2 (P2)**: Dual-purpose (I/O or higher address bus).
- **Port 3 (P3)**: Special-purpose I/O (e.g., serial communication).

---

## 7. Structure of I/O Ports and Their Operation

Each port has:
- **Latch**: Stores the output value.
- **Driver**: Drives the output.
- **Input Buffer**: Reads the input value.

---

## 8. External Memory Interface

The 8051 can interface with external memory using:
- **ALE (Address Latch Enable)**: Latches the lower address byte.
- **PSEN (Program Store Enable)**: Reads external program memory.
- **RD/WR**: Reads/writes external data memory.

---

### Example: Toggle LEDs on Port 1

```c
#include <reg51.h>

void delay() {
    int i, j;
    for (i = 0; i < 1000; i++) {
        for (j = 0; j < 100; j++);
    }
}

void main() {
    while (1) {
        P1 = 0xFF;  // Turn ON all LEDs
        delay();
        P1 = 0x00;  // Turn OFF all LEDs
        delay();
    }
}
```

This program toggles all LEDs connected to Port 1 of the 8051 microcontroller.

