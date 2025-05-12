
# Unit IV: Timers and Counters (07 Hrs)

## Topics Covered:
1. Timer/Counter Registers: TMOD, TCON, SCON, SBUF, PCON  
2. Timer Modes  
3. Programming for Time Delay Using Mode 1 and Mode 2  

---

## 1. Timer/Counter Registers

### TMOD (Timer Mode Register):
- Configures the mode of operation for Timer 0 and Timer 1.
- **Bits**:
  - `GATE`: Enables/Disables timer operation via external pin.
  - `C/T`: Selects Timer (0) or Counter (1) mode.
  - `M1`, `M0`: Selects the mode (Mode 0, 1, 2, or 3).

### TCON (Timer Control Register):
- Controls the start/stop of timers and interrupt flags.
- **Bits**:
  - `TF1`: Timer 1 overflow flag.
  - `TR1`: Timer 1 run control bit.
  - `TF0`: Timer 0 overflow flag.
  - `TR0`: Timer 0 run control bit.

---

## 2. Timer Modes

### Mode 0:
- 13-bit timer mode.
- Timer counts from 0x0000 to 0x1FFF.

### Mode 1:
- 16-bit timer mode.
- Timer counts from 0x0000 to 0xFFFF.

### Mode 2:
- 8-bit auto-reload mode.
- Timer counts from 0x00 to a preset value.

---

## 3. Programming for Time Delay

### Example: Time Delay Using Mode 1
```c
#include <reg51.h>

void delay() {
    TMOD = 0x01;  // Timer 0, Mode 1
    TH0 = 0xFC;   // Load high byte
    TL0 = 0x66;   // Load low byte
    TR0 = 1;      // Start Timer 0
    while (TF0 == 0);  // Wait for overflow
    TR0 = 0;      // Stop Timer 0
    TF0 = 0;      // Clear overflow flag
}

void main() {
    while (1) {
        P1 = 0xFF;  // Turn ON LEDs
        delay();
        P1 = 0x00;  // Turn OFF LEDs
        delay();
    }
}
```

### Example: Time Delay Using Mode 2
```c
#include <reg51.h>

void delay() {
    TMOD = 0x02;  // Timer 0, Mode 2
    TH0 = 0xF8;   // Load auto-reload value
    TR0 = 1;      // Start Timer 0
    while (TF0 == 0);  // Wait for overflow
    TF0 = 0;      // Clear overflow flag
}

void main() {
    while (1) {
        P1 = 0xFF;  // Turn ON LEDs
        delay();
        P1 = 0x00;  // Turn OFF LEDs
        delay();
    }
}
```

These programs demonstrate how to use Timer 0 in Mode 1 and Mode 2 to create time delays.
