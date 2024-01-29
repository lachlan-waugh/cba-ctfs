---
title: "rootkits"
layout: "bundle"
outputs: ["Reveal"]
---

{{< slide class="center" >}}
## rootkits
### lunch & learn

---

{{% section %}}

### overview
* userland kits
* os internals
* kernelland kits

---

### what is a rootkit
* ~~exploitation/exercising a vulnerability~~\*
* ~~a program to get root~~\*
* a post exploitation tool for:
    * persistence, and
    * stealth

> \* not always at least

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
    * e.g. hiding other malware

{{% /section %}}

---

### how do rootkits work?

* you are the admin/superuser/root
* you can do anything
* **hooking functions**
    * appending additional functionality
    * not replacing it
* the operating system is just a program

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
* we tell the kernel to do this via syscalls

> syscalls are the eyes of the application

---

### system calls

![](/assets/img/rootkits/syscall.png)

{{% /section %}}

---

### kernelland kits

* two main types
    * hooking (static)
    * modules (dynamic)

---

{{% section %}}

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
* AV could detect
    * the system call table changes
    * or that the system call itself is changing
    * or that the address of the syscall is abnormal

---

### interrupt descriptor table
another table of function pointers

interrupts are how the system goes from user to kernel-mode
* page faults
* errors (divide-by-zero)

{{% /section %}}

---

{{% section %}}

### modules


{{% /section %}}

---

{{% section %}}

### detections

---

### syscall hooking
pretty easy to detect

|  syscall  | function * |
|-----------|------------|
| sys_write | 0xFFABCDEF |
| sys_read  | 0xAAAB0122 |
| sys_open  | 0xFFABCE10 |

---

### library hooking
```bash
# 6pm
cat /bin/ls | sha256sum
a6f7b874ea69329372ad75353314d7bcacd8c0be365023dab195bcac015d6009

# 7pm
cat /bin/ls | sha256sum
7aad4dc6e4d99b28d4857b4e06f7522a6aba48999a63ed850621dbbf89050185
```

> but I didn't update ls?

---

### why is it hard
performance

* detections for the kernel require kernel-code
* detections are really slow
    * do you verify every syscall?
    * every page fault?
* any AV would need to run as root

---

{{% /section %}}

---

### even scarier versions of rootkits
* hypervisor rootkits (sits above the os)
    * really bad for cloud computing
* BIOS rootkits
* Memory hooking

---

### Any questions?
