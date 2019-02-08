# GDB

gdb stands for GNU Project Debugger.   
 It is, as the name says, a debugger, and can be used in reverse engineering in order to disassemble and analyze binary files.

## Running and Disassembling

In order to run it, you must execute:

```text
gdb programName
```

So, the default syntax of gdb is AT&T. Since here we mainly use Intel syntax we may change it using

```text
set disassembly-flavor intel
```

So, in order to disassemble a function you must use

```text
disassemble main
```

It is important to notice that the program will be as it shows in memory, but you can use another software in order to visualize better the control flow of it.

## GDB Commands

If only `Enter` is pressed the last it is equivalent to typing and running the last command again.

### Control Flow

* `run arg1, arg2...`   


         Runs the program and, if provided, with the arguments arg1, arg2, ...

* `break *address`   


         Sets a breakpoint at the given address. Can be used with function name insted of address.

* `del`   


         Removes all the breakpoints

* `si`   


         Step one instruction

* `ni`   


         Like si, but not showing execution of function calls \(skipping them\).

* `set $eax=x`   


         Sets register \(eax for example\) with value given 'x'

* `define hook-stop`   


         Define hook of stops, like the example below:

  ```text
  define hook-stop
  info registers
  x/24wx $esp
  x/2i $eip
  end
  ```

### Registers

* `info registers`   


         Shows the value at the registers of the given program at that moment

* `x/wx $reg`   


         Prints register "reg" content as hexadecimal

* `x/s $reg`   


         Prints register "reg" content as ascii

* `x/24wx $esp`    


         Prints the stack of the program \(24 words\)

* `x/2i $eip`   


         Prints the next two instructions.

* `x function`   


         Prints address of function

* `p function`   


         Prints the address and return type of function

* `info proc mappings`   


         Show the map of memory

