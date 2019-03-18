# x86 Hello World

Taking the code as for example, it is recommended to understand first the basic concepts of x86 Assembly, such as the mov instruction.

Take for example this program:

```text
;; Program Hello WOrld
section .text
global _start

_start:
        mov     edx,len                             ;message length
        mov     ecx,msg                             ;message to write
        mov     ebx,1                               ;file descriptor (stdout)
        mov     eax,4                               ;system call number (sys_write)
        int     0x80                                ;call kernel

        mov     eax,1                               ;system call number (sys_exit)
        int     0x80                                ;call kernel

section     .data
        msg     db  'Hello, world!',0xa                 ;our dear string
        len     equ $ - msg                             ;length of our dear string
```

#### Understanding the code

It starts out with a comment, that is `;` as you can see.

Afterwards, it is necessary to specify the sections of the code. Since the Assembly goes directly into the memory, you need to specify what is the `text` fragment and what is `data` \(non executable code, usually used to store strings, some variables, etc\). As you can see, a global label `_start`is defined. That is necessary so that when the compiler gets and analyses this code it will know where to start running \(It is a default label\).

Lets jump into the `.data` section. First it will declare a define byte \(`db`\) that we called `msg`, with the string that we want to print out, together with `0xa`, that is a newline character \(equivalent to `\n` in C, for example\). In the next line, we define a `len` variable that represents the length of the string, that is, the current place at the memory this instruction is \(represented by `$`\) subtracted by the start of the string \(`msg`\).

Going back to the `_start` label \(also called as a function in this case\), at the first 4 lines we just store the variables at the registers `edx` and `ecx`, than we set `ebx` as 1 and `eax` as 4. This means that, since we want to write something to `stdout` \(or standard output\), we will use the `write` syscall, that asks for the argument `fd`, passed through by `ebx` as a convention, as seen at [System Calls Reference](https://syscalls.kernelgrok.com/). So `int`erruption 0x80 will be called \(that is a _syscall_\), which will print "Hello, World!" at the terminal.

In the end, eax will be set to 1, meaning the _syscall_ exit. Then it will be called through `int 0x80`, exiting the program.

In case we wanted to set a `return 0` at the end of the code, we could just `mov ebx, 0` just before the syscall.

#### Compiling and Testing the code

In order to compile the x86 Assembly code, a good way is to use [nasm](https://nasm.us/) compiler.

Supposing we have a `hello.asm` code, we can compile as

```bash
nasm -f elf hello.asm
```

Doing that we specify that the format of the file will be an `elf` \(32 bits\) and a new object `hello.o` will be produced.

Still, that is not our executable file, in order to get that we need to use `ld` command to link the object with the libraries of our system, which can be easily done:

```bash
ld -s -o hello hello.o -m elf_i386
```

It simply links the generated object to a `hello` executable, that has the format `elf_i386`. In case any error occurs, check out if you have the `32bits glibc` at your own operational system.

So, you can execute simply using

```bash
./hello
```

And that's it, you have your Hello World :D

### References

* [Linux System Calls Reference](https://syscalls.kernelgrok.com/)
* [x86 Hello World](http://asm.sourceforge.net/intro/hello.html)
* [nasm](https://nasm.us/)

