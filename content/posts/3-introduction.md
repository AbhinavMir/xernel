---
title: "Some introductory notes, points to cover, logistics"
draft: false
date: 1
---

Trying to cram a bunch of information in. 

What happens when you turn on your computer?

1. **POST (Power-On Self-Test):**
   - When a computer is powered on or reset, it goes through POST, a series of diagnostics.
   - POST checks for bootable devices (floppy disk, CD-ROM, hard disk) based on firmware configuration.

2. **Master Boot Record (MBR):**
   - The BIOS checks bootable devices for a boot signature (0x55, 0xAA at byte offsets 510 and 511).
   - If found, the MBR is loaded into memory at 0x0000:0x7c00, and execution is transferred to it.

3. **Early Environment:**
   - The early execution environment depends on the BIOS implementation.
   - Registers may not have valid values, except for DL (drive code).
   - The CPU is in Real Mode (unless specific BIOS activates Protected Mode).

4. **Kernel:**
   - The bootloader loads the kernel into memory and passes control to it.

5. **Loading:**
   - When booting from a hard drive, only 446 bytes are available for the boot record.
   - Tasks before running the kernel include determining the boot partition, locating the kernel image, loading it into memory, enabling protected mode, and preparing the runtime environment.

6. **Loading Approaches:**
   - Geek loading: Attempt to fit all tasks into the boot record (challenging).
   - One-stage loading: Use a stub program to transition to protected mode and prepare for the kernel.
   - Two-stage loading: Employ a separate stub program loaded below 1MB memory for various tasks.

7. **Traditional Way:**
   - The MBR relocates itself, identifies the active partition, and chainloads the first sector of that partition.

8. **Easy Way Out:**
   - Recommends using established bootloaders like GRUB for convenience and functionality.

9. **Other Methods:**
   - Various methods include loading stage 2 "raw," placing it between MBR and the first partition, using a tool to detect sectors/clusters, or creating an empty filesystem.

10. **Examples:**
    - DOS and Windows create empty filesystems, placing the kernel and shell as files.
    - Old Linux booted from floppy disks using a two-stage process.
    - Mention of a bootloader called "nuni" that switched to protected mode and loaded a file in a single bootsector.

## More notes
**Boot Signatures:**
- Boot signatures are specific byte sequences used to identify bootable sectors or partitions.
- In the context of Master Boot Records (MBRs), boot signatures consist of two bytes: 0x55 and 0xAA, located at byte offsets 510 and 511, respectively.
- When BIOS checks for a bootable device, it looks for these signatures to determine if a sector can be loaded as a boot record.

**Master Boot Record (MBR):**
- The Master Boot Record is a small program stored in the first sector (sector number 0) of a storage device, such as a hard drive or SSD.
- The MBR contains executable code that's responsible for initiating the boot process.
- It also includes a partition table, which describes the layout of the disk and the locations of primary partitions.
- The MBR is loaded into memory by the BIOS if it contains the correct boot signature, and control is transferred to it.

**Why 446 Bytes?:**
- The MBR typically consists of 512 bytes, but the first 446 bytes are reserved for the boot code.
- The remaining 66 bytes are used for the partition table, which describes up to four primary partitions on the disk.
- The decision to allocate 446 bytes for boot code is historical and practical. It allows enough space for essential boot code and leaves room for additional bootloader stages or custom code if needed.
- The partition table, which follows the boot code, is necessary for the BIOS to locate and boot the appropriate partition.

# More general notes
- OS concepts
    - Program between user and hardware
    - Allows users to execute programs
    - Provides protection, reliability, efficiency, predictability, convenience
- Computer system
    - Hardware, OS, programs, users
- System organization
    - CPUs, controllers connected via bus to shared memory
    - Memory accessed via controller
    - Concurrent execution competing for memory cycles
- Example: PC chipset architecture
- Bootstrap program
    - Initial program when system starts
    - Initializes CPU, memory, devices
    - Loads OS kernel into memory 
    - e.g. GRUB, LILO, Das U-Boot, systemd-boot/gummiboot
    - OS executes first process (init in Linux) then waits for events/interrupts
