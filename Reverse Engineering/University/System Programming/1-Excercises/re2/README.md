# Re2.exe

Ta có 1 file PE (Window) **re2.exe**, chạy thử xem sao :

<p align="center"> <img width=800 height=130 src="https://user-images.githubusercontent.com/48288606/162610127-d95a1035-8cee-4004-9e03-9261229716ea.png"></p>

Tìm chuỗi **"Wrong Password"** để tìm xem chỗ xử lý ra chuỗi này. Vào _View -> Open subviews -> Strings (Shift + F12). _

<p align="center"> <img width=800 height=70 src="https://user-images.githubusercontent.com/48288606/162610238-35fcd559-8507-4cb1-ba1b-2f3b6beffc88.png"></p>

Ta thấy chuỗi này được lưu tại địa chỉ _0x00404060_ tại segment _.rdata_. Tìm tất cả hàm có liên quan đến chuỗi này. _Chuột phải -> List cross references to (Ctrl + X) -> OK_. Ta thấy có duy nhất hàm **sub_401726** sử dụng chuỗi này. Phân tích hàm dưới dạng _pseudo-code_:

![image](https://user-images.githubusercontent.com/48288606/162610444-b5886809-e481-4452-ae97-3bf8a7db45de.png)

> Lưu ý: Sử dụng thao tác _Chuột phải -> Jump to xref_ lên tất cả các hàm ta sẽ biết được luồng gọi hàm như sau: _start() -> sub_401190() -> sub_4017B8() -> sub_401726_ với tham số truyền vào **lớn hơn 1**. Còn các hàm khác thực hiện công việc như cấp phát vùng nhớ, kiểm tra số lượng tham số, ... Ta chỉ quan tâm đến hàm chính ở trên.

**a2** là length của chuỗi nhập vào, **a1** là number user nhập. Nếu ascii_code của các ký tự tại các vị trí **0, 1, 2, 3, 4, 5, 6** thỏa: **83(S), 80(P), 97(a), 67(C), 73(I), 111(o), 83(S)** --> "SPaCIoS", thì kết quả trả về là **"Gratz man :)"** thành công.

Kiểm tra lại: 

<p align="center"> <img width=400 height=50 src="https://user-images.githubusercontent.com/48288606/162611096-108e4682-4d82-4e81-a090-c22427d4e1ef.png"></p>

Password: **SPaCIoS**
