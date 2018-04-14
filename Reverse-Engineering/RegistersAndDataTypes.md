# Registers and Data Types
Here we'll be studying x86 and x86-64 architecture registers, following mainly Intel Pattern.
In order to store data in general, the main "thing" we use are registers.
## General Purpose Registers
At x86 architecture there are eight 32-bit general purpose registers (GPRs), some of them can also be divided into 8 and 16-bit registers. 

| Register      | Purpose           | 16 - Bits  | 8 Bits |
| ------------- |:-------------| :-----:| :-----:
| ESI		| Source in string/memory operations 	| SI | - | 
| EBP		| Base Frame Pointer			| BP | - | 
| ESP		| Stack Pointer				| SP | - | 
| EIP 		| Instruction Pointer (Program counter) | -  | - | 
| ECX		| Counter in loops 			| -  | - |
| EFLAGS	| Store operations - Ex: Flag Zero	| -  | - |
| EAX		| 					| AX |AH-AL| 
| EBX		| 					| -  | - | 
| EDX		| 					| -  | - | 
| EDI		| 					| DI | - |

## Instruction set
The x86 instruction set are around the data movement between registers and memory, classified in 5 types: 
 -  Immediate to register
 - Register to register
 - Immediate to memory
 - Register to memory and vice versa
 - Memory to memory - Only in RISC architectures.

### x86
The focus here will be the Intel syntax.
AT&T prefixes the register with % and immediates with $, which doesn't happen at Intel. They also add a prefix to the instruction to indicate operation width (long, byte, etc.).
At Intel syntax the destination come and then the source (op dest source), at AT&T it is the opposite.
Instructions have variable-lenght (1 to 15 bytes).

x86 uses [] to indicate memory access (similar to ***** at C/C++)
In order to sum or subtract address inside [] usually is used hexadecimal, for example:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; mov eax [ecx+10h] - Where the h is used to indicate hexadecimal notation.


 - MOV - mov ecx, [eax]
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sets ecx = [eax]
 - ADD - inc dword ptr [eax]
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Increments value at address eax.
 

### ARM
 - Load Word - LDR R3, [R3] 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Read the value at address R3.
 - Store Word - STR R2, [R3] 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Store the value from R2 at address R3.
 - Add to register - ADDS R2, R3, #1
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Add 1 to R3 and store at R2.

## References
- [Practical Reverse Engineering](https://www.amazon.com/Practical-Reverse-Engineering-Reversing-Obfuscation/dp/1118787315) - By [Bruce Dang](https://www.amazon.com/Bruce-Dang/e/B00IHK3NT0)



