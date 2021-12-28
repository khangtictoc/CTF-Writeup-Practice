# ⛳ Stack Architect

- Description: Khởi động nc 45.122.249.68 10018
- Hint:
  - POP_2 gadget
  - func1 + func1 + pop_2 + 0x20010508 + 0x08052001 + func2 + win

## Write-up:


Ta có 4 biến cần quan tâm **check1**, **check2**, **check3**, **check4** là 4 biến toàn cục

![image](https://user-images.githubusercontent.com/48288606/147558474-45f43ce1-f6c4-4693-87fb-647582234b1f.png)

Xem mã giả của từng hàm trên IDA. Xét tại hàm **main()**:

![image](https://user-images.githubusercontent.com/48288606/147556706-61c727af-4529-4697-b4b9-edd08f0e369b.png)

Hàm main kiểm tra biến **check1**, nếu khác 0 thì thoát chương trình. Sau đó cho nhập chuỗi và tăng giá trị **check1** thêm 1. Tiếp đến xét hàm **win()**:

![image](https://user-images.githubusercontent.com/48288606/147556787-1d3b743f-db29-48e9-b804-26a833265cc0.png)

Đây là hàm ta cần đi đến để thực thi shell. Nếu các biến **check2**, **check3**, **check4** khác 0 thì ta sẽ thực thi được command. Xét hàm **func1(int)**:

![image](https://user-images.githubusercontent.com/48288606/147556763-b590f142-1ef8-4a5f-85c1-c87427adb8b9.png)

Hàm **func1** gán giá trị `check3 = 1` khi **check2 != 0** và **a1 = 536937736 (0x20010508)**, gán  `check2 = 1` khi **result = 0**; mà **result = 0** chỉ khi chuỗi **s1 = "I'm sorry, don't leave me, I want you here with me \~\~"**. Như vậy, tại đây ta mong muốn set giá trị cho **check2** và **check3**, ta phải gán được giá trị hợp lý cho biến **a1**, mà **a1** là đối số truyền vào nên ta phải pop sau khi vào hàm. Ta có hướng thực thi sau để thỏa mãn các điều kiện : **func1 -> func1 -> pop_a1 -> 536937736**.  Xét tại hàm **func2()**:

![image](https://user-images.githubusercontent.com/48288606/147556732-fabc7098-f520-4d98-8cb4-3281e1f2dc03.png)

Hàm **func2()** kiểm tra biến **check3 != 0** sau đó kiểm tra **v1 = 134553601 (0x8052001)** và gán `check4 = 1`. Tương tự, muốn set giá trị cho **check4** ta phải đáp ứng các điều kiện, ta phải thực thi công đoạn ở **func1()** trước, vì **func2()** kiểm tra **check3**. Một khi hoàn thành xong ta có thể nhảy đến hàm **win()**, luồng thực thi: **pop_v1 -> 134553601 -> func2 -> win**.

Tham khảo code exploit hoàn chỉnh [tại đây](stack.py)

Thử với file test:

![image](https://user-images.githubusercontent.com/48288606/147570923-176db54a-61b8-40e9-9dd0-5bc2183b0755.png)


Flag: **Wanna.One{neu_ban_chinh_phuc_duoc_chinh_minh_ban_co_the_chinh_phuc_duoc_the_gioi}**
