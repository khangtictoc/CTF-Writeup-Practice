# re1.bin

Xem file format bằng **file** trên Kali Linux:
 
 ![image](https://user-images.githubusercontent.com/48288606/162609573-015d9b0f-bbcc-458b-af9a-18fd1cef5edd.png)
 
Vậy ta sẽ thực thi trên Linux để kiểm thử. Giờ thì dịch ngược với IDA, xem hàm main của chúng ta trong _pseudo-code_ :
 
<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162609651-e993be1e-5d56-4591-8d39-5ad432495d7f.png"> </p>

- 2 dòng đầu khai báo 2 biến con trỏ char **s1**, và **s1a**
- 4 dòng tiếp để in menu tên chương trình ra màn hình
- Sau đó biến **s1a** sẽ được xử lý với hàm **getString()** với đối số truyền vào là **s1** (Mạnh dạn đoán đây là hàm lấy ký tự người dùng nhập vào 🙃). Cứ vào hàm **getString()** cho chắc, vì đây không phải hàm thư việc C:
 
<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162609656-dcfe54ac-1e1b-45df-8866-50723ac2cdeb.png"> </p>

Hàm **getString()**:

+ Ta thấy hàm định nghĩa không cần đối số, vậy việc truyền biến **s1** vào không có ý nghĩa gì. Ban đầu hàm khai báo 1 số biến. Biến v4 lưu index của string, giá trị ban đầu chuỗi rỗng nên **v4 = 0**
+ Sau đó, 1 bước chính là cấp phát động bộ nhớ cho dữ liệu nhập vào với hàm **malloc()** với size bộ nhớ là **2u**, ptra sẽ là chuỗi string được cấp phát. Sau đó kiểm tra _cấp phát vùng nhớ nếu khả thi_, nếu bộ nhớ RAM máy tính hết thì sẽ in lỗi.

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162609668-033b26ed-5249-40ee-8d54-3cc560c9964a.png"> </p>

+ 1 bước chính khác còn lại là cho người dùng nhập vào bằng hàm **getchar()** với vòng lặp vô hạn **while(1)**,  hàm này sẽ cast  ký tự ta nhập vào thành số, và chỉ lấy duy nhất _1 ký tự_. Nếu ký tự nhập vào có ascii code bằng _10_ (tức là xuống dòng) thì vòng lặp while **break** và **return ptra** (trả về kết quả nhập) và được **cast** lại sang **char** đưa vào biến **s1a**, sau đó gán **v1 = v4 + 2** và được cấp phát với size mới **v1**, tăng _index **v4** lên 1_ để đến với ký tự tiếp theo. Sau đó lại tiếp tục thực hiện tương tự như công đoạn trên: _Cấp phát vùng nhớ nếu khả thi_
 
<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162609678-8e897a31-f45b-41ed-8762-542c69e46c58.png"> </p>

Giải thích dài dòng cho vui vậy thôi, hàm **getString()** đơn giản là lấy input user (đúng như ta đoán :v). Sau đó nếu input này bằng “**123456789**” thì in ra dòng chữ **“Bien joue, vous pouvez valider l'epreuve avec le pass**” tức là password đúng. 

Kiểm nghiệm lại:
 
Password: **123456789**

