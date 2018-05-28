# GDB
gdb stands for GNU Project Debugger. <br>
It is, as the name says, a debugger, and can be used in reverse engineering in order to disassemble and analyze binary files.

## Running and Disassembling
In order to run it, you must execute:
```
gdb programName
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
If only `Enter` is pressed the last it is equivalent to typing and running the last command again.
### Control Flow
- `run arg1, arg2...` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Runs the program and, if provided, with the arguments arg1, arg2, ...
- `break *address` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sets a breakpoint at the given address. Can be used with function name insted of address.
- `del` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Removes all the breakpoints
- `si` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Step one instruction
- `ni` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Like si, but not showing execution of function calls (skipping them).
- `set $eax=x` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sets register (eax for example) with value given 'x'
- `define hook-stop` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Define hook of stops, like the example below:
```
define hook-stop
info registers
x/24wx $esp
x/2i $eip
end
```

### Registers

- `info registers` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Shows the value at the registers of the given program at that moment
- `x/wx $reg` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Prints register "reg" content as hexadecimal
- `x/s $reg` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Prints register "reg" content as ascii
- `x/24wx $esp`  <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Prints the stack of the program (24 words)
- `x/2i $eip` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Prints the next two instructions.
- `x function` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Prints address of function
- `p function` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Prints the address and return type of function
- `info proc mappings` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Show the map of memory