- x86 boot sector (MBR)
    - Assumed to be first sector on disk
    - Contains boot code and partition table
    - BIOS loads it into memory and executes it
    - Can chainload another boot sector
    - Must fit in 512 bytes before partition table
- BIOS booting steps:
    - Power on self test (POST) 
    - Check boot sectors on drives for valid signature
    - Read valid sector into memory at 0x7C00
    - May relocate it, replacing 0x7C00 with new sector
    - Execute boot code to load kernel
- x86 memory map
    - IVT, BIOS data, Conventional mem, Boot sector, Extended BIOS, Video/ROM
- BIOS services to kernel services timeline
- 32-bit memory layout  
    - Last 16 bytes accessible via EIP register
    - Upper areas unusable in real mode
    - 640KB conventional mem 
    - BIOS in high memory
- Computer system organization
    - CPUs, controllers, bus, shared memory
- System operation
    - Concurrent device and CPU execution
    - Controller in charge of device type
    - Controller has local buffer
    - CPU/DMA moves data between buffer and memory  
    - Controller interrupts CPU on completion
- Interrupt causes
    - I/O completion
    - Program faults
    - Bus errors, address errors, page faults
    - System calls
- x86 exceptions and interrupts
- Interrupt hardware
    - Cascaded 8259 PIC chips
    - Later advanced to support PCI interrupts
- Multiprocessor interrupt hardware
    - xAPIC, IOAPIC
- Interrupt handling
    - CPU stops execution and transfers control to ISR
    - Uses interrupt vector table of ISR addresses
    - May disable interrupts during processing
    - Resumes execution after
    - State preserved by storing registers and PC
- I/O structure
    - CPU loads controller registers to start I/O
    - Controller interprets then performs operation
    - Interrupts CPU on completion
- Synchronous vs asynchronous I/O
- Polling
    - CPU repeatedly checks device status
    - Uses device table to track requests
    - OS maintains wait queue per device
- DMA
    - Used for high speed devices 
    - Device controller transfers data between buffer and memory without CPU
    - Only one interrupt per block rather than per byte  
- Storage structure
    - Main memory directly accessible to CPU
    - Secondary storage extends capacity
- Storage hierarchy
    - Organized by speed, cost, volatility, capacity 
    - Caching - copying data to faster storage
    - Main memory is last cache for secondary storage
- Storage device hierarchy
- Storage performance of different levels
- Caching principles
    - Frequently used data copied to faster storage
    - Cache checked first before lower memory levels
    - Cache smaller than storage it caches
    - Cache management important - size and replacement policy
    - Exploits spatial and temporal locality
- Hardware protection
    - OS prevents interference between programs
    - Also protects itself from malicious programs
    - Hardware can detect errors and generate traps to terminate programs
    - Signals notify programs of kernel events from interrupts
- Dual mode protection
    - User and kernel modes
    - Hardware mode bit tracks current mode
    - Traps switch to kernel mode at privileged ring
    - Kernel executes privileged instructions
    - x86 has two mode bits 
- I/O protection
    - I/O instructions executed by OS 
    - Privileged - why?
- Memory protection
    - OS and interrupt code cannot be modified by user programs
    - User programs also isolated from each other
    - OS uses hardware to enforce address space boundaries
- CPU protection
    - Timer interrupts preempt processes 
    - Timeslice program execution
    - Allow multiple programs to share CPU
- User to kernel transition
    - Timer prevents infinite loops
    - OS sets interrupt after period
    - Decrements counter, generates interrupt at 0
    - Regains control or terminates exceeding program
- Computing environments
    - Traditional, office, home networks
    - Blurring over time
    - Networked access to shared resources
- Client-server
    - Dumb terminals -> PCs
    - Many systems now servers responding to client requests
