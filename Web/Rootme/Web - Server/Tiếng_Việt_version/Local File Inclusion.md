# Local File Inclusion

**30 Points**

**Title**: Abbreviated LFI

**Statement**: Get in the admin section.

## Analysis:

Vào mục **admin** thì bị yêu cầu `username` và `password`:

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/163718230-ec2b4933-a22a-4882-8287-589832d892e6.png"></p>

Vào link **sysadm** xem thử có gì:

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/163718028-dd579420-28a0-4baf-931d-b4d803d6e899.png"></p>

Vào tiếp **index.html** thì show ra nội dung file:

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/163718125-792abad3-af8f-4334-bfef-881ba30c4ab1.png"></p>

Phân tích input đầu vào của chúng ta tại các tham số của URL:
- `files` chỉ định đường dẫn thư mục chứa file
- `f` chỉ định file được lấy nội dung.

Nếu backend không kiểm tra cẩn thận các tham số, ta có thể chuyển sang đường dẫn ta mong muốn. Thử payload:

```
?files=../
```

> NOTE: Đường dẫn file và đường dẫn URL không có mối liên hệ với nhau. `http://challenge01.root-me.org/web-serveur/ch16/` và `http://challenge01.root-me.org/web-serveur/ch16/admin/` không có nghĩa thư mục hiện tại có folder **admin**

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/163718286-f32da144-1679-41d1-9c9f-73694bdcc84d.png"></p>

Vậy là đã thành công thực hiện **LFI** (chuyển về đường dẫn trước đó của thư hiện đang hiện hành, tức là resource location của trang web hiện tại). Ta thấy có một đường dẫn `admin`.

Nếu muốn đến thẳng cách giải quyết, đến mục [Solution](#solution). Nhưng mà cứ từ từ, giờ mình phân tích tiếp. Thử lùi lại thêm một vị trí nữa xem sao, có khi mình có thể lui ngay _root path_ rồi đọc thông tin nhạy cảm như `/etc/shadow` chẳng hạn:

```
?files=../../
```

![image](https://user-images.githubusercontent.com/48288606/163718400-1c2dd417-fda8-4758-83f7-b7ce3b1008f7.png)

Vậy là nếu mình đang ở đường dẫn `/challenge/web-serveur` thì  mình không được sang đường dẫn khác ngoài vùng `/challenge/web-serveur/ch16:/tmp`. Server dùng hàm [realpath()](https://www.php.net/manual/en/function.realpath.php) để thực hiện

> NOTE: Từ đây mình có thể hiểu được server phân chia và tạo các challenge trên đường dẫn `/tmp` và tạo challenge trong thư mục đó. Ví dụ: `ch16`. Điều này khá hữu ích khi ta exploit một số bài khác (có thể không nằm trong mảng web).

 mình vẫn còn parameter `f` là chưa dùng, thử payload với `f`:

```
?f=../
```

Không có gì hiện ra, thử lùi lại bao nhiêu đường dẫn nữa vẫn không được. Có thể phải cần biến `files` để xác định path

```
?files=sysadm&f=../
```
![image](https://user-images.githubusercontent.com/48288606/163720017-35202252-db56-4d52-8b30-8bc0a3e2873e.png)

Không có gì hiện ra @@. Thử đến `../../../` thì bung ra lỗi:

```
?files=sysadm&f=../../../
```

![image](https://user-images.githubusercontent.com/48288606/163719781-7afb7dd8-5772-4c5e-979d-350942a02609.png)

Ta thấy bên server xử lý biến `f` với hàm [file_get_contents()](https://www.php.net/manual/en/function.file-get-contents.php) (Hàm [realpath()](https://www.php.net/manual/en/function.realpath.php) xử lý biến `files`). Vì đường ngoài vùng cho phép nên **realpath()** trả về **false** và **file_get_content()** sẽ không đọc được file nào --> Lỗi

Vậy tại sao trong trường hợp trước đó lại không xuất lỗi. Đó là vì file vẫn hợp lệ, lưu ý một  _folder_name_ được  đưa vào **file_get_content()** sẽ không bị lỗi. 

## Solution: 

Với payload: `?files=../`, chúng ta có đường dẫn `admin`, truy cập vào thấy không có gì đặc biệt (tương tự với `text.gif`, `files`). Đối với file `index.php`:

![image](https://user-images.githubusercontent.com/48288606/163720294-5b73f313-fc33-478c-962a-6612d3feaeb9.png)

Đây là file mã nguồn để xử lý chính. Thử payload sau xem thử trong folder `admin` có những file nào:

```
?files=../admin
```

> NOTE: Nếu click thẳng vào `admin` thì tham số ta truyền vào sẽ là `?files=../&f=admin` và **file_get_content()** sẽ xuất ra nội dung rỗng, ta sẽ không xem được trong folder `admin` có gì

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/163720735-73902d45-e8ba-4f75-81d4-81804b653fdd.png"></p>

Vào `index.php`. Ta có thể thấy `username` và `password`  ở đây:

```php
$realm = 'PHP Restricted area';
$users = array('admin' => 'OpbNJ60xYpvAQU8');
```

Đăng nhập với xác thực trên

![image](https://user-images.githubusercontent.com/48288606/163721325-4799a398-f3fe-4c8c-8baa-6fb5d2c0842e.png)

Flag: **OpbNJ60xYpvAQU8**
