
# Unit V: Interrupts and Interfacing (06 Hrs)

## Topics Covered:
1. Introduction to Interrupts  
2. Interrupt Types and Their Vector Addresses  
3. Interrupt Enable Register and Interrupt Priority Register (IE, IP)  
4. Basics of Interfacing: ADC, DAC, LCD, Stepper Motor  

---

## 1. Introduction to Interrupts

Interrupts are signals that temporarily halt the execution of the main program to execute a specific task. Once the task is completed, the program resumes from where it was interrupted.

### Key Points:
- Interrupts improve the efficiency of a microcontroller by allowing it to respond to events as they occur.
- Interrupts can be hardware-based (e.g., external signals) or software-based (e.g., timers).

---

## 2. Interrupt Types and Their Vector Addresses

### Interrupt Types in 8051:
1. **External Interrupt 0 (INT0)**: Triggered by a low-level signal or edge on pin P3.2.
2. **Timer Interrupt 0 (TF0)**: Triggered when Timer 0 overflows.
3. **External Interrupt 1 (INT1)**: Triggered by a low-level signal or edge on pin P3.3.
4. **Timer Interrupt 1 (TF1)**: Triggered when Timer 1 overflows.
5. **Serial Interrupt (RI/TI)**: Triggered by serial communication events.

### Interrupt Vector Table:
Each interrupt has a fixed memory location (vector address) where the microcontroller jumps when the interrupt occurs.

| Interrupt         | Vector Address |
|-------------------|----------------|
| External INT0     | 0003H          |
| Timer 0 Overflow  | 000BH          |
| External INT1     | 0013H          |
| Timer 1 Overflow  | 001BH          |
| Serial Interrupt  | 0023H          |

---

## 3. Interrupt Enable Register and Interrupt Priority Register

### IE (Interrupt Enable Register):
- Enables or disables specific interrupts.
- **Bit Structure**:
  - EA: Global interrupt enable (1 = enable all interrupts).
  - ET2: Enable Timer 2 interrupt.
  - ES: Enable Serial interrupt.
  - ET1: Enable Timer 1 interrupt.
  - EX1: Enable External Interrupt 1.
  - ET0: Enable Timer 0 interrupt.
  - EX0: Enable External Interrupt 0.

### Example:
```c
IE = 0x85;  // Enable External INT0 and Timer 0 interrupts
```

### IP (Interrupt Priority Register):
- Sets the priority of interrupts (1 = high priority, 0 = low priority).
- **Bit Structure**:
  - PT2: Priority for Timer 2 interrupt.
  - PS: Priority for Serial interrupt.
  - PT1: Priority for Timer 1 interrupt.
  - PX1: Priority for External Interrupt 1.
  - PT0: Priority for Timer 0 interrupt.
  - PX0: Priority for External Interrupt 0.

### Example:
```c
IP = 0x01;  // Set high priority for External INT0
```

---

## 4. Basics of Interfacing

### 4.1 ADC (Analog-to-Digital Converter):
- Converts analog signals into digital values.
- Common ADC IC: ADC0804.
- **Interfacing Steps**:
  1. Connect analog input to the ADC.
  2. Configure control pins (e.g., Start, EOC).
  3. Read digital output from the ADC.

### Example:
```c
#include <reg51.h>

void main() {
    // ADC interfacing code here
}
```

---

### 4.2 DAC (Digital-to-Analog Converter):
- Converts digital values into analog signals.
- Common DAC IC: DAC0808.
- **Interfacing Steps**:
  1. Send digital data to DAC input pins.
  2. Configure reference voltage.
  3. Observe analog output.

---

### 4.3 LCD (Liquid Crystal Display):
- Used to display characters and numbers.
- Common LCD: 16x2.
- **Interfacing Steps**:
  1. Connect data pins (D0–D7) and control pins (RS, RW, EN).
  2. Initialize the LCD.
  3. Send data/commands to the LCD.

### Example:
```c
#include <reg51.h>

void lcd_init() {
    // LCD initialization code
}

void lcd_display(char *str) {
    // Code to display string on LCD
}

void main() {
    lcd_init();
    lcd_display("Hello, World!");
}
```

---

### 4.4 Stepper Motor:
- Converts electrical pulses into mechanical rotation.
- **Interfacing Steps**:
  1. Connect motor windings to microcontroller via driver IC (e.g., ULN2003).
  2. Send control signals to rotate the motor.

### Example:
```c
#include <reg51.h>

void stepper_rotate() {
    // Stepper motor rotation code
}

void main() {
    stepper_rotate();
}
```

---

## Practice Exercises

1. Write a program to toggle an LED using an external interrupt.
2. Interface an ADC with the 8051 microcontroller and display the digital value on an LCD.
3. Write a program to generate a square wave using a DAC.
4. Interface a stepper motor with the 8051 and rotate it clockwise and counterclockwise.
5. Configure Timer 0 interrupt to blink an LED at regular intervals.

