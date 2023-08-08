---
title: "04: binary exploitation"
layout: "bundle"
outputs: ["Reveal"]
---

## We'll get started at 13:05

---

{{< slide class="center" >}}
# binary exploitation
## week04

---

## disclaimer
* many of the tools and techniques discussed in these sessions could be used against real websites/applications
* don't do that

---

## acknowledgement of country
* We begin by acknowledging the Traditional Custodians of the land on which we meet, and pay our respects to their Elders past and present. We extend that arespect to Aboriginal and Torres Strait Islander peoples here today.

---

{{% section %}}

## what will we cover this session
* buffers overflows
* shellcode
* return-oriented programming

{{% /section %}}

---

{{% section %}}

## buffer overflows

---

#### Q: what happens if you write more content into a buffer than it can store?
A. the array resizes to fit the new content

B. the content gets truncated

C. an error is thrown

---

#### Q: what happens if you attempt to write more content into a buffer than it can store?
A. the array resizes to fit the new content

B. the content gets truncated

C. an error is thrown

**D. the content gets written after the end of the array**

---

### Where is this buffer stored?
* buffers are stored on the stack\*, next to other variables (& other interesting stuff we'll get to later)

* so if our content get's written after the end of the array, could we overwrite other variables?

> \*non-malloced buffers

---

### Example

```C
void main(void) {
    char input[40];
    int is_admin = 0;

    gets(input);
    if (is_admin) {
        // idk do something only admins should do
    }

    return;
}
```

---

## [Demo](will-add-later)

---

### What else can we do with it?
* what other content might you be able to overwrite?

* you can basically write until you overwrite something that causes a problem (e.g. a pointer?)

* what else is stored close to the local variables?

---

### stack frame?
![](/assets/img/week04/stack-grows-up.png)

---

### then what?
* what if instead of overwriting the local variables, we overwrote the return address?

* we could redirect the flow of the application

---

```
    0x18  [  ARGS  ] <- Parameters
    0x14  [  EIP   ] <- Stored Return Pointer
    0x10  [  EBP   ] <- Stored Frame Pointer
    0x0C  [  AAAA  ] <- these are local vars
    0x08  [  AAAA  ]
    0x04  [  AAAA  ]
    0x00  [  AAAA  ]
```

---

![](/assets/img/week04/stack-grows-down.png)

---

## Demo

{{% /section %}}

---

### problem!!
what if we don't have a basic win function, or useful variable to overwrite?

---

{{% section %}}
## 🐚 Shellcode
* Q: What is a win() function (or any function)?

---

## 🐚 Shellcode
* Q: What is a win() function (or any function)?
* A: It's just a sequence of assembly instructions

---

## 🐚 Shellcode
* Q: What is a win() function (or any function)?
* A: It's just a sequence of assembly instructions
    * Assembly is just bytes

---

## 🐚 Shellcode
* Q: What is a win() function (or any function)?
* A: It's just a sequence of assembly instructions
    * Assembly is just bytes
    * Bytes is just data (which we can send)

---

## 🐚 Shellcode
* Q: What is a win() function (or any function)?
* A: It's just a sequence of assembly instructions
    * Assembly is just bytes
    * Bytes is just data (which we can send)
* Hence if we can write some assembly instructions, and point EIP at them, we can  get code execution (e.g. read/write, pop a shell)!

---

### system calls
* we cannot directly read/write/open/create files

* this is handled by the kernel (the operating system)

* think of it like a function/api, we tell it what to do, it takes over and does it

---

### registers
* small memory regions located on the CPU

* RAM is the memory for the current processes

* registers is the memory for the current instruction

* what if we manipulated the registers to invoke our own instruction?

---

### how do we do that?
> [linux syscall references](https://cgi.cse.unsw.edu.au/~z5164500/syscall/)

---

```
// argv = envp = NULL
xor edx, edx
xor ecx, ecx

// push '/bin/sh' onto stack
push 0x68           
push 0x732f2f2f
push 0x6e69622f
mov ebx, esp

// call execve()
mov eax, 0xb    // Syscall Number 11
int 0x80        // Trigger syscall
```

---

## Demo

{{% /section %}}

---

### problem!
`NX` (`W^X`)

> regions of memory that are writable, cannot be executable (and vice-versa) 

---

{{% section %}}

## Return Oriented Programming

---

### ROP
* Instead of writing our own assembly instruction, we re-use existing instructions from the program.

* We use instructions preceding a `ret` (gadgets), so we can jump to them, execute them, and jump back.

* We chain these gadgets so we can execute a full payload, by: jumping to first one, executing it, jumping back, jumping to the second one, etc.

---

### Gadgets
* Instructions can comprise of multiple-bytes
    * If jump to an offset within an instructions
    * We could have an entirely new instruction

```
    0xAABBCCDD          0xAABBCCDD      0xAABBCCDD
      ^^^^^^^^              ^^                ^^^^
    MOV EAX, 12         XOR EAX, EAX       INC EAX; CALL WIN
```

> note, I made those ^^^ up entirely

---

### Old shellcode
```
/* argv = envp = NULL */
xor edx, edx
xor ecx, ecx

/* push '/bin/sh' onto stack */
push 0x68
push 0x732f2f2f
push 0x6e69622f
mov ebx, esp

/* call execve() */
mov eax, 0xb /* Syscall Number 11 */
int 0x80     /* Trigger syscall */
```

---

### How do we replicate this
`execve('/bin/sh', NULL, NULL)`
```
EAX = 0xB # (11)
EBX = address of /bin/sh
ECX = NULL
EDX = NULL

INT 0x80 Syscall
```

---

```
[GADGET_1] # EAX := 0xB # (11)
[GADGET_2] # EBX := address to /bin/sh
[GADGET_3] # ECX := NULL
[GADGET_4] # EDX := NULL
[GADGET_5] # INT 0x80 Syscall
```

---

### How do we find gadgets?
* [Ropper](https://github.com/sashs/Ropper)
* [ROPgadget](https://github.com/JonathanSalwan/ROPgadget)
* [ropr](https://github.com/Ben-Lichtman/ropr)

---

## Demo

{{% /section %}}

---

## Recommended challenges
* [exploit.education/pheonix](https://exploit.education/phoenix/)
* [pwnable.kr](http://pwnable.kr)
* [picoCTF](https://picoctf.org)

---

### next week
reverse engineering
* what if we weren't given the source code?
* static analysis
* dynamic analysis

---

## thanks!
that's all :)