- P2P
    - No clients or servers, all nodes are peers
    - Nodes act as client, server or both
    - Join network and register/discover services
- Web
    - Ubiquitous
    - More devices networked for web access
    - Traffic management with load balancers
    - Evolution of OSes from client to client/server

- Bootstrap program
    - First program executed on startup
    - Initializes CPU registers, memory, devices
    - Loads OS kernel into memory
    - e.g. GRUB, LILO, Das U-Boot, systemd-boot
    - OS runs first process (init) then waits for events
- Interrupts
    - Hardware interrupts from devices to CPU
    - Software interrupts/traps via syscalls or faults  
- Old PC boot sector
    - Assumed to be first disk sector
    - Has boot code and partition table
    - BIOS loads it into memory at 0x7C00
    - May relocate it and load new sector at 0x7C00
    - Size limited to 512 bytes before partition table
- UEFI boot procedure
    - Uses GPT partitioning and EFI system partition  
    - More advanced than MBR boot
- Example DOS boot sector
    - Assembly code
    - Partition table
    - 0xAA55 signature
- BIOS booting steps
    - POST  
    - Find valid boot sector and load at 0x7C00
    - Execute boot code
    - Real mode IVT and BIOS services
    - Protected mode kernel services
- 32-bit memory layout
    - Top 16 bytes accessible via EIP 
    - 640KB conventional memory
    - BIOS in high memory  
- Memory map
    - IVT, BIOS data, boot sector, conventional mem, extended BIOS, video/ROM
- System organization 
    - CPUs, controllers, bus, shared memory
- System operation
    - Concurrent device and CPU execution
    - Controller controls device type
    - Local buffering 
    - CPU/DMA copy between buffer and memory
    - Controller interrupts CPU on completion  
- Interrupt causes
    - I/O completion
    - Program faults  
    - Bus errors, address errors, page faults
    - System calls
- x86 exceptions and interrupts
- Interrupt hardware
    - Cascaded 8259 PIC chips
    - Advanced to support PCI interrupts
- Multiprocessor interrupt hardware
    - xAPIC, IOAPIC, LAPIC
- Interrupt handling
    - CPU transfers control to ISR
    - Uses interrupt vector table
    - May disable interrupts during processing
    - Saves state, restores after handling
    - Resumes execution 
- I/O structure
    - CPU loads controller registers
    - Controller performs operation
    - Interrupts CPU on completion
- Synchronous vs asynchronous I/O
- Polling
    - CPU checks device status repeatedly
    - Tracks requests in device table
    - OS maintains wait queue per device
- DMA
    - For high speed devices
    - Transfers between buffer and memory without CPU  
    - One interrupt per block rather than per byte
- Storage structure  
    - Main memory directly accessible to CPU
    - Secondary storage extends capacity 
- Hierarchy
    - Organized by speed, cost, volatility, capacity
    - Caching copies data to faster storage
    - Main memory as last cache for secondary 
- Device hierarchy
- Performance of storage levels 
- Caching principles
    - Frequently used data copied to faster storage 
    - Cache checked first
    - Smaller than storage it caches
    - Cache management important - size and replacement
    - Exploits locality  
- Hardware protection 
    - OS prevents interference between programs
    - Also protects itself
    - Hardware detects errors and traps programs
    - Signals notify programs of kernel events
- Dual mode protection
    - User and kernel modes  
    - Hardware mode bit tracks current mode
    - Traps switch to kernel mode at privileged ring
    - Kernel executes privileged instructions
    - x86 has two mode bits
- I/O protection  
    - I/O instructions executed by OS
    - Privileged - why?
- Memory protection
    - OS and interrupt code cannot be modified by users 
    - Users isolated from each other
    - OS enforces address space boundaries
- CPU protection
    - Timer interrupts preempt processes
    - Timeslice program execution
    - Allow sharing of CPU
- User to kernel transition
    - Timer prevents infinite loops
    - OS sets interrupt after period
    - Generates interrupt when counter hits 0
    - Regains control or terminates offending program