

# Binary Protections

In case you already tried to make some reverse engineering challenge yourself, you've probably stumbled into some problems like "why the hell is this not working as it was supposed to" or "why is this not executing correctly" or even "wow I'm so dumb".  
And probably it was because of some of the protections gcc includes when compiling a binary.

## PIE - Position Independent Code

Pie, or position independent code, is one of the most common protections.
It means that the machine code that, being placed somewhere in primary memory, executes properly regardless of its absolute address.

Let's see an example of a `HelloWorld.c` code so it's clearer

```c
#include <stdio.h>

int main(){
    printf("Hello World");
}
```

Compiling and disassembling the binary using gdb (I am using peda extension, but that's not necessary)

```bash
gcc helloworld.c -o helloworld
gdb helloworld
disassemble main
```

![1552952052699](/home/estevam/.config/Typora/typora-user-images/1552952052699.png)

Above we see the code disassembly when not running. If you pay attention to the addresses, they start with 0x0...000 and then there is the address of the instruction.

If we run the program and try to disassemble it again, see what happens:

![1552952303509](/home/estevam/.config/Typora/typora-user-images/1552952303509.png)

As you can see, the address now is a little bit different, what makes exploitation harder because this will change based on when and where the code is executed.

So, in order to disable, simply compile like this:

```bash
gcc helloworld.c -o helloworld -no-pie
```

Then we have the new disassembly:

![1552952617724](/home/estevam/.config/Typora/typora-user-images/1552952617724.png)

If we run the code and disassemble the main, the addresses of the instructions will be the same. Try for yourself!

## Exec Stack 

## ASLR



