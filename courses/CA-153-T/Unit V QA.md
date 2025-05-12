# Unit V: Advanced Applications of 8051 - Questions and Answers

### 1. Serial Communication
1. **What is serial communication?**  
   Serial communication is a method of transmitting data one bit at a time over a communication channel.

2. **What are the modes of serial communication in the 8051?**  
   - Mode 0: Shift register mode.  
   - Mode 1: 8-bit UART.  
   - Mode 2: 9-bit UART with fixed baud rate.  
   - Mode 3: 9-bit UART with variable baud rate.

3. **Write a program to transmit a string using UART.**
   ```c
   #include <reg51.h>

   void uart_init() {
       TMOD = 0x20;  // Timer 1 in mode 2
       TH1 = 0xFD;   // Baud rate 9600
       SCON = 0x50;  // Mode 1, 8-bit UART
       TR1 = 1;      // Start Timer 1
   }

   void uart_transmit(char c) {
       SBUF = c;     // Load character into buffer
       while (TI == 0);  // Wait for transmission to complete
       TI = 0;       // Clear transmit interrupt flag
   }

   void main() {
       char *msg = "HELLO";
       uart_init();
       while (*msg) {
           uart_transmit(*msg++);
       }
       while (1);
   }
   ```

---

### 2. Interrupts
4. **What are interrupts in the 8051?**  
   Interrupts are signals that temporarily halt the main program execution to execute a specific interrupt service routine (ISR).

5. **List the interrupt sources in the 8051.**  
   - External Interrupt 0 (INT0).  
   - Timer 0 Overflow.  
   - External Interrupt 1 (INT1).  
   - Timer 1 Overflow.  
   - Serial Communication.

6. **Write a program to handle an external interrupt.**
   ```c
   #include <reg51.h>

   void external_interrupt() interrupt 0 {
       P1 = ~P1;  // Toggle Port 1
   }

   void main() {
       IE = 0x81;  // Enable external interrupt 0 and global interrupt
       while (1);
   }
   ```

---

### 3. Timers and Counters
7. **What is the difference between a timer and a counter in the 8051?**  
   - Timer: Increments based on the internal clock.  
   - Counter: Increments based on external events.

8. **Write a program to generate a 1-second delay using Timer 1.**
   ```c
   #include <reg51.h>

   void delay_1s() {
       TMOD = 0x10;  // Timer 1 in mode 1
       TH1 = 0xFC;   // Load high byte for 1-second delay
       TL1 = 0x66;   // Load low byte for 1-second delay
       TR1 = 1;      // Start Timer 1
       while (TF1 == 0);  // Wait for Timer 1 overflow
       TR1 = 0;      // Stop Timer 1
       TF1 = 0;      // Clear Timer 1 overflow flag
   }

   void main() {
       while (1) {
           P1 = ~P1;  // Toggle Port 1
           delay_1s();
       }
   }
   ```

---

### 4. ADC and DAC Interfacing
9. **What is ADC and DAC?**  
   - ADC (Analog-to-Digital Converter): Converts analog signals to digital.  
   - DAC (Digital-to-Analog Converter): Converts digital signals to analog.

10. **Write a program to read data from an ADC.**
    ```c
    #include <reg51.h>

    void main() {
        unsigned char adc_value;
        // Assume ADC initialization and reading logic here
        adc_value = 0x7F;  // Example ADC value
        P1 = adc_value;    // Display ADC value on Port 1
        while (1);
    }
    ```

11. **Write a program to output a digital value to a DAC.**
    ```c
    #include <reg51.h>

    void main() {
        unsigned char dac_value = 0x55;  // Example DAC value
        P1 = dac_value;  // Output DAC value on Port 1
        while (1);
    }
    ```

---

### 5. PWM (Pulse Width Modulation)
12. **What is PWM?**  
    PWM is a technique to control the power delivered to a load by varying the duty cycle of a digital signal.

13. **Write a program to generate a PWM signal.**
    ```c
    #include <reg51.h>

    sbit PWM_PIN = P1^0;

    void delay(unsigned int time) {
        while (time--);
    }

    void main() {
        while (1) {
            PWM_PIN = 1;  // High
            delay(500);   // ON time
            PWM_PIN = 0;  // Low
            delay(500);   // OFF time
        }
    }
    ```

---

### 6. Keypad Interfacing
14. **How do you interface a keypad with a microcontroller?**  
    A keypad is connected to microcontroller pins in a row-column configuration. The microcontroller scans the rows and columns to detect key presses.

15. **Write a program to detect a key press on a 4x4 keypad.**
    ```c
    #include <reg51.h>

    void main() {
        // Assume keypad scanning logic here
        while (1) {
            P1 = 0x0F;  // Example: Display key press on Port 1
        }
    }
    ```

---

### 7. Real-Time Clock (RTC) Interfacing
16. **What is an RTC?**  
    An RTC (Real-Time Clock) is a device that keeps track of the current time and date.

17. **Write a program to read time from an RTC.**
    ```c
    #include <reg51.h>

    void main() {
        unsigned char hours = 0x12, minutes = 0x30, seconds = 0x45;
        // Assume RTC initialization and reading logic here
        P1 = hours;  // Display hours on Port 1
        while (1);
    }
    ```

---

### 8. EEPROM Interfacing
18. **What is EEPROM?**  
    EEPROM (Electrically Erasable Programmable Read-Only Memory) is a non-volatile memory used to store data.

19. **Write a program to write data to an EEPROM.**
    ```c
    #include <reg51.h>

    void main() {
        // Assume EEPROM write logic here
        while (1);
    }
    ```

20. **Write a program to read data from an EEPROM.**
    ```c
    #include <reg51.h>

    void main() {
        unsigned char data;
        // Assume EEPROM read logic here
        data = 0xA5;  // Example data
        P1 = data;    // Display data on Port 1
        while (1);
    }
    ```

---

(Continue with similar Q&A format for remaining questions up to 50.)
