# Radare 2

"R2" is a rewrite from scratch of radare in order to provide a set of libraries and tools to work with binary files.

## Basics and Running

In order to run Radare

```text
r2 programName
```

Start radare with -d flag to debug like gdb.   


Like in vim, you can enter command mode with :

## Commands

* ?          Get information about characters you can use \(also works like a?\)
* aaa          Automatically analyse and autoname functions.
* afl          Print every function radare found.
* s   `newLocation`          Change current location to newLocation \(example sym.main\).
* pdf          Print the disassembly of current function.
* VV          Enter visual mode, showing control graph

### Control Flow

When running the control flow you will notice that rip \(instruction pointer register is at the execution\)

| Command | Action | Example |
| :---: | :--- | :---: |
| `db address` | Sets breakpoint at address | `db 0x004005bd` |
| `dc` | Runs the program | - |
| `s` | Step to next instruction | - |
| `S` | Step to next non-library function | - |
| `dr` | Show what is in registers | - |
| `ood` | Reload file in debug mode | - |
| `dr reg=value` | Sets reg to value | `dr=rip0x0040064b` |
| `afvn prevName newName` | Renames variable | `afvn local_2_4 sum` |
| `V!` | Change to complete info grid | - |

### Visual Mode

| Command | Action |
| :---: | :--- |
| `tab` and `shift+tab` | select blocks   |
| `shift+hjkl` | move the block |
| `p` | Cycle within different representations \(with or without address in beginning for example\) |
| `?` | Show Help |
| `shift + r` | change colors |

