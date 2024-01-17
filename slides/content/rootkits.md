---
title: "rootkits"
layout: "bundle"
outputs: ["Reveal"]
---

{{< slide class="center" >}}
## rootkits
### lunch && learn 

---

{{% section %}}

### overview
* userland kits
* os internals
* kernelland kits

---

### what is a rootkit
* ~~exploitation/exercising a vulnerability~~
* ~~a program to get root~~
* post exploitation tool for persistence and stealth

---

### an example
you've
* infected a device (gotten rce, malware, etc)
* escalated your privileges to root
* now what do you want to do?

---

### what do we want a rootkit to do
* persistence
    * surviving reboots
    * backdooring
* stealth
    * hiding processes/files/network activity
    * cleaning logs
    * evading detection

{{% /section %}}

---

{{% section %}}

### userland kits
* often based on replacing utilities
    * *ls*: doesn't show rootkit's files
    * *netstat*: doesn't reveal rootkit's ports
    * *ps*: doesn't show rootkit's processes
    * *cat*: show fake file contents

---

### 
* overriding system libraries
    * overwriting `libc.so`
    * `LD_PRELOAD`

---

### windows
relatively common on windows

* overwriting DLLs (dynamically linked libraries)
* ~~IAT (Import Address Table) Hooking~~ (its RO now)
* Inline Hooking

---

### problems
these are all pretty bad

* these are pretty easy to detect by a simple AV
    * the hash of the files are changing
* does pythons `os.listdirs()` use `ls`? ... no

{{% /section %}}

---

{{% section %}}

### operating systems

![](/assets/img/rootkits/rings.png)

---

### kernel
kernel is the most privileged part of an OS

* operates in ring0
* can do basically anything
    * execute any instruction
    * read/write anywhere
    * access hardware

> used to be like this, not anymore

---

### userland
* userland we can't access hardware
    * we don't modify the pixels when calling `print()`
    * we can't just directly read the harddrive

> we tell the kernel to do this via syscalls

---

### system calls

![](/assets/img/rootkits/syscall.png)

---

### hooking
every userland program uses syscalls

* what if we overwrote these syscalls
* and made them do what we want

---

### how do we do this
that's the hard part

* overwriting the system call table
* overwriting the system call itself

---

### still kinda bad
* AV could detect the system call table changes
* or that the system call itself is changing

---

### interrupt descriptor table
another table of function pointers

interrupts are how the system goes from user to kernel-mode
* page faults
* errors (divide-by-zero)

> syscalls are the eyes of the application

{{% /section %}}

---

{{% section %}}

### kernelland kits
TODO

{{% /section %}}
