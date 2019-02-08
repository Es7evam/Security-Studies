# Registers and Data Types  
Here we'll be studying x86 and x86-64 architecture registers, following mainly Intel Pattern.  
In order to store data in general, the main "thing" we use are registers.  
## Registers
At x86 architecture there are eight 32-bit general purpose registers (GPRs), some of them can also be divided into 8 and 16-bit registers.

### General Purpose Registers
| Register | Purpose |16 - Bits | 8 Bits |  
| ------------- | :------: |:-----:| :-----:  
| EAX | Acumulator, used for arithmetic operations and to store results| AX |AH-AL|  
| EBX | Base register for the stack| - | - |  
| ECX | Counter in loops | - | - |
| EDX | Used to store addresses of the data| - | - |  

### Address Registers
| Register | Purpose |16 - Bits |
| ------------- |:--------| :-----:|
| ESI | Source in string/memory operations | SI   
| EDI | Destination in string/memory operations | DI |
| EBP | Base Frame Pointer | BP |
| ESP | Stack Pointer | SP | |

### Another registers
| Register | Purpose |16 - Bits |
| ------------- |:--------| :-----:|
| EIP | Instruction Pointer (Program counter) | - |
| EFLAGS | Store operations - Ex: Flag Zero | - |  

## Instruction set  
The x86 instruction set are around the data movement between registers and memory, classified in 5 types:  
- Immediate to register  
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


- MOV - mov ecx, [eax]  <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sets ecx = [eax]  
- ADD - inc dword ptr [eax] <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Increments value at address eax.  
- SUB - sub eax, 0x20 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Subtracts eax by 0x20.
- PUSH - push eax <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pushes eax at the stack

- CMP - cmp eax, ebx <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if(eax == ebx) Sets eflags;
- JNE - jne 0x400086 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Jumps to given address if eflags was set to equal.

- CALL - call 0x400086 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Jumps to given address and saves current location at stack.
- RET - ret <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pops the address of the stack and returns control to that location - ("jump").
- LEA - lea eax, [esp+0x1c] <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Moves address of register to another (eax = esp+0x1c), used to pass parameters
- LEAVE - leave <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Moves ebp to esp and pops ebp from the stack.


### ARM  
- Load Word - `LDR R3, [R3]` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Read the value at address R3.  
- Store Word - `STR R2, [R3]`  <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Store the value from R2 at address R3.  
- Add to register - `ADDS R2, R3, #1`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Add 1 to R3 and store at R2.  