# ⛳ Shellcode

- Description: dễ mà tự viết đi trên trên mạng không có đâu
  - Bắt buộc dùng open, read, write để đọc flag
  - Không cần quan tâm đến seccomp
  - Dùng syscall ngoài open, read, write sẽ bị khóa
  - nc 45.122.249.68 10017
- Hint:
  - bạn Nhật Trường có một bài blog tương tự bài này trên x86, thử chuyển code sang x86-64 bạn sẽ giải được bài này link: https://drx.home.blog/2019/04/03/pwnable-tw-orw/

## Write-up:

Flag: **Wanna.One{ve_so_sang_mua_chieu_xo_em_nghi_anh_la_ai_ma_sang_cua_chieu_do}**
