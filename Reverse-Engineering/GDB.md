# GDB
gdb stands for GNU Project Debugger. <br>
It is, as the name says, a debugger, and can be used in reverse engineering in order to disassemble and analyze binary files.

## Running and Disassembling
In order to run it, you must execute:
```
gdb programname
```

So, the default syntax of gdb is AT&T. Since here we mainly use Intel syntax we may change it using

```
set disassembly-flavor intel
```

So, in order to disassemble a function you must use
```
disassemble main
```

It is important to notice that the program will be as it shows in memory, but you can use another software in order to visualize better the control flow of it.

## GDB Commands

### Control Flow
- `break *function` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sets a breakpoint at the given function.
- `si` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Step one instruction
- `ni` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Like

### Registers

- `info registers` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Shows the value at the registers of the given program at that moment
