# Lab Course on CA-153-T: Questions and Answers

### 1. Study of 8051 Microcontroller Chip and Keil µVision-5
1. **What is the purpose of the Keil µVision-5 IDE?**  
   Keil µVision-5 is an integrated development environment used for writing, compiling, and debugging programs for microcontrollers.

2. **How do you create a new project in Keil µVision-5?**  
   - Open Keil µVision-5.  
   - Go to `Project > New µVision Project`.  
   - Select the target microcontroller.  
   - Add source files and start coding.

---

### 2. Study of Proteus Simulator for 8051 Simulation
3. **What is Proteus Simulator?**  
   Proteus is a simulation software used to design and test circuits, including microcontroller-based systems.

4. **How do you simulate an 8051 program in Proteus?**  
   - Create a circuit with the 8051 microcontroller.  
   - Load the compiled hex file into the 8051.  
   - Run the simulation to observe the output.

---

### 3. Program to Find Largest/Smallest from a Series
5. **Write a program to find the largest number in an array.**
   ```c
   #include <reg51.h>

   void main() {
       unsigned char arr[] = {10, 25, 5, 15};
       unsigned char max = arr[0];
       unsigned char i;

       for (i = 1; i < 4; i++) {
           if (arr[i] > max) {
               max = arr[i];
           }
       }

       P1 = max;  // Display the largest number on Port 1
       while (1);
   }
   ```

6. **Write a program to find the smallest number in an array.**
   ```c
   #include <reg51.h>

   void main() {
       unsigned char arr[] = {10, 25, 5, 15};
       unsigned char min = arr[0];
       unsigned char i;

       for (i = 1; i < 4; i++) {
           if (arr[i] < min) {
               min = arr[i];
           }
       }

       P1 = min;  // Display the smallest number on Port 1
       while (1);
   }
   ```

---

### 4. Program to Perform Arithmetic Operations
7. **Write a program to add two 8-bit numbers.**
   ```c
   #include <reg51.h>

   void main() {
       unsigned char a = 0x12, b = 0x34, sum;
       sum = a + b;
       P1 = sum;  // Display the result on Port 1
       while (1);
   }
   ```

8. **Write a program to multiply two 8-bit numbers.**
   ```c
   #include <reg51.h>

   void main() {
       unsigned char a = 5, b = 3, product;
       product = a * b;
       P1 = product;  // Display the result on Port 1
       while (1);
   }
   ```

---

### 5. Interfacing of LED/LEDs to 8051 Microcontroller
9. **How do you interface an LED with the 8051 microcontroller?**  
   An LED is connected to a microcontroller pin through a current-limiting resistor. The pin is toggled to turn the LED ON or OFF.

10. **Write a program to blink an LED connected to Port 1, Pin 0.**
    ```c
    #include <reg51.h>

    sbit LED = P1^0;  // Define LED connected to Port 1, Pin 0

    void delay() {
        int i, j;
        for (i = 0; i < 1000; i++) {
            for (j = 0; j < 100; j++);
        }
    }

    void main() {
        while (1) {
            LED = 1;  // Turn ON LED
            delay();
            LED = 0;  // Turn OFF LED
            delay();
        }
    }
    ```

---

### 6. Interfacing of Switch and LED to 8051 Microcontroller
11. **Write a program to control an LED using a switch.**
    ```c
    #include <reg51.h>

    sbit SWITCH = P1^1;  // Define switch connected to Port 1, Pin 1
    sbit LED = P1^0;     // Define LED connected to Port 1, Pin 0

    void main() {
        while (1) {
            if (SWITCH == 0) {  // If switch is pressed
                LED = 1;        // Turn ON LED
            } else {
                LED = 0;        // Turn OFF LED
            }
        }
    }
    ```

---

### 7. Traffic Light Controller Using 8051 Microcontroller
12. **Write a program to simulate a traffic light controller.**
    ```c
    #include <reg51.h>

    sbit RED = P1^0;    // Red light
    sbit YELLOW = P1^1; // Yellow light
    sbit GREEN = P1^2;  // Green light

    void delay() {
        int i, j;
        for (i = 0; i < 1000; i++) {
            for (j = 0; j < 100; j++);
        }
    }

    void main() {
        while (1) {
            RED = 1; YELLOW = 0; GREEN = 0;  // Red light ON
            delay();
            RED = 0; YELLOW = 1; GREEN = 0;  // Yellow light ON
            delay();
            RED = 0; YELLOW = 0; GREEN = 1;  // Green light ON
            delay();
        }
    }
    ```

---

### 8. Interfacing LCD to 8051 Microcontroller
13. **Write a program to display "HELLO" on an LCD.**
    ```c
    #include <reg51.h>

    sbit RS = P2^0;  // Register Select
    sbit EN = P2^1;  // Enable
    sbit RW = P2^2;  // Read/Write

    void delay() {
        int i, j;
        for (i = 0; i < 1000; i++) {
            for (j = 0; j < 100; j++);
        }
    }

    void lcd_command(unsigned char cmd) {
        P1 = cmd;
        RS = 0; RW = 0; EN = 1;
        delay();
        EN = 0;
    }

    void lcd_data(unsigned char data) {
        P1 = data;
        RS = 1; RW = 0; EN = 1;
        delay();
        EN = 0;
    }

    void main() {
        lcd_command(0x38);  // Initialize LCD
        lcd_command(0x0C);  // Display ON, Cursor OFF
        lcd_command(0x01);  // Clear display
        lcd_command(0x80);  // Move to first line

        lcd_data('H');
        lcd_data('E');
        lcd_data('L');
        lcd_data('L');
        lcd_data('O');

        while (1);
    }
    ```

---

(Continue with similar Q&A format for remaining assignments up to 50.)
