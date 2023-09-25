---
title: "IDTs"
draft: false
---

Ref. [https://dev.to/frosnerd/writing-my-own-keyboard-driver-16kh](https://dev.to/frosnerd/writing-my-own-keyboard-driver-16kh) - for more about keyboard drivers and IDTs.
**Interrupt Descriptor Table (IDT)**:
- The IDT is a data structure in the x86 architecture that provides a mapping between interrupt numbers and their corresponding interrupt handler routines.
- It is used to manage various types of interrupts, including hardware interrupts (IRQs) and software interrupts (system calls, exceptions).
- Each entry in the IDT is called a Gate and contains information about the interrupt handler's location and privilege level.
- Types of Gates: Interrupt Gates, Trap Gates, Task Gates.
    - Interrupt Gates: Used for hardware-generated interrupts like timer interrupts (IRQ0) or keyboard interrupts (IRQ1).
    - Trap Gates: Used for software-generated interrupts, such as system calls, exceptions, and software interrupts (INT instruction).
    - Task Gates: Used for hardware task switches.
- The IDT is set up during system initialization and can be modified by the kernel to handle custom interrupt handling routines.
- Hardware or software triggers an interrupt, and the CPU uses the IDT to locate and execute the appropriate interrupt handler (Interrupt Service Routine - ISR).



**Kernel and IDT**:
- The kernel sets up the IDT during boot to handle various exceptions and system calls.
- Kernel drivers can register their ISRs in the IDT to handle hardware interrupts from devices.
- The IDT plays a critical role in routing interrupts to the appropriate interrupt handlers in the kernel.

**IDT Manipulation**:
- Kernel functions like `lidt` (load IDT register) and `set_gate` are used to manipulate the IDT.
- These functions allow the kernel to set up and modify the IDT as needed, including registering custom interrupt handlers.

**Security Considerations**:
- Manipulating the IDT is a privileged operation and should be done carefully to prevent security vulnerabilities.

Remember that the IDT is specific to the x86 architecture, and other architectures may have their own mechanisms for managing interrupts and exceptions.