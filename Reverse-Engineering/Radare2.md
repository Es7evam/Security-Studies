# Radare 2
"R2" is a rewrite from scratch of radare in order to provide a set of libraries and tools to work with binary files.

## Basics and Running
In order to run Radare
```
r2 programName
```
Start radare with -d flag to debug like gdb. <br>

Like in vim, you can enter command mode with :

## Commands
- ?  <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Get information about characters you can use (also works like a?)

- aaa  <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Automatically analyse and autoname functions.

- afl <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Print every function radare found.

- s &nbsp; `newLocation` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Change current location to newLocation (example sym.main).

- pdf   <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Print the disassembly of current function.

- VV  <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Enter visual mode, showing control graph

### Control Flow
When running the control flow you will notice that rip (instruction pointer register is at the execution)

| Command | Action | Example
| :-------------: | :---------------- | :---:
| `db address` | Sets breakpoint at address| `db 0x004005bd`
| `dc` | Runs the program | - |
| `s` | Step to next instruction | - |
|`S` | Step to next non-library function  |   |

### Visual Mode
| Command | Action     |
| :-------------: | :------------- |
| `tab` and `shift+tab` | select blocks <br> |
| `shift+hjkl` | move the block |
| `p` | Cycle within different representations (with or without address in beginning for example)|
| `?` | Show Help |
| `shift + r` | change colors |